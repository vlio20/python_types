from typing import TypeVar, Generic

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()


intStack = Stack[int]()
strStack = Stack[str]()