from typing import overload


@overload
def hello(x: str) -> int:
    ...


@overload
def hello(x: int) -> str:
    ...


def hello(x: str | int) -> str | int:
    # implementation
    if isinstance(x, str):
        return 1
    else:
        return 'a'


x = hello('asdsa')
y = hello(1)



