from typing import Literal

kenVeLof = Literal['yes', 'no']


def yes_or_no(x: kenVeLof) -> None:
    if x == 'yes':
        print('yes')
    else:
        print('no')


yes_or_no('yes')
yes_or_no('no')

yes_or_no('maybe')

