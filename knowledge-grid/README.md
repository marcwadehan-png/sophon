# Knowledge Grid（知识格子系统）

> 动态知识格子引擎 — 像大脑一样自适应连接知识节点

<p align="center">

[![Version](https://img.shields.io/badge/Version-6.2.0-orange.svg)](../CHANGELOG.md)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](../LICENSE)

</p>

## 特性

- **21个知识格子**: A系列(智慧核心) + B系列(运营知识) + C系列(实战方法)
- **动态加载**: Markdown格式的知识格子，运行时动态解析
- **知识融合**: 跨格子知识融合，举一反三
- **方法论检查**: 五维诊断框架
- **神经网络集成**: 与神经网络布局系统无缝对接

## 安装

```bash
pip install -e .
```

## 快速开始

```python
from knowledge_grid import get_knowledge_engine

engine = get_knowledge_engine()
result = engine.query("如何提升用户增长")
print(result["answer"])
```

## 格子索引

| 分类 | 格子 | 描述 |
|------|------|------|
| A系列 | A1-A8 | 智慧核心(逻辑/决策/反思等) |
| B系列 | B1-B9 | 运营知识(用户增长/直播/私域等) |
| C系列 | C1-C4 | 实战方法(电商/数据/内容/投放) |

## CLI工具

```bash
python -m knowledge_grid.cli
```

## 目录结构

```
knowledge_grid/
├── A1_逻辑判断.md      # A系列: 智慧核心 (A1-A8)
├── A2_智慧模块.md
├── A3_论证审核.md
├── A4_判断决策.md
├── A5_五层架构.md
├── A6_核心执行链.md
├── A7_感知记忆.md
├── A8_反思进化.md
├── B1_互联网用户增长.md # B系列: 运营知识 (B1-B9)
├── B2_直播运营.md
├── B3_私域运营.md
├── B4_活动策划.md
├── B5_会员运营.md
├── B6_广告策划.md
├── B7_地产策划.md
├── B8_招商策划.md
├── B9_策略运营.md
├── C1_电商运营.md      # C系列: 实战方法 (C1-C4)
├── C2_数据运营.md
├── C3_内容营销.md
├── C4_广告投放.md
├── cell_engine.py      # 核心引擎
├── fusion_engine.py    # 知识融合器
├── method_checker.py   # 方法论检查器
├── cli.py              # 命令行工具
└── README.md
```

## 依赖

- Python >= 3.10
- pyyaml

## 协议

MIT License
