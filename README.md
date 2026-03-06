# Knowledge OS Starter

> AI-native personal knowledge base starter for Obsidian, Git, Markdown, and AI Agent workflows.

一个面向 Obsidian、Git、Markdown 和 AI Agent 工作流的开源个人知识库模板。

`obsidian` `personal knowledge base` `pkm` `second brain` `zettelkasten` `markdown` `ai agent` `knowledge management`

[English README](README_EN.md)

它不是传统笔记仓库，而是一个把信息流转为知识、思考、项目、创作和资产的 `Knowledge OS` 起点。它也可以被理解为一个 `Obsidian vault template`、`PKM starter`、`second brain template`、`knowledge management system` 和 `AI-ready markdown repository`。

## 项目定位

这个仓库可以被理解为：

- 一个适合长期维护的 `personal knowledge base`
- 一个面向 Obsidian 的 `Markdown-first` 知识库模板
- 一个兼容检索、自动化和 Agent 工作流的 `AI-native PKM starter`
- 一个结合 `second brain`、`zettelkasten`、项目管理和创作流程的结构化仓库

## 适合谁

- 想把个人知识库做成长期可维护系统的人
- 想让知识库同时适合人阅读和 AI 调用的人
- 想基于 Markdown + Git 开源自己的知识管理方法的人
- 想把内容生产、研究和项目沉淀放进同一个结构的人

## 核心特性

- 六层增强结构：`Input -> Knowledge -> Thinking -> Project -> Creation -> Assets`
- 原子知识规范：一个知识一个文件
- 统一命名规则与唯一 ID
- 机器可读 frontmatter，便于 AI 检索与自动化
- 开箱可用的知识、思考、创作、项目模板
- 零依赖脚本：自动编号与知识层规范校验
- GitHub 开源所需的基础文档、模板和 CI 工作流

## 仓库结构

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

## 快速开始

### 1. 复制模板

你可以直接把这个仓库作为你的知识库根目录，或者 fork 后重命名。

### 2. 阅读核心规则

建议按这个顺序阅读：

1. [00_System/01-知识库架构总纲.md](00_System/01-知识库架构总纲.md)
2. [00_System/03-目录结构规范.md](00_System/03-目录结构规范.md)
3. [00_System/04-文件命名规范.md](00_System/04-文件命名规范.md)
4. [00_System/06-元数据规范.md](00_System/06-元数据规范.md)
5. [00_System/07-信息流转工作流.md](00_System/07-信息流转工作流.md)

### 3. 新建知识

先查询下一个编号：

```bash
python3 scripts/kb_tools.py next-id AI
```

然后在对应领域目录下创建文件，例如：

```text
02_Knowledge/AI/KNOW-AI-003-你的主题.md
```

### 4. 校验知识层

```bash
python3 scripts/kb_tools.py validate
```

## 文档入口

- [系统说明](00_System/README.md)
- [脚本说明](scripts/README.md)
- [开源发布资料包](docs/OPEN_SOURCE_PACKAGE.md)
- [GitHub 发布操作流程](docs/GITHUB_PUBLISH_FLOW.md)
- [开源发布检查清单](docs/OPEN_SOURCE_RELEASE_CHECKLIST.md)

## 开源内容清单

这个仓库已经准备了以下适合 GitHub 开源的资料：

- [LICENSE](LICENSE)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- [SECURITY.md](SECURITY.md)
- [CHANGELOG.md](CHANGELOG.md)
- [Issue 模板](.github/ISSUE_TEMPLATE)
- [PR 模板](.github/pull_request_template.md)
- [知识校验 GitHub Actions](.github/workflows/validate-knowledge.yml)

## 建议的开源定位

推荐把它定位为：

`An AI-native personal knowledge base starter for Obsidian, Git, Markdown, and structured knowledge workflows.`

如果你想做中文开源主页，可以使用：

`一个面向 Obsidian、Git、Markdown 与 AI Agent 工作流的 AI 原生个人知识库模板。`

## 建议的 GitHub Topics

建议优先添加这些 topics：

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

## 许可证

本仓库默认使用 [MIT License](LICENSE)。

## 贡献

欢迎提交 issue、模板改进、脚本增强和文档修订。开始前请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。
