# Changelog

所有重要的项目变更都将记录在此文件中。

格式遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/) 规范。

## [6.2.0] - 2026-04-27

### Added
- **统一 Monorepo 结构**: 整合 knowledge-grid, reasoning-mind, memory-core 三大组件
- **21个知识格子**: A系列(智慧核心) + B系列(运营知识) + C系列(实战方法)
- **35个智慧引擎**: 儒家/道家/佛家/兵家/名家/阴阳家 + 西方哲学/心理学/复杂性科学
- **三层记忆架构**: 感官记忆、短期记忆、长期记忆
- **多范式推理引擎**: ReAct, ToT, CoT, Long-CoT, 阴阳推理, 叙事推理
- **Hebbian学习**: 神经网络权重复用机制
- **ROI追踪系统**: 记忆ROI分析与优化

### Components

#### Knowledge Grid
- `cell_engine.py`: 动态格子加载引擎
- `fusion_engine.py`: 跨格子知识融合
- `method_checker.py`: 五维方法论检查
- `cli.py`: 命令行交互界面

#### Reasoning Mind
- `react_engine.py`: ReAct 行动推理
- `tot_engine.py`: Tree-of-Thought 思维树
- `long_cot_engine.py`: 长思维链
- `yinyang_reasoning.py`: 阴阳对立统一推理
- `narrative_reasoning.py`: 叙事推理

#### Memory Core
- `neural_memory_system_v3.py`: 核心记忆引擎
- `hebbian_learning_engine.py`: Hebbian 学习
- `reinforcement_learning_v3.py`: 强化学习
- `transfer_learner.py`: 迁移学习

### Changed
- 统一版本号至 v6.2.0
- 优化模块间导入链
- 改进文档结构

### Fixed
- 修复格子元数据解析问题
- 优化推理引擎内存占用

## [6.1.0] - 2026-04-20

### Added
- 新增复杂性科学智慧引擎
- 新增阴阳家学派
- 新增 ROI 分析报告系统

### Changed
- 优化记忆编码效率

## [6.0.0] - 2026-04-15

### Added
- 初始开源版本
- 21个知识格子系统
- 35个智慧学派引擎
- 三层记忆架构

---

## 版本说明

- **MAJOR**: 重大架构变更
- **MINOR**: 新功能添加
- **PATCH**: Bug 修复和文档更新
