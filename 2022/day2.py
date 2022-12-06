from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day2.py < sample.in
echo "=== real ===" ; py day2.py < day2.in
echo "=== sample ===" ; py day2.py < sample.in ; echo "=== real ===" ; py day2.py < day2.in
"""

A = sys.stdin.read().strip().splitlines()

m = {
    'R': 1,
    'P': 2,
    'S': 3,
}

m2 = {
    'X': 'R',
    'Y': 'P',
    'Z': 'S',
}


m3 = {
    'A': 'R',
    'B': 'P',
    'C': 'S',
}

def win(a, b):
    return (a == 'R' and b == 'S') or (a == 'S' and b == 'P') or (a == 'P' and b == 'R')

def get_out(opp, desired):
    if desired == 'Y':
        return opp
    elif desired == 'X':
        # lose
        t = {
            'R': 'S',
            'S': 'P',
            'P': 'R',
        }
        return t[opp]
    else:
        t = {
            'R': 'P',
            'S': 'R',
            'P': 'S',
        }
        return t[opp]

res = 0
for line in A:
    a, b = line.split()
    a = m3[a]
    b = get_out(a, b)
    res += m[b]
    if a == b:
        res += 3
    elif win(b, a):
        res += 6
print(res)
