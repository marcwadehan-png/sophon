"""
Sophon src 兼容层
================

本模块提供向后兼容的导入路径，让内部 `from src.xxx` 的导入
能够正确工作。

使用方式：
    from src.core.paths import ...
    from src.neural_memory import ...
    from src.intelligence import ...
"""

import os
import sys
from pathlib import Path

# 获取项目根目录 (src 的父目录)
_PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(_PROJECT_ROOT))

# 导入同名子模块 (实际指向 memory-core 等)
from memory_core import *
from reasoning_mind import *
from knowledge_grid import *
