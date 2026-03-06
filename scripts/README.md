# scripts

这里放知识库的辅助脚本。首轮提供一个零依赖 CLI：

`python3 scripts/kb_tools.py`

## 命令

### 查询下一个知识 ID

```bash
python3 scripts/kb_tools.py next-id AI
python3 scripts/kb_tools.py next-id BIZ
```

输出示例：

```text
KNOW-AI-003
```

### 校验知识层规范

```bash
python3 scripts/kb_tools.py validate
```

会检查：

- 文件名是否符合 `KNOW-领域代码-编号-中文主题.md`
- `id` 是否重复
- `id / domain / type` 是否与文件名和目录一致
- 必填 frontmatter 是否缺失
- `status / source_type / created / updated / tags` 是否符合规范
