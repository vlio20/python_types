from typing import List

Vector = List[int]


def avg(items: Vector) -> float:
    return sum(items) / len(items)


a = avg([1, 2, 3])
