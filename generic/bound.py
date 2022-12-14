from typing import TypeVar


class Animal:
    pass


class Cat(Animal):
    pass


class Dog(Animal):
    pass


class Human:
    pass


A = TypeVar('A', bound=Animal)


def make_noise(animal: A) -> None:
    pass


make_noise(Cat())  # 👍
make_noise(Dog())  # 👍
make_noise(Human())
