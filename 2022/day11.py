# from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; pypy3 day11.py < sample.in
echo "=== real ===" ; pypy3 day11.py < day11.in
echo "=== sample ===" ; pypy3 day11.py < sample.in ; echo "=== real ===" ; pypy3 day11.py < day11.in
"""

A = sys.stdin.read().strip().split('\n\n')

N = len(A)


def gen_add(a):
    return lambda x: x + a

def gen_mul(a):
    return lambda x: x * a

monkeys = []
items = []
inspected = [0] * N

all_div = 1

for block in A:
    lines = block.splitlines()
    item = map(int, lines[1].split(': ')[1].split(', '))
    op = lines[2].split(': ')[1]
    if 'old * old' in op:
        func = lambda x: x * x
    elif 'old +' in op:
        val = op.split('+')[-1]
        func = gen_add(int(val))
    elif 'old *' in op:
        val = op.split('*')[-1]
        func = gen_mul(int(val))
    else:
        assert False
    div = int(lines[3].split()[-1])
    t = int(lines[4].split()[-1])
    f = int(lines[5].split()[-1])
    all_div *= div
    monkeys.append((func, div, t, f))
    items.append(item)

for ri in range(10000):
    for mi in range(N):
        monkey = monkeys[mi]
        for item in items[mi]:
            item = monkey[0](item)
            # item //= 3
            if item % monkey[1] == 0:
                target = monkey[2]
            else:
                target = monkey[3]
            assert target != mi
            items[target].append(item % all_div)
            inspected[mi] += 1
        items[mi] = []

print(inspected)

inspected.sort()
inspected = inspected[::-1]
print(inspected[0] * inspected[1])