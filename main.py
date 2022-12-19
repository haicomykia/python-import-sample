import sys
from app.one import say
from app.three import substract
from app import sub

if __name__ == "__main__":
    sub.message()
    say.hello()
    print(f'1 + 3 = {say.plus(1, 3)}')

    print(f'1 + 2 - 3 = {substract.substract(1, 2, 3)}')

    print()

    print('print sys.path:')

    for path in sys.path:
        print(f'{path}')
