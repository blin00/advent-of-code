from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day8.py < sample.in
echo "=== real ===" ; py day8.py < day8.in
echo "=== sample ===" ; py day8.py < sample.in ; echo "=== real ===" ; py day8.py < day8.in
"""
A = read_input('/dev/stdin')
N = len(A)

valid = [
    'abcefg',
    'cf', #
    'acdeg',
    'acdfg',
    'bcdf', #
    'abdfg',
    'abdefg',
    'acf', #
    'abcdefg', #
    'abcdfg',
]

def identify(ten):
    assert len(ten) == 10
    res = {}
    easy = {
        2: 1,
        3: 7,
        4: 4,
        7: 8,
    }
    for mapping in itertools.permutations(range(7)):
        good = True
        for thing in ten:
            canon = ''.join(sorted(thing))
            t = ''
            for ch in canon:
                x = mapping[ord(ch) - ord('a')]
                x = chr(x + ord('a'))
                t += x
            t = ''.join(sorted(t))
            if t not in valid:
                good = False
                break
        if good:
            return mapping
    assert False



res = 0
for line in A:
    a, b = line.split(' | ')
    for part in b.split(' '):
        if len(part) in (2, 3, 7, 4):
            res += 1
print(res)

res = 0

for line in A:
    a, b = line.split(' | ')
    a = a.split(' ')
    m = identify(a)

    tt = ''
    for digit in b.split(' '):
        t = ''
        canon = ''.join(sorted(digit))
        for ch in canon:
            x = m[ord(ch) - ord('a')]
            x = chr(x + ord('a'))
            t += x
        t = ''.join(sorted(t))
        d = valid.index(t)
        tt += str(d)

    tt = int(tt)
    res += tt
print(res)