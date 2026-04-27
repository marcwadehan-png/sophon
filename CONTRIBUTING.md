# Contributing to Sophon

感谢您对 Sophon 项目的关注！本项目欢迎所有形式的贡献，包括但不限于代码、文档、测试和反馈。

## 如何贡献

### 1. Fork & Clone

```bash
# Fork 仓库后克隆
git clone https://github.com/YOUR_USERNAME/sophon.git
cd sophon
```

### 2. 创建功能分支

```bash
git checkout -b feature/your-feature-name
# 或修复bug
git checkout -b fix/issue-description
```

### 3. 开发规范

#### 代码风格
- 遵循 PEP 8
- 使用 4 空格缩进
- 类名 `CamelCase`，函数名 `snake_case`
- 模块级 docstring 使用三重引号

#### 类型注解
- 建议为公共 API 添加类型注解
- 使用 `typing` 模块的完整类型

```python
from typing import List, Dict, Optional

def process_data(items: List[str]) -> Dict[str, int]:
    """处理数据并返回统计结果"""
    ...
```

#### 提交信息
遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

```
<type>(<scope>): <subject>

feat(knowledge-grid): add new cell fusion engine
fix(reasoning-mind): resolve memory leak in cache
docs(memory-core): update API documentation
```

类型标识：
- `feat`: 新功能
- `fix`: 错误修复
- `docs`: 文档更新
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建/工具变更

### 4. 测试

```bash
# 安装开发依赖
pip install -e ./knowledge-grid[dev]
pip install -e ./reasoning-mind[dev]
pip install -e ./memory-core[dev]

# 运行测试
pytest

# 带覆盖率
pytest --cov=knowledge_grid
```

### 5. 提交 Pull Request

1. 确保所有测试通过
2. 更新相关文档
3. 填写 PR 模板
4. 关联相关 Issue

## 项目结构

```
sophon/
├── knowledge-grid/     # 知识格子系统
├── reasoning-mind/     # 推理智慧系统
├── memory-core/        # 记忆系统
└── README.md
```

## 组件贡献指南

### Knowledge Grid
- 新格子文件: `A*.md`, `B*.md`, `C*.md`
- 遵循 INDEX.md 中的元数据格式
- 添加适当的 tags 和关联格子

### Reasoning Mind
- 新推理引擎: 继承 `BaseReasoningEngine`
- 新智慧学派: 遵循现有 YAML 配置格式
- 添加对应的单元测试

### Memory Core
- 新学习策略: 遵循 `learning_strategies/` 规范
- 添加 Hebbian/RL/Transfer Learning 测试

## 行为准则

- 尊重所有参与者
- 使用包容性语言
- 积极接受建设性反馈
- 关注社区长远利益

## 许可

贡献的代码将采用 MIT License。

## 问题反馈

- Bug 报告: [GitHub Issues](https://github.com/sophon-ai/sophon/issues)
- 功能建议: [GitHub Discussions](https://github.com/sophon-ai/sophon/discussions)
- 安全问题: 请私信维护者

---

再次感谢您的贡献！
