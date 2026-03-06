# Contributing

Thanks for contributing to Knowledge OS Starter.

## Scope

Useful contributions include:

- template improvements
- documentation clarifications
- validation script enhancements
- better examples for knowledge, thinking, and creation layers
- GitHub workflow and community tooling improvements

## Before You Start

1. Read [00_System/01-知识库架构总纲.md](00_System/01-知识库架构总纲.md).
2. Read [00_System/04-文件命名规范.md](00_System/04-文件命名规范.md).
3. Read [00_System/06-元数据规范.md](00_System/06-元数据规范.md).

## Development Rules

- Keep the repository Markdown-first and low-dependency.
- Do not introduce plugins or external services as hard requirements.
- Keep examples small and reusable.
- Preserve compatibility with plain GitHub rendering and Obsidian usage.

## Knowledge File Rules

If you add or edit files in `02_Knowledge`:

- use the `KNOW-领域代码-编号-中文主题.md` naming format
- keep `type: knowledge`
- include all required frontmatter fields
- keep tags in English `kebab-case`
- link the node to at least two related notes when possible

Run validation before submitting:

```bash
python3 scripts/kb_tools.py validate
```

## Pull Request Process

1. Create a focused branch.
2. Keep the change scoped to one concern.
3. Explain what changed and why.
4. Include examples or screenshots if the change affects onboarding or GitHub presentation.
5. Make sure validation passes.

## Large Changes

If you want to change the core structure, naming rules, metadata schema, or open-source positioning, open an issue first and describe the rationale before sending a PR.
