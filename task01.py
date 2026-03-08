from typing import Callable, Dict


def caching_fibonaccі() -> Callable[[int], int]:
    cache: Dict[int, int] = {}

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result
        return result

    return fibonacci


if __name__ == "__main__":
    fib = caching_fibonaccі()
    print(fib(10))  # Output: 55
    print(fib(15))  # Output: 610
    print(fib(0))  # Output: 0
    print(fib(1))  # Output: 1
