from typing import Callable


def foo() -> bool:
    ...


def boo(x: int) -> bool:
    ...


def exec(f: Callable[[], bool]) -> bool:
    return f()


goo(foo)
goo(boo)
