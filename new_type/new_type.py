from typing import List, NewType

Vector = NewType('Vector', List[int])


def avg(items: Vector) -> float:
    return sum(items) / len(items)


a = avg([1, 2, 3])

v = Vector([1, 2, 3])
avg(v)
