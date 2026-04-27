# Reasoning Mind（推理智慧系统）

> 多范式推理引擎 — 融合古今中外的思维智慧

## 特性

- **10+种推理范式**: ReAct / Tree-of-Thought / CoT / Long-CoT / 阴阳推理等
- **35个智慧引擎**: 儒家/道家/佛家/兵法/经济学/复杂性科学等学派
- **深度咨询推理**: 企业战略/管理/营销等复杂问题求解
- **元认知框架**: 自我反思与策略调整

## 安装

```bash
pip install -e .
```

## 快速开始

```python
from reasoning_mind import ReasoningEngine

engine = ReasoningEngine()
result = await engine.think("如何提升团队创新能力", mode="cot")
print(result["reasoning"])
```

## 推理引擎

| 引擎 | 类型 | 描述 |
|------|------|------|
| ReAct | 行动推理 | Reasoning + Action 循环 |
| ToT | 思维树 | 树状探索与剪枝 |
| Long-CoT | 长思维链 | 深度思考与反思 |
| YinYang | 阴阳推理 | 对立统一分析 |
| Narrative | 叙事推理 | 故事化问题分析 |

## 智慧学派

- **东方智慧**: 儒家/道家/佛家/兵家/名家/阴阳家
- **西方智慧**: 哲学/心理学/复杂性科学
- **现代智慧**: 行为经济学/神经科学/复杂系统

## 目录结构

```
reasoning_mind/
├── reasoning/           # 推理引擎
│   ├── react_engine.py
│   ├── tot_engine.py
│   └── ...
├── engines/             # 35个智慧引擎
├── wisdom_encoding/     # 智慧编码
└── dispatcher/          # 智慧调度器
```

## 依赖

- Python >= 3.10
- pyyaml
- loguru

## 协议

MIT License
