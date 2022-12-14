from typing import Literal

KenVeLo = Literal['yes', 'no']


def yes_or_no(x: KenVeLo) -> None:
    if x == 'yes':
        print('ken')
    else:
        print('lo')


yes_or_no('yes')
yes_or_no('no')

yes_or_no('maybe')

