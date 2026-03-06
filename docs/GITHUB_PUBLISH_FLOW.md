# GitHub 发布操作流程

这份流程默认你要把当前仓库作为一个公开的开源产品发布到 GitHub。

## 阶段一：本地整理

### 1. 检查公开边界

确认以下内容不会公开：

- 私人日记
- 私人聊天全文
- 商业敏感信息
- 未获得授权的长篇摘录
- 任何密钥、Token、账号信息

### 2. 检查仓库结构

确认以下路径都存在：

- `00_System`
- `01_Input`
- `02_Knowledge`
- `03_Thinking`
- `04_Project`
- `05_Creation`
- `06_Assets`
- `90_Archive`
- `scripts`
- `docs`
- `.github`

### 3. 本地校验

运行：

```bash
python3 scripts/kb_tools.py validate
```

如果校验失败，先修复知识层文件命名和 frontmatter。

### 4. 检查 README

确认根目录 `README.md` 已经能让陌生人理解：

- 这是什么
- 为什么有价值
- 如何开始使用
- 下一步看什么文档

## 阶段二：初始化 Git

如果当前目录还不是 Git 仓库：

```bash
git init
git add .
git commit -m "feat: initial open-source release"
```

说明：

- `.gitignore` 已经准备好，会忽略 `.DS_Store` 等无关文件。
- 如果 `git add .` 前已经有不想公开的文件，先删除或移动。

## 阶段三：创建 GitHub 仓库

### 1. 在 GitHub 新建仓库

建议仓库名：

- `knowledge-os-starter`

可选仓库名：

- `ai-personal-kb-starter`
- `obsidian-knowledge-os-template`

### 2. 填写仓库信息

建议：

- Visibility: `Public`
- Description: 使用 [OPEN_SOURCE_PACKAGE.md](OPEN_SOURCE_PACKAGE.md) 中的推荐文案
- 不要勾选自动创建 README、.gitignore 或 LICENSE，因为本地已准备好

### 3. 添加远程仓库并推送

```bash
git remote add origin <你的 GitHub 仓库地址>
git branch -M main
git push -u origin main
```

## 阶段四：配置 GitHub 页面信息

### 1. 补充 About 区域

设置：

- Description
- Website（如暂无可留空）
- Topics

推荐 topics 见 [OPEN_SOURCE_PACKAGE.md](OPEN_SOURCE_PACKAGE.md)。

### 2. 检查社区文件是否生效

仓库推送后，GitHub 会自动识别：

- `LICENSE`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `.github/ISSUE_TEMPLATE`
- `.github/pull_request_template.md`

### 3. 检查 Actions

进入 GitHub 的 `Actions` 页面，确认 `Validate Knowledge Files` 工作流可正常运行。

## 阶段五：打第一个 Release

### 1. 创建标签

```bash
git tag v0.1.0
git push origin v0.1.0
```

### 2. 在 GitHub 创建 Release

建议标题：

`v0.1.0 - Initial public release`

建议内容：

- Initial Knowledge OS Starter structure
- System docs for naming, metadata, links, and workflow
- Templates for knowledge, thinking, project, and creation notes
- Validation and next-ID helper script
- GitHub community files and CI workflow

## 阶段六：发布后的维护动作

### 1. 置顶文档

建议在 README 或 pinned issue 里告诉用户：

- 从哪里开始读
- 如何创建第一个知识节点
- 如何校验

### 2. 处理首批 issue

优先处理三类反馈：

- 不清楚如何上手
- 命名或元数据规则太重
- Obsidian / GitHub 兼容性问题

### 3. 规划后续版本

推荐顺序：

1. `v0.2.0` 新建知识文件脚本
2. `v0.3.0` 主题索引页/地图页
3. `v0.4.0` 更完整示例内容

## 最后检查清单

在点击公开前，确保：

- 没有私人或敏感内容
- `README.md` 可独立解释项目
- `python3 scripts/kb_tools.py validate` 通过
- LICENSE 和社区文件齐全
- Release 文案已准备
