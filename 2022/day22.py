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
echo "=== sample ===" ; python3 day22.py < sample.in
echo "=== real ===" ; python3 day22.py < day22.in
echo "=== sample ===" ; python3 day22.py < sample.in ; echo "=== real ===" ; python3 day22.py < day22.in
"""

A = sys.stdin.read().rstrip('\n')
N = len(A)

grid, inst = A.split('\n\n')
grid = grid.splitlines()
grid = pad_grid(grid)

dir = DIRS_M['R']

def tokenize(inst):
    res = []
    cur = ''
    for c in inst:
        if c == 'L' or c == 'R':
            if cur:
                res.append(int(cur))
                cur = ''
            res.append(c)
        else:
            cur += c
    if cur:
        res.append(int(cur))
    return res

inst = tokenize(inst)

y = 0
x = grid[0].index('.')

R = len(grid)
C = len(grid[0])

def try_move_dir(x, y, d):
    dx, dy = DIRS[d]
    nx, ny = x, y
    while True:
        nx += dx
        ny += dy
        if nx < 0:
            nx = C - 1
        elif nx >= C:
            nx = 0
        if ny < 0:
            ny = R - 1
        elif ny >= R:
            ny = 0
        if grid[ny][nx] == '.':
            return nx, ny
        elif grid[ny][nx] == '#':
            return x, y
        else:
            assert grid[ny][nx] == ' '

DIM = 50

def check_wall(x, y, d, nx, ny, nd):
    assert 0 <= ny < R, (nx, ny)
    assert 0 <= nx < C, (nx, ny)
    if grid[ny][nx] == '#':
        return x, y, d
    else:
        assert grid[ny][nx] == '.'
        return nx, ny, nd

def try_move_dir_cube(x, y, d):
    dx, dy = DIRS[d]
    nx, ny = x + dx, y + dy
    if 0 <= nx < C and 0 <= ny < R:
        if grid[ny][nx] == '.':
            return nx, ny, d
        elif grid[ny][nx] == '#':
            return x, y, d
        else:
            assert grid[ny][nx] == ' '
            if 0 <= nx < DIM and 0 <= ny < DIM:
                # 1 -> 4
                assert d == DIRS_M['L']
                nd = DIRS_M['R']
                assert dy == 0
                ny = 2 * DIM + (DIM - y - 1)
                nx = 0
                return check_wall(x, y, d, nx, ny, nd)
            elif 0 <= nx < DIM and DIM <= ny < 2 * DIM:
                # 3 <-> 4
                if d == DIRS_M['L']:
                    nd = DIRS_M['D']
                    ny = 2 * DIM
                    nx = y - DIM
                    return check_wall(x, y, d, nx, ny, nd)
                elif d == DIRS_M['U']:
                    nd = DIRS_M['R']
                    ny = x + DIM
                    nx = DIM
                    return check_wall(x, y, d, nx, ny, nd)
                else:
                    assert False
            elif 2 * DIM <= nx < 3 * DIM and DIM <= ny < 2 * DIM:
                # 2 -> 3
                if d == DIRS_M['D']:
                    nd = DIRS_M['L']
                    nx = 2 * DIM - 1
                    ny = x - 2 * DIM + DIM
                    return check_wall(x, y, d, nx, ny, nd)
                else:
                    # 3 -> 2
                    assert d == DIRS_M['R']
                    nd = DIRS_M['U']
                    ny = DIM - 1
                    nx = y - DIM + 2 * DIM
                    return check_wall(x, y, d, nx, ny, nd)
            elif 3 * DIM <= nx < 4 * DIM:
                # 2 -> 5
                assert d == DIRS_M['R']
                nd = DIRS_M['L']
                nx = 2 * DIM - 1
                ny = 2 * DIM + (DIM - y - 1)
                return check_wall(x, y, d, nx, ny, nd)
            elif 2 * DIM <= nx < 3 * DIM and 2 * DIM <= ny < 3 * DIM:
                # 5 -> 2
                assert d == DIRS_M['R']
                nd = DIRS_M['L']
                nx = 3 * DIM - 1
                ny = (DIM - (y - 2 * DIM) - 1)
                return check_wall(x, y, d, nx, ny, nd)
            elif 1 * DIM <= nx < 2 * DIM and 3 * DIM <= ny < 4 * DIM:
                # 5 <-> 6
                if d == DIRS_M['D']:
                    nd = DIRS_M['L']
                    nx = DIM - 1
                    ny = x - DIM + 3 * DIM
                    return check_wall(x, y, d, nx, ny, nd)
                else:
                    assert d == DIRS_M['R']
                    nd = DIRS_M['U']
                    ny = 3 * DIM - 1
                    nx = y - 3 * DIM + DIM
                    return check_wall(x, y, d, nx, ny, nd)
            else:
                assert False
    else:
        if nx < 0:
            if 2 * DIM <= ny < 3 * DIM:
                # 4 -> 1
                assert d == DIRS_M['L']
                nd = DIRS_M['R']
                nx = DIM
                ny = (DIM - (y - 2 * DIM) - 1)
                return check_wall(x, y, d, nx, ny, nd)
            elif 3 * DIM <= ny < 4 * DIM:
                # 6 -> 1
                assert d == DIRS_M['L']
                nd = DIRS_M['D']
                ny = 0
                nx = y - 3 * DIM + DIM
                return check_wall(x, y, d, nx, ny, nd)
            else:
                assert False
        if ny < 0:
            if DIM <= nx < 2 * DIM:
                # 1 -> 6
                assert d == DIRS_M['U']
                nd = DIRS_M['R']
                nx = 0
                ny = 3 * DIM + x - DIM
                return check_wall(x, y, d, nx, ny, nd)
            if 2 * DIM <= nx < 3 * DIM:
                # 2 -> 6
                assert d == DIRS_M['U']
                nd = d
                nx = x - 2 * DIM
                ny = 4 * DIM - 1
                return check_wall(x, y, d, nx, ny, nd)
        if nx >= C:
            # 2 -> 5
            nd = DIRS_M['L']
            nx = 2 * DIM - 1
            ny = 2 * DIM + (DIM - y - 1)
            return check_wall(x, y, d, nx, ny, nd)

        if ny >= R:
            # 6 -> 2
            nd = d
            ny = 0
            nx = x + 2 * DIM
            return check_wall(x, y, d, nx, ny, nd)
            



for op in inst:
    if isinstance(op, str):
        if op == 'L':
            dir = (dir - 1) % 4
        else:
            assert op == 'R'
            dir = (dir + 1) % 4
    else:
        for i in range(op):
            x, y, dir = try_move_dir_cube(x, y, dir)
            assert 0 <= x < C
            assert 0 <= y < R
            assert grid[y][x] == '.'

row = y + 1
col = x + 1
facing = (dir - 1) % 4
# not 37396
print(row, col, facing, row * 1000 + col * 4 + facing)