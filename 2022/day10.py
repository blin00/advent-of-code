# from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; pypy3 day10.py < sample.in
echo "=== real ===" ; pypy3 day10.py < day10.in
echo "=== sample ===" ; pypy3 day10.py < sample.in ; echo "=== real ===" ; pypy3 day10.py < day10.in
"""

A = sys.stdin.read().strip().splitlines()

rows = 6
cols = 40

interesting = [20, 60, 100, 140, 180, 220]  # 1 index
idx = 0

cycles = 0
x = 1
res = 0

def do_work():
    global idx, cycles, x, res
    col = cycles % cols
    row = cycles // cols
    if x - 1 <= col <= x + 1:
        res2[row].append('#')
    else:
        res2[row].append('.')

    if idx < len(interesting) and (cycles + 1) == interesting[idx]:
        idx += 1
        res += x * (cycles + 1)
    cycles += 1

res2 = [[] for _ in range(rows)]

for line in A:
    if line == 'noop':
        do_work()
    else:
        a = int(line.split()[1])
        for i in range(2):
            do_work()
        x += a
print(res)
for row in res2:
    print(''.join(row))