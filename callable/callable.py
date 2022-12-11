from typing import Callable


def foo(x: str, y: int) -> bool:
    return True


def boo(x: int) -> bool:
    return True


def goo(f: Callable[[str, int], bool]) -> bool:
    return f('hello', 1)


goo(foo)
goo(boo)
