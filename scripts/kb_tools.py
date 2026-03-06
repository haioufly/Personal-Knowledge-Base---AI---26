#!/usr/bin/env python3
"""Knowledge base helper tools.

Supported commands:
- next-id: print the next knowledge ID for a given domain.
- validate: validate knowledge file naming and required frontmatter.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


DOMAIN_TO_DIR = {
    "AI": "AI",
    "TECH": "技术",
    "BIZ": "商业",
    "PSY": "心理",
    "SOC": "社会",
    "DES": "设计",
    "GAME": "游戏设计",
}

DIR_TO_DOMAIN = {directory: domain for domain, directory in DOMAIN_TO_DIR.items()}
KNOWLEDGE_FILENAME_RE = re.compile(r"^KNOW-([A-Z]+)-(\d{3})-(.+)\.md$")
REQUIRED_FIELDS = (
    "id",
    "type",
    "domain",
    "tags",
    "status",
    "source_type",
    "created",
    "updated",
)
ALLOWED_STATUS = {"active", "draft", "archived"}
ALLOWED_SOURCE_TYPE = {"book", "paper", "article", "video", "conversation", "synthesis"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TAG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


@dataclass
class ValidationError:
    path: Path
    message: str


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def knowledge_root() -> Path:
    return repo_root() / "02_Knowledge"


def iter_knowledge_files() -> list[Path]:
    root = knowledge_root()
    files: list[Path] = []
    for path in sorted(root.rglob("*.md")):
        if path.name in {"README.md", "知识模板.md"}:
            continue
        files.append(path)
    return files


def parse_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    data: dict[str, object] = {}
    current_key: str | None = None
    items: list[str] = []

    for line in lines[1:]:
        if line.strip() == "---":
            if current_key is not None:
                data[current_key] = items
            return data

        if line.startswith("  - ") or line.startswith("\t- "):
            if current_key is not None:
                items.append(line.split("- ", 1)[1].strip())
            continue

        if current_key is not None:
            data[current_key] = items
            current_key = None
            items = []

        if ":" not in line:
            continue

        key, raw_value = line.split(":", 1)
        key = key.strip()
        value = raw_value.strip()
        if value == "":
            current_key = key
            items = []
        else:
            data[key] = value

    return {}


def next_id(domain: str) -> str:
    if domain not in DOMAIN_TO_DIR:
        valid = ", ".join(sorted(DOMAIN_TO_DIR))
        raise ValueError(f"unknown domain '{domain}', expected one of: {valid}")

    highest = 0
    for path in iter_knowledge_files():
        match = KNOWLEDGE_FILENAME_RE.match(path.name)
        if not match:
            continue
        file_domain, number, _title = match.groups()
        if file_domain == domain:
            highest = max(highest, int(number))
            continue

        metadata = parse_frontmatter(path)
        if metadata.get("domain") == domain:
            highest = max(highest, int(number))

    return f"KNOW-{domain}-{highest + 1:03d}"


def validate_knowledge_file(path: Path) -> list[ValidationError]:
    errors: list[ValidationError] = []
    relative_path = path.relative_to(repo_root())

    match = KNOWLEDGE_FILENAME_RE.match(path.name)
    if not match:
        errors.append(
            ValidationError(relative_path, "filename must match KNOW-领域代码-编号-中文主题.md")
        )
        return errors

    domain_code, _number, title = match.groups()
    if not title.strip():
        errors.append(ValidationError(relative_path, "filename title segment cannot be empty"))

    expected_domain = DIR_TO_DOMAIN.get(path.parent.name)
    if expected_domain is None:
        errors.append(
            ValidationError(relative_path, f"unexpected knowledge directory '{path.parent.name}'")
        )
    elif expected_domain != domain_code:
        errors.append(
            ValidationError(
                relative_path,
                f"filename domain '{domain_code}' does not match parent directory '{path.parent.name}'",
            )
        )

    metadata = parse_frontmatter(path)
    if not metadata:
        errors.append(ValidationError(relative_path, "missing or malformed frontmatter"))
        return errors

    for field in REQUIRED_FIELDS:
        if field not in metadata:
            errors.append(ValidationError(relative_path, f"missing required frontmatter field '{field}'"))

    if metadata.get("id") and metadata["id"] != path.stem.split("-", 3)[0] + "-" + path.stem.split("-", 3)[1] + "-" + path.stem.split("-", 3)[2]:
        errors.append(ValidationError(relative_path, "frontmatter id must match filename id prefix"))

    if metadata.get("type") and metadata["type"] != "knowledge":
        errors.append(ValidationError(relative_path, "frontmatter type must be 'knowledge'"))

    if metadata.get("domain") and metadata["domain"] != domain_code:
        errors.append(ValidationError(relative_path, "frontmatter domain must match filename domain"))

    status = metadata.get("status")
    if isinstance(status, str) and status not in ALLOWED_STATUS:
        errors.append(ValidationError(relative_path, f"invalid status '{status}'"))

    source_type = metadata.get("source_type")
    if isinstance(source_type, str) and source_type not in ALLOWED_SOURCE_TYPE:
        errors.append(ValidationError(relative_path, f"invalid source_type '{source_type}'"))

    for date_field in ("created", "updated"):
        value = metadata.get(date_field)
        if isinstance(value, str) and not DATE_RE.match(value):
            errors.append(ValidationError(relative_path, f"field '{date_field}' must use YYYY-MM-DD"))

    tags = metadata.get("tags")
    if not isinstance(tags, list) or not tags:
        errors.append(ValidationError(relative_path, "frontmatter tags must be a non-empty list"))
    else:
        for tag in tags:
            if not TAG_RE.match(tag):
                errors.append(ValidationError(relative_path, f"invalid tag '{tag}'"))

    return errors


def validate() -> int:
    files = iter_knowledge_files()
    errors: list[ValidationError] = []

    ids: dict[str, list[Path]] = {}
    for path in files:
        metadata = parse_frontmatter(path)
        if isinstance(metadata.get("id"), str):
            ids.setdefault(metadata["id"], []).append(path.relative_to(repo_root()))
        errors.extend(validate_knowledge_file(path))

    for knowledge_id, paths in ids.items():
        if len(paths) > 1:
            joined = ", ".join(str(path) for path in paths)
            for path in paths:
                errors.append(ValidationError(path, f"duplicate id '{knowledge_id}' also found in: {joined}"))

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error.path}: {error.message}")
        return 1

    print(f"Validation passed: {len(files)} knowledge files checked.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Knowledge base helper tools")
    subparsers = parser.add_subparsers(dest="command", required=True)

    next_id_parser = subparsers.add_parser("next-id", help="print the next knowledge ID for a domain")
    next_id_parser.add_argument("domain", help="domain code, e.g. AI or BIZ")

    subparsers.add_parser("validate", help="validate knowledge files")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "next-id":
        try:
            print(next_id(args.domain.upper()))
        except ValueError as exc:
            print(f"Error: {exc}", file=sys.stderr)
            return 2
        return 0

    if args.command == "validate":
        return validate()

    parser.error(f"unsupported command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
