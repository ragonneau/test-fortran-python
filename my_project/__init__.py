__all__ = ['fib']
__version__ = '1.0.0'

def fib(n):
    from .fib2 import fib as fib2
    return fib2(n)

