"""Reasoning Mind Tests"""

import pytest


class TestReActEngine:
    """Test ReAct reasoning engine"""

    def test_import(self):
        """Test that react engine can be imported"""
        from reasoning_mind import _react_engine
        assert _react_engine is not None


class TestToTEngine:
    """Test Tree-of-Thought engine"""

    def test_import(self):
        """Test that tot engine can be imported"""
        from reasoning_mind import _tot_engine
        assert _tot_engine is not None


class TestYinYangReasoning:
    """Test YinYang reasoning"""

    def test_import(self):
        """Test that yinyang reasoning can be imported"""
        from reasoning_mind import _yinyang_reasoning
        assert _yinyang_reasoning is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
