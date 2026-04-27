"""Knowledge Grid Tests"""

import pytest


class TestCellEngine:
    """Test cell_engine module"""

    def test_import(self):
        """Test that cell_engine can be imported"""
        from knowledge_grid import cell_engine
        assert cell_engine is not None


class TestFusionEngine:
    """Test fusion_engine module"""

    def test_import(self):
        """Test that fusion_engine can be imported"""
        from knowledge_grid import fusion_engine
        assert fusion_engine is not None


class TestMethodChecker:
    """Test method_checker module"""

    def test_import(self):
        """Test that method_checker can be imported"""
        from knowledge_grid import method_checker
        assert method_checker is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
