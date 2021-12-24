from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day23.py < sample.in
echo "=== real ===" ; py day23.py < day23.in
echo "=== sample ===" ; py day23.py < sample.in ; echo "=== real ===" ; py day23.py < day23.in
"""


from heapq import *


A = read_input('/dev/stdin', strip_lines=False)

N = len(A)

energy = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}


free_cells = []
res = 0

# ..x.x.x.x..
#   . . . .
#   . . . .


Q = []

R = len(A)
C = len(A[0])

for i in range(R):
    if len(A[i]) < C:
        A[i] += ' ' * (C - len(A[i]))

for i in range(2):
    for j in range(C):
        if A[i][j] != '#':
            if i == 1 and j in (3, 5, 7, 9):
                continue
            free_cells.append((i, j))
dest_cells = defaultdict(list)

m1 = {
    'A': 3,
    'B': 5,
    'C': 7,
    'D': 9,
}

thing_to_dest_col = {
    0: 3,
    1: 5,
    2: 7,
    3: 9,
}

dest_col_to_thing = {v: k for k, v in thing_to_dest_col.items()}

energy2 = [
    1,
    10,
    100,
    1000,
]

state = defaultdict(list)

for i in range(2, R):
    for j in range(C):
        if A[i][j] != '#' and A[i][j] != ' ':
            thing = A[i][j]
            state[thing].append((i, j))
            dest_cells[j].append((i, j))
DIV = len(dest_cells[3])
NUM_THINGS = DIV * 4

def solved(state):
    good = True
    for i in range(4):
        idx = i * DIV
        for j in range(DIV):
            a = state[i * DIV + j]
            if a[0] >= 2 and a[1] == thing_to_dest_col[i]:
                pass
            else:
                good = False
                break
    return good

def get_neighbors(i, j):
    for ii, jj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
        if 0 <= ii < R and 0 <= jj < C and A[ii][jj] != '#':
            yield ii, jj


initial = []
for x in 'ABCD':
    initial += state[x]
assert len(initial) == NUM_THINGS


def bfs(src, dst, state):
    Q = []
    visited = set()
    Q.append((0, src))
    visited.add(src)
    for d, u in Q:
        if u == dst:
            return d
        for ii, jj in get_neighbors(*u):
            if (ii, jj) in state:
                continue
            if (ii, jj) in visited:
                continue
            visited.add((ii, jj))
            Q.append((d + 1, (ii, jj)))
    return INF

assert len(free_cells) == 7

heappush(Q, (0, tuple(initial)))
dist = defaultdict(lambda: INF)

def dump_state(state):
    for i in range(R):
        r = []
        for j in range(C):
            try:
                idx = state.index((i, j))
                r.append(str(idx))
            except ValueError:
                if A[i][j] >= 'A' and A[i][j] <= 'D':
                    r.append('.')
                else:
                    r.append(A[i][j])
        print(''.join(r))

import random
dist[tuple(initial)] = 0
dump_state(tuple(initial))

def get_contents(state, coord):
    if coord in state:
        return state.index(coord)
    return None

def get_valid_room_dest(state):
    for col in dest_col_to_thing.keys():
        order = dest_cells[col][::-1]
        for cell in order:
            if cell not in state:
                yield cell
                break

def cell_is_done(state, cell):
    if cell[0] < 2:
        return False
    idx = state.index(cell)
    thing = idx // DIV
    if cell[1] != thing_to_dest_col[thing]:
        return False
    for c in dest_cells[cell[1]]:
        if c[0] <= cell[0]:
            continue
        fuck = get_contents(state, c)
        if fuck is None:
            return False
        if fuck // DIV != thing:
            return False
    return True


while Q:
    d, state = heappop(Q)

    if solved(state):
        print('ans:', d)
        break
    if d > dist[state]:
        continue
    valid_room_dest = list(get_valid_room_dest(state))
    valid_room_dest_by_thing = [None] * 4
    for a, b in valid_room_dest:
        valid_room_dest_by_thing[dest_col_to_thing[b]] = a, b
    for i in range(NUM_THINGS):
        # try moving thing i
        if cell_is_done(state, state[i]):
            continue
        thing = i // DIV
        dest_col = thing_to_dest_col[thing]
        if state[i][0] == 1:
            # free
            valid_targets = []
            for a, b in valid_room_dest:
                if b == dest_col:
                    valid_targets = [(a, b)]
        else:
            # in a room
            valid_targets = itertools.chain(free_cells, valid_room_dest)


        # valid_targets = itertools.chain(free_cells, valid_room_dest)

        for dst in valid_targets:
            new_state = tuple(dst if j == i else state[j] for j in range(NUM_THINGS))
            if dst in state:
                continue
            if dst[0] >= 2:
                if dst[1] != dest_col:
                    # wrong room
                    continue
                if not cell_is_done(new_state, dst):
                    continue

            if state[i][0] == 1 and dst[0] == 1:
                # shuffling
                continue
            delta = bfs(state[i], dst, state)
            if delta >= INF:
                continue
            new_d = d + energy2[thing] * delta
            if new_d < dist[new_state]:
                dist[new_state] = new_d
                heappush(Q, (new_d, new_state))
    