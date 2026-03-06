---
id: KNOW-AI-002
type: knowledge
domain: AI
tags:
  - ai-agent
  - metadata
  - knowledge-structure
status: active
source_type: synthesis
created: 2026-03-06
updated: 2026-03-06
---

# AI Agent知识结构

## 定义
AI Agent 知识结构是指一种让知识节点同时适合人阅读和机器解析的内容组织方式。

## 核心机制
通过稳定的 frontmatter 字段、明确的类型划分、标签和双链，Agent 可以在不理解整库上下文的前提下完成筛选、关联和生成。

## 关键要点
- 元数据是机器接口。
- `id` 解决唯一引用问题。
- `tags` 和 `domain` 解决筛选与聚类问题。

## 应用 / 启发
适用于 AI 辅助写作、知识检索、项目研究、自动摘要和后续脚本化处理。

## 示例
当 Agent 要找所有与知识结构相关的节点时，可以直接筛选 `type=knowledge` 且 `tags` 包含 `knowledge-structure` 或 `metadata` 的文件。

## 相关知识
- [[KNOW-AI-001-KnowledgeOS]]
- [[../设计/KNOW-DES-001-知识图谱结构]]
- [[../../03_Thinking/方法论/METHOD-信息到创造工作流]]

## 来源
基于 AI Agent 调用需求和本仓库元数据规范整理。
