"""Memory Core Tests"""

import pytest


class TestNeuralMemory:
    """Test neural memory system"""

    def test_import(self):
        """Test that neural memory can be imported"""
        from memory_core import neural_memory_system_v3
        assert neural_memory_system_v3 is not None


class TestHebbianLearning:
    """Test Hebbian learning"""

    def test_import(self):
        """Test that hebbian learning can be imported"""
        from memory_core import hebbian_learning_engine
        assert hebbian_learning_engine is not None


class TestReinforcementLearning:
    """Test reinforcement learning"""

    def test_import(self):
        """Test that RL can be imported"""
        from memory_core import reinforcement_learning_v3
        assert reinforcement_learning_v3 is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
