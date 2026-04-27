"""验证脚本 - 测试所有子项目导入"""
import sys
sys.path.insert(0, '.')

results = []

# Test knowledge-grid
try:
    from knowledge_grid import KnowledgeSystem
    results.append(("knowledge_grid", "OK"))
except Exception as e:
    results.append(("knowledge_grid", f"FAIL: {e}"))

# Test reasoning-mind
try:
    from reasoning_mind import DeepReasoningEngine
    results.append(("reasoning_mind", "OK"))
except Exception as e:
    results.append(("reasoning_mind", f"FAIL: {e}"))

# Test memory-core
try:
    from memory_core import NeuralMemorySystemV3
    results.append(("memory_core", "OK"))
except Exception as e:
    results.append(("memory_core", f"FAIL: {e}"))

# Test src compatibility layer
try:
    from src.core.paths import DATA_DIR
    results.append(("src.core.paths", "OK"))
except Exception as e:
    results.append(("src.core.paths", f"FAIL: {e}"))

# Print results
print("=" * 50)
print("Import Verification Results")
print("=" * 50)
for name, status in results:
    print(f"{name:20} {status}")
print("=" * 50)

# Summary
failed = [r for r in results if not r[1].startswith("OK")]
if failed:
    print(f"\n❌ {len(failed)} module(s) failed")
    sys.exit(1)
else:
    print(f"\n✅ All {len(results)} modules imported successfully")
