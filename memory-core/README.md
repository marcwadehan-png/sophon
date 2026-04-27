# Memory Core（记忆系统）

> 三层记忆架构 — 感官/短期/长期的神经记忆模拟

<p align="center">

[![Version](https://img.shields.io/badge/Version-6.2.0-orange.svg)](../CHANGELOG.md)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](../LICENSE)

</p>

## 特性

- **三层记忆模型**: 感官记忆 → 短期记忆 → 长期记忆
- **Hebbian学习**: "一起激活的神经元会连接" — 突触可塑性
- **ROI追踪**: 投资回报驱动的记忆优化
- **语义记忆**: 概念与关系的向量化存储
- **自适应策略**: 根据使用频率动态调整记忆权重

## 安装

```bash
pip install -e .
```

## 快速开始

```python
from memory_core import MemorySystem

memory = MemorySystem()
await memory.store("用户反馈", "提升加载速度")
result = await memory.recall("用户反馈")
print(result)
```

## 架构

```
Memory System
├── Sensory Memory     # 感官输入缓冲
├── Short-term Memory  # 工作记忆/注意力
└── Long-term Memory   # 永久知识存储
    ├── Episodic       # 情景记忆
    ├── Semantic       # 语义记忆
    └── Procedural     # 程序记忆
```

## 核心模块

| 模块 | 描述 |
|------|------|
| NeuralMemorySystem | 核心记忆引擎 |
| HebbianLearning | Hebbian学习算法 |
| ROITracker | 记忆ROI追踪 |
| SemanticMemory | 语义向量化 |
| AdaptiveStrategy | 自适应策略 |

## 学习策略

- **Hebbian学习**: 权重复用
- **强化学习**: 奖励驱动
- **迁移学习**: 知识复用
- **信息论检索**: 最大熵优化

## 依赖

- Python >= 3.10
- pyyaml
- loguru
- numpy

## 协议

MIT License