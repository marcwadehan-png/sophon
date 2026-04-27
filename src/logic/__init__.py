"""src.logic - 逻辑推理兼容层"""

from typing import List, Dict, Any


class FallacyDetector:
    """逻辑谬误检测器（占位实现）"""
    
    FALLACIES = [
        "ad_hominem",      # 人身攻击
        "straw_man",       # 稻草人
        "appeal_to_authority",  # 权威谬误
        "false_dilemma",   # 虚假两难
        "slippery_slope",  # 滑坡谬误
        "circular_reasoning",  # 循环论证
        "hasty_generalization",  # 草率概括
    ]
    
    def detect(self, text: str) -> List[Dict[str, Any]]:
        """检测文本中的逻辑谬误"""
        results = []
        text_lower = text.lower()
        
        for fallacy in self.FALLACIES:
            if fallacy.replace("_", " ") in text_lower:
                results.append({
                    "type": fallacy,
                    "confidence": 0.5,
                    "suggestion": f"注意可能的 {fallacy} 谬误"
                })
        
        return results
