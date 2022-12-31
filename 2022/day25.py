try:
    from sortedcontainers import *
    from math import gcd, lcm
except ImportError:
    pass
from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; pypy3 day25.py < sample.in
echo "=== real ===" ; pypy3 day25.py < day25.in
echo "=== sample ===" ; pypy3 day25.py < sample.in ; echo "=== real ===" ; pypy3 day25.py < day25.in
"""

A = sys.stdin.read().rstrip('\n').splitlines()
N = len(A)

val = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2,
}

sum = 0

for line in A:
    acc = 0
    for i, c in enumerate(reversed(line)):
        p = i
        acc += val[c] * 5 ** p

    sum += acc


print(sum)


val_rev = {
    2: '2',
    1: '1',
    0: '0',
    -1: '-',
    -2: '=',
}

res = ''

while True:
    if not sum:
        break
    digit = sum % 5
    if digit == 4:
        digit = -1
    if digit == 3:
        digit = -2
    res += val_rev[digit]
    sum -= digit
    sum //= 5

print(''.join(res[::-1]))

