from typing import TypeVar

T = TypeVar('T', int, float)


def sum_two(a: T, b: T) -> T:
    return a + b


sum_two(1, 2)  # 3
sum_two(1.0, 2.0)  # 3.0
