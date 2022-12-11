from typing import TypeGuard, TypedDict, Dict


class Person(TypedDict):
    name: str
    age: int


def is_person(val: Dict) -> TypeGuard[Person]:
    try:
        return isinstance(val['name'], str) \
               and isinstance(val['age'], int)
    except KeyError:
        return False


def print_age(val: Dict):
    if is_person(val):
        print(f"Age: {val['age']}")
        print(f"Address: {val['address']}")
    else:
        print('Not a person!')
