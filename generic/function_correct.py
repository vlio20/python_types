from typing import TypeVar

T = TypeVar('T', int, float)


def sum_two(a: T, b: T) -> T:
    return a + b


sum_two('a', 'b')