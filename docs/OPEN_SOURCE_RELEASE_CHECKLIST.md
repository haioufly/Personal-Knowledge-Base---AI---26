# 开源发布检查清单

## 内容安全

- [ ] 没有私人笔记、私人对话或敏感项目内容
- [ ] 没有版权不明的长篇摘录
- [ ] 没有密钥、Token、账号或环境变量信息

## 仓库完整性

- [ ] 根目录 README 可独立解释项目
- [ ] `00_System` 文档完整
- [ ] 模板文件可直接复用
- [ ] 至少有一组示例知识 / 思考 / 创作节点
- [ ] `docs` 下有开源资料和发布流程

## 规范与自动化

- [ ] `python3 scripts/kb_tools.py validate` 通过
- [ ] `.github/workflows/validate-knowledge.yml` 已存在
- [ ] Issue / PR 模板已存在

## GitHub 展示

- [ ] 已确定仓库名
- [ ] 已准备 description
- [ ] 已准备 topics
- [ ] 已准备首发版本号

## 发布动作

- [ ] 已 `git init`
- [ ] 已首个 commit
- [ ] 已 push 到 GitHub
- [ ] 已检查 Actions 是否运行
- [ ] 已创建 `v0.1.0` Release
