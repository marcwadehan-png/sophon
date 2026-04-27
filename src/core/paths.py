"""
src.core.paths - 路径配置
=========================

提供项目所有路径的便捷访问
"""

from pathlib import Path

# 项目根目录
PROJECT_ROOT = Path(__file__).parent.parent.parent

# 数据目录
DATA_DIR = PROJECT_ROOT / "data"
MEMORY_DIR = DATA_DIR / "memory"
LEARNING_DIR = DATA_DIR / "learning"
KNOWLEDGE_DIR = DATA_DIR / "knowledge"
SOLUTION_LEARNING_DIR = DATA_DIR / "solution_learning"
DAILY_MEMORY_DIR = DATA_DIR / "daily_memory"

# 创建必要目录
for _dir in [DATA_DIR, MEMORY_DIR, LEARNING_DIR, KNOWLEDGE_DIR]:
    _dir.mkdir(parents=True, exist_ok=True)
