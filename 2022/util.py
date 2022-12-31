import re
from operator import add
from collections import defaultdict, Counter
import itertools
import math

import sys
sys.setrecursionlimit(int(1e7)) # segfault == you done messed up

# convention that positive y is down
# increment to clockwise/turn right, decrement to counterclockwise/turn left
# index with grid[y][x]

# this is x, y meta
DIRS = {
    0: (0, -1),
    1: (1, 0),
    2: (0, 1),
    3: (-1, 0),
}

DIRS_M = {
    'U': 0,
    'R': 1,
    'D': 2,
    'L': 3,
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3,
}

inf = INF = float('inf')

def sgn(x):
    if x == 0:
        return 0
    return x // abs(x)


def read_input(fname, t=lambda x: x, strip_lines=True, force_multi=False):
    with open(fname, 'r') as f:
        contents = f.read()
    if strip_lines:
        lines = contents.strip().split('\n')
    else:
        lines = contents.split('\n')
    if len(lines) == 1 and not force_multi:
        return t(lines[0])
    return list(map(t, lines))

def maybe_int(s):
    try:
        return int(s)
    except ValueError:
        return s

def keep_by_index(indices, arr):
    result = []
    for i in sorted(indices):
        if i < len(arr):
            result.append(arr[i])
    return result

def remove_by_index(indices, arr):
    result = []
    to_remove = set(indices)
    for i in range(len(arr)):
        if i not in to_remove:
            result.append(arr[i])
    return result

def min_by(f, arr):
    return min([(f(x), x) for x in arr])[1]

def max_by(f, arr):
    return max([(f(x), x) for x in arr])[1]

def parse_coord(line):
    return tuple(map(int, line.split(',')))

def metric_taxi(a, b):
    return sum(abs(a[i] - b[i]) for i in range(len(a)))

def move_by(d, p):
    if isinstance(d, int):
        d = DIRS[d]
    return tuple(map(add, d, p))

def parse_list(s):
    s = s.strip()
    return [int(x.strip('()[]<>')) for x in s.split(',')]

def fatal(*args, **kwargs):
    print(*args, **kwargs)
    exit()

def automata(grid, rule, iterations):
    R = len(grid)
    C = len(grid[0])
    def get_neighbors(i, j):
        # for ii, jj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
        for ii, jj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)):
            if 0 <= ii < R and 0 <= jj < C:
                yield ii, jj

    for _ in range(iterations):
        new_grid = [[None] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                neighbors = map(lambda x: grid[x[0]][x[1]], get_neighbors(i, j))
                new_grid[i][j] = rule(grid[i][j], Counter(neighbors))
        grid = new_grid
    return grid

def print_grid(grid, t=lambda x: x):
    for row in grid:
        print(''.join(map(t, row)))

def rule_gol(me, neighbors):
    if me == '*':
        return '*' if 2 <= neighbors['*'] <= 3 else '.'
    else:
        return '*' if neighbors['*'] == 3 else '.'

def prod(L):
    result = 1
    for x in L:
        result *= x
    return result

def reverse_dict(d):
    result = defaultdict(list)
    for k, v in d.items():
        for x in v:
            result[x].append(k)
    return result

builtin_map = map

def map(*args, **kwargs):
    return list(builtin_map(*args, **kwargs))

def do_ps(lst):
    prefix = [0]
    for x in lst:
        prefix.append(prefix[-1] + x)
    return prefix

def transpose(A):
    N = len(A)
    M = len(A[0])
    res = []
    for j in range(M):
        row = [A[i][j] for i in range(N)]
        res.append(row)
    return res

def crt(n, a):
    from functools import reduce
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * pow(p, -1, n_i) * p
    return sum % prod

def dump_dict_grid(d, t=lambda x: x):
    min_x = min(x for x, y in d.keys())
    max_x = max(x for x, y in d.keys())
    min_y = min(y for x, y in d.keys())
    max_y = max(y for x, y in d.keys())
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(t(d[(x, y)]), end='')
        print()

def ordch(ch: str) -> int:
    assert len(ch) == 1
    x = ord(ch)
    if x >= ord('a') and x <= ord('z'): return x - ord('a')
    if x >= ord('A') and x <= ord('Z'): return x - ord('A')
    raise Exception(f"{ch} is not alphabetic")

def add_interval(ss, L, R):
    # [L, R)
    assert L <= R
    if L == R:
        return None
    idx = ss.bisect_left((L, R))
    while idx < len(ss):
        ival = ss[idx]
        if ival[0] > R:
            break
        R = max(R, ival[1])
        ss.pop(idx)
    if idx > 0:
        idx -= 1
        ival = ss[idx]
        if ival[1] >= L:
            L = min(L, ival[0])
            R = max(R, ival[1])
            ss.pop(idx)
    res = (L, R)
    ss.add(res)
    return res

def remove_interval(ss, L, R):
    # [L, R)
    assert L <= R
    if L == R:
        return
    added = add_interval(ss, L, R)
    r2 = added[1]
    ss.remove(added)
    if added[0] != L:
        ss.add((added[0], L))
    if R != r2:
        ss.add((R, r2))

def pad_grid(grid, ch=' '):
    C = max(len(row) for row in grid)
    for i in range(len(grid)):
        if len(grid[i]) < C:
            grid[i] += ch * (C - len(grid[i]))
    return grid

def n4(i, j, mi=None, mj=None):
    """(x, y, C, R) or (i, j, R, C)"""
    for di, dj in ((-1, 0), (0, -1), (1, 0), (0, 1)):
        ii = i + di
        jj = j + dj
        if mi is not None:
            if ii < 0 or ii >= mi:
                continue
        if mj is not None:
            if jj < 0 or jj >= mj:
                continue
        yield ii, jj

def n8(i, j, mi=None, mj=None):
    """(x, y, C, R) or (i, j, R, C)"""
    for di in range(-1, 2):
        for dj in range(-1, 2):
            ii = i + di
            jj = j + dj
            if di == 0 and dj == 0:
                continue
            if mi is not None:
                if ii < 0 or ii >= mi:
                    continue
            if mj is not None:
                if jj < 0 or dj >= mj:
                    continue
            yield ii, jj

def n5(i, j, mi=None, mj=None):
    """(x, y, C, R) or (i, j, R, C)"""
    yield i, j
    yield from n4(i, j, mi, mj)

def n9(i, j, mi=None, mj=None):
    """(x, y, C, R) or (i, j, R, C)"""
    yield i, j
    yield from n8(i, j, mi, mj)

def n4d(pt):
    d = len(pt)
    for i in range(d):
        for sgn in (-1, 1):
            pt2 = list(pt)
            pt2[i] += sgn
            yield tuple(pt2)

def n8d(pt):
    d = len(pt)
    for choice in itertools.product((-1, 0, 1), repeat=d):
        if not(any(choice)):
            continue
        pt2 = list(pt)
        for i, sgn in enumerate(choice):
            pt2[i] += sgn
        yield tuple(pt2)

def ints(s, expected=None):
    res = map(int, re.findall(r'-?\d+', s))
    if expected is not None:
        assert len(res) == expected, f"for string {s}, expected {expected} ints, got {len(res)} ({res})"
    return res


def rline(x1, y1, x2, y2, unhinged=False):
    d = math.gcd(x2 - x1, y2 - y1) or 1
    assert d >= 1
    dy = (y2 - y1) // d
    dx = (x2 - x1) // d
    if not unhinged:
        assert dx in (-1, 0, 1) and dy in (-1, 0, 1), f"line ({x1}, {y1}) -> ({x2}, {y2}) is not horizontal, vertical, or 45 degree diagonal"
    while True:
        yield x1, y1
        if (x1, y1) == (x2, y2): break
        x1 += dx
        y1 += dy

def _util_test():
    assert list(rline(1, 1, 1, 1)) == [(1, 1)]
    assert list(rline(1, 1, 3, 1)) == [(1, 1), (2, 1), (3, 1)]
    assert list(rline(1, 3, 1, 1)) == [(1, 3), (1, 2), (1, 1)]
    assert list(rline(5, -3, 7, -5)) == [(5, -3), (6, -4), (7, -5)]
    assert list(rline(-6, 10, -10, 6)) == [(-6, 10), (-7, 9), (-8, 8), (-9, 7), (-10, 6)]
    assert list(rline(0, 0, 3, 4, True)) == [(0, 0), (3, 4)]
    assert list(rline(-106, -108, -100, -100, True)) == [(-106, -108), (-103, -104), (-100, -100)]
    assert list(rline(-106, 108, -100, 100, True)) == [(-106, 108), (-103, 104), (-100, 100)]
    assert list(rline(106, -108, 100, -100, True)) == [(106, -108), (103, -104), (100, -100)]
    assert list(rline(106, 108, 100, 100, True)) == [(106, 108), (103, 104), (100, 100)]

    assert ints('1 2 3 45 + 67 = -89,(90,91,92) asdf93asdf') == [1, 2, 3, 45, 67, -89, 90, 91, 92, 93]


if __name__ == '__main__':
    _util_test()
