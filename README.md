# Sophon（所门）

> AI 认知架构三件套 — 知识格子 / 推理引擎 / 记忆系统

**一句话**: 受《三体》中的智子（Sophon）启发，构建像大脑一样思考的 AI 认知架构 — 21个知识格子存储领域智慧，35个智慧学派驱动多范式推理，三层神经记忆系统实现自主学习和知识进化。

<p align="center">

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-6.2.0-orange.svg)](CHANGELOG.md)
[![GitHub Stars](https://img.shields.io/github/stars/sophon-ai/sophon?style=social)](https://github.com/sophon-ai/sophon/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/sophon-ai/sophon?style=social)](https://github.com/sophon-ai/sophon/network/members)
[![Code Style](https://img.shields.io/badge/Code%20Style-black-000000.svg)](https://github.com/psf/black)
[![Imports](https://img.shields.io/badge/imports-isort-yellow.svg)](https://github.com/PyCQA/isort)

</p>

<p align="center">
  <b>GitHub Topics:</b>
  <code>ai</code> <code>cognitive-architecture</code> <code>knowledge-graph</code> <code>reasoning-engine</code> <code>memory-system</code> <code>neural-network</code> <code>wisdom-engine</code> <code>agent-framework</code> <code>multi-paradigm-reasoning</code> <code>hebbian-learning</code>
</p>

## 组件

| 项目 | 描述 | 仓库 |
|------|------|------|
| [knowledge-grid](knowledge-grid/) | 21个动态知识格子引擎 | `sophon-ai/knowledge-grid` |
| [reasoning-mind](reasoning-mind/) | 多范式推理 + 35个智慧引擎 | `sophon-ai/reasoning-mind` |
| [memory-core](memory-core/) | 三层神经记忆系统 | `sophon-ai/memory-core` |

## 架构

```
┌─────────────────────────────────────────────────┐
│                  Sophon Agent                    │
├─────────────────────────────────────────────────┤
│  ┌───────────┐  ┌────────────┐  ┌───────────┐  │
│  │Knowledge  │  │ Reasoning  │  │  Memory   │  │
│  │  Grid     │  │   Mind     │  │   Core    │  │
│  │ (藏书阁)  │  │ (推理智慧)  │  │ (记忆系统) │  │
│  └─────┬─────┘  └──────┬─────┘  └─────┬─────┘  │
│        │               │               │        │
│        └───────────────┼───────────────┘        │
│                        ▼                        │
│              [ Unified Brain ]                  │
└─────────────────────────────────────────────────┘
```

## 安装

```bash
# 安装全部组件
pip install -e ./knowledge-grid
pip install -e ./reasoning-mind
pip install -e ./memory-core
```

## 快速开始

```python
from knowledge_grid import get_knowledge_engine
from reasoning_mind import ReasoningEngine
from memory_core import MemorySystem

# 初始化
grid = get_knowledge_engine()
reasoning = ReasoningEngine()
memory = MemorySystem()

# 协同工作
query = "如何提升用户留存"
knowledge = grid.search(query)
reasoning_result = await reasoning.think(knowledge, mode="cot")
await memory.store(query, reasoning_result)
```

## 组件详解

### Knowledge Grid

21个知识格子覆盖：
- **A系列(智慧核心)**: A1逻辑判断 ~ A8反思进化
- **B系列(运营知识)**: B1用户增长 ~ B9策略运营
- **C系列(实战方法)**: C1电商 ~ C4广告投放

### Reasoning Mind

10+推理范式：
- ReAct / ToT / CoT / Long-CoT
- 阴阳推理 / 叙事推理 / 逆向推理

35个智慧引擎：
- 东方: 儒/道/佛/兵/名/阴阳
- 西方: 哲学/心理学/复杂性科学
- 现代: 行为经济学/神经科学

### Memory Core

三层记忆架构：
- **感官记忆**: 输入缓冲
- **短期记忆**: 工作记忆
- **长期记忆**: 永久存储

学习机制：
- Hebbian学习
- 强化学习
- 迁移学习

## 项目结构

```
sophon/
├── knowledge-grid/     # 知识格子系统
│   ├── cells/          # 21个格子Markdown
│   ├── engine.py       # 核心引擎
│   └── ...
├── reasoning-mind/     # 推理智慧系统
│   ├── reasoning/      # 推理引擎
│   ├── engines/        # 35个智慧引擎
│   └── ...
├── memory-core/        # 记忆系统
│   ├── neural_memory/  # 核心模块
│   └── ...
└── README.md
```

## 依赖

- Python >= 3.10
- pyyaml
- loguru
- numpy

## 协议

MIT License - 详见各组件目录

## 联系

- Issue: https://github.com/sophon-ai/sophon/issues
- Email: marcwadehan@gmail.com

---

## 亮点

| 能力 | 描述 |
|------|------|
| 🧠 知识格子 | 21个领域知识节点，动态关联、跨域融合、举一反三 |
| 🌳 多范式推理 | ReAct/ToT/CoT/阴阳推理/叙事推理等 10+ 推理范式 |
| 💡 35个智慧引擎 | 儒/道/佛/兵/名/阴阳家 + 哲学/心理学/复杂性科学/经济学 |
| 🧬 三层记忆 | 感官→短期→长期，支持 Hebbian/强化/迁移三种学习机制 |
| 🔗 自主学习 | Hebbian 突触可塑性 + ROI 驱动的记忆优化 + 知识衰减与进化 |
| 📦 Monorepo | 三个子包独立可用，也可组合为完整认知架构 |

## GitHub 仓库描述
