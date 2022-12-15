# from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; python3 day15.py < sample.in
echo "=== real ===" ; python3 day15.py < day15.in
echo "=== sample ===" ; python3 day15.py < sample.in ; echo "=== real ===" ; python3 day15.py < day15.in
"""

A = sys.stdin.read().strip().splitlines()
# A = sys.stdin.read().strip().split('\n\n')

N = len(A)

sensors = []

for line in A:
    l, r = line.split(': ')
    ll, lr = l.split(', ')
    sx = int(ll.split(' ')[-1].split('=')[1])
    sy = int(lr.split('=')[1])
    rl, rr = r.split(', ')
    bx = int(rl.split(' ')[-1].split('=')[1])
    by = int(rr.split('=')[1])
    sensors.append((sx, sy, bx, by))

def solve(y_target):
    beacons = set()
    m = {}
    for sx, sy, bx, by in sensors:
        d = abs(sx - bx) + abs(sy - by)
        m[(sx, sy)] = d
        beacons.add((bx, by))
    res = 0

    for x in range(int(-5e6), int(5e6)):
        good = True
        for sx, sy, _, _ in sensors:
            my_dist = abs(sx - x) + abs(sy - y_target)
            if my_dist <= m[(sx, sy)]:
                good = False
                break
        if not good:
            if (x, y_target) not in beacons:
                res += 1
    return res

from z3 import *

def solve2(bound):
    beacons = set()
    m = {}
    for sx, sy, bx, by in sensors:
        d = abs(sx - bx) + abs(sy - by)
        m[(sx, sy)] = d
        beacons.add((bx, by))
    
    s = Solver()
    x, y = Int('x'), Int('y')
    s.add(x >= 0)
    s.add(x <= bound)
    s.add(y >= 0)
    s.add(y <= bound)
    for sx, sy, bx, by in sensors:
        my_dist = Abs(sx - x) + Abs(sy - y)
        s.add(my_dist > m[(sx, sy)])
        s.add(And(x != bx, y != by))

    
    assert s.check() == sat
    m = s.model()
    return m[x].as_long(), m[y].as_long()

# print(solve(2000000))

x, y = solve2(4000000)
print(x, y, x * 4000000 + y)