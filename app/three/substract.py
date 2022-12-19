import sys
from one import say

print(say.plus(1, 2) - 3)

print('---')

for path in sys.path:
    print(f'{path}')
