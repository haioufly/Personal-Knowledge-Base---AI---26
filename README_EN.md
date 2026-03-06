# Knowledge OS Starter

> AI-native personal knowledge base starter for Obsidian, Git, Markdown, and AI Agent workflows.

An open-source personal knowledge base starter for Obsidian, Git, Markdown, and AI Agent workflows.

`obsidian` `personal knowledge base` `pkm` `second brain` `zettelkasten` `markdown` `ai agent` `knowledge management`

[中文说明](README.md)

This repository is not just a note vault. It is a `Knowledge OS` starter that turns information into reusable knowledge, thinking frameworks, project context, creative output, and long-term assets. It can also be discovered and used as an `Obsidian vault template`, `PKM starter`, `second brain template`, `knowledge management system`, and `AI-ready markdown repository`.

## Positioning

This repository can be understood as:

- a long-term maintainable `personal knowledge base`
- a `Markdown-first` template for Obsidian users
- an `AI-native PKM starter` for retrieval, automation, and agent workflows
- a structured workflow that combines `second brain`, `zettelkasten`, project context, and creative output

## Who It Is For

- people building a long-term personal knowledge system
- people who want notes that work for both humans and AI
- people who want a Markdown + Git workflow that can be open-sourced
- people combining research, writing, projects, and knowledge management in one repository

## Core Features

- six-layer structure: `Input -> Knowledge -> Thinking -> Project -> Creation -> Assets`
- atomic knowledge rule: one knowledge unit per file
- consistent naming rules and unique IDs
- machine-readable frontmatter for AI retrieval and automation
- reusable templates for knowledge, thinking, creation, and project notes
- zero-dependency helper script for next-ID generation and validation
- GitHub-ready community files and CI workflow

## Repository Structure

```text
.
├── 00_System
├── 01_Input
├── 02_Knowledge
├── 03_Thinking
├── 04_Project
├── 05_Creation
├── 06_Assets
├── 90_Archive
├── docs
├── scripts
└── .github
```

## Quick Start

### 1. Copy the Starter

Use this repository directly as your vault root, or fork it and rename it for your own setup.

### 2. Read the Core Rules

Recommended reading order:

1. [00_System/01-知识库架构总纲.md](00_System/01-知识库架构总纲.md)
2. [00_System/03-目录结构规范.md](00_System/03-目录结构规范.md)
3. [00_System/04-文件命名规范.md](00_System/04-文件命名规范.md)
4. [00_System/06-元数据规范.md](00_System/06-元数据规范.md)
5. [00_System/07-信息流转工作流.md](00_System/07-信息流转工作流.md)

### 3. Create a New Knowledge Note

Get the next ID first:

```bash
python3 scripts/kb_tools.py next-id AI
```

Then create a file in the matching domain folder, for example:

```text
02_Knowledge/AI/KNOW-AI-003-YourTopic.md
```

### 4. Validate the Knowledge Layer

```bash
python3 scripts/kb_tools.py validate
```

## Documentation

- [System Docs](00_System/README.md)
- [Scripts](scripts/README.md)
- [Open Source Package](docs/OPEN_SOURCE_PACKAGE.md)
- [GitHub Publish Flow](docs/GITHUB_PUBLISH_FLOW.md)
- [Open Source Release Checklist](docs/OPEN_SOURCE_RELEASE_CHECKLIST.md)

## Open-Source Package

This repository already includes:

- [LICENSE](LICENSE)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- [SECURITY.md](SECURITY.md)
- [CHANGELOG.md](CHANGELOG.md)
- [Issue Templates](.github/ISSUE_TEMPLATE)
- [Pull Request Template](.github/pull_request_template.md)
- [Knowledge Validation Workflow](.github/workflows/validate-knowledge.yml)

## Recommended Positioning

Suggested one-line description:

`An AI-native personal knowledge base starter for Obsidian, Git, Markdown, and structured knowledge workflows.`

## Suggested GitHub Topics

Recommended topics:

- `knowledge-management`
- `personal-knowledge-base`
- `obsidian`
- `obsidian-md`
- `markdown`
- `pkm`
- `second-brain`
- `zettelkasten`
- `knowledge-base`
- `note-taking`
- `ai-agent`
- `ai-native`
- `productivity`
- `digital-garden`
- `templates`

## License

This repository uses the [MIT License](LICENSE).

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.
