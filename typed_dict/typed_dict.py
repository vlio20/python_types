from typing import TypedDict


class User(TypedDict):
    name: str
    age: int


def get_user_data() -> User:
    return {'name': 'John', 'age': 30}


user = get_user_data()
print(user['name'])


u: User = {
    'name': 'John',
    'age': '30'
}
