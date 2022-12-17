from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from math import gcd, lcm
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; pypy3 day17.py < sample.in
echo "=== real ===" ; pypy3 day17.py < day17.in
echo "=== sample ===" ; pypy3 day17.py < sample.in ; echo "=== real ===" ; pypy3 day17.py < day17.in
"""

A = sys.stdin.read().strip()
N = len(A)

BLOCKS ='''
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##'''.strip().split('\n\n')

WIDTH = 7

# alternate push, fall

grid = set()
# (x, y), y increases with height

ITER = 1000000000000
time = 0
next_block = 0


def parse_block(b):
    b = b.splitlines()
    height = len(b)
    width = len(b[0])
    points = []

    for i in range(height):
        for j in range(width):
            if b[i][j] == '#':
                points.append((j, height - i - 1))
    return points

BP = [parse_block(b) for b in BLOCKS]

top_y = -1

def add(block, dx, dy):
    return [(dx + x, dy + y) for (x, y) in block]


def collide(b):
    for x, y in b:
        if (x, y) in grid:
            return True
        if x < 0 or x >= WIDTH:
            return True
        if y < 0:
            return True
    return False

def keep_top(n):
    to_yeet = []
    for (x, y) in grid:
        if y < top_y - n:
            to_yeet.append((x, y))
    for (x, y) in to_yeet:
        grid.remove((x, y))

def serialize_state():
    return tuple(sorted([(x, y - top_y) for (x, y) in grid]))

oct = 0
dp = {}
offset = 0
while True:
    keep_top(50)

    if next_block == 0:
        state = serialize_state()
        key = (time, state)
        if key in dp:
            # print('got repeated state:')
            # print('time:', time)
            # print('oct:', oct)
            (prev_oct, prev_top_y) = dp[key]
            # print('prev_oct:', prev_oct)
            # print('prev_top_y:', prev_top_y)
            # print('top_y:', top_y)
            # thx copilot
            period = oct - prev_oct
            y_diff = top_y - prev_top_y
            offset += y_diff * ((ITER - oct) // period)
            oct += (ITER - oct) // period * period
        else:
            dp[key] = (oct, top_y)
    assert oct <= ITER
    if oct == ITER:
        break

    b = BP[next_block]
    b = add(b, 2, top_y + 4)
    while True:
        # jet of gas
        dir = A[time]
        time = (time + 1) % len(A)
        if dir == '>':
            dx = 1
        else:
            dx = -1
        newb = add(b, dx, 0)
        if not collide(newb):
            b = newb
        # fall down
        newb = add(b, 0, -1)
        if not collide(newb):
            b = newb
        else:
            break
    for x, y in b:
        top_y = max(top_y, y)
        grid.add((x, y))
    next_block = (next_block + 1) % len(BP)
    oct += 1
    if oct == ITER:
        break

print(top_y + offset + 1)
