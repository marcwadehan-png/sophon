"""src.core - 核心路径和工具"""

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

# 确保目录存在
for _dir in [DATA_DIR, MEMORY_DIR, LEARNING_DIR, KNOWLEDGE_DIR]:
    _dir.mkdir(parents=True, exist_ok=True)


# 超时守卫
class TimeoutLevel:
    """超时等级"""
    SHORT = 30
    MEDIUM = 60
    LONG = 120
    EXTENDED = 300


def _level_ordinal(level) -> int:
    """获取超时等级序号"""
    return getattr(TimeoutLevel, level.name, 0) if hasattr(level, 'name') else 0
