"""src.utils - 工具函数兼容层"""

# 简单重试工具
class RetryError(Exception):
    """重试耗尽异常"""
    pass


class CircuitBreaker:
    """简单的熔断器实现"""
    def __init__(self, failure_threshold=5):
        self.failure_count = 0
        self.failure_threshold = failure_threshold
        self.is_open = False
    
    def record_failure(self):
        self.failure_count += 1
        if self.failure_count >= self.failure_threshold:
            self.is_open = True
    
    def record_success(self):
        self.failure_count = 0
        self.is_open = False


_circuit_breakers = {}


def get_circuit_breaker(name: str, threshold: int = 5) -> CircuitBreaker:
    """获取熔断器"""
    if name not in _circuit_breakers:
        _circuit_breakers[name] = CircuitBreaker(threshold)
    return _circuit_breakers[name]
