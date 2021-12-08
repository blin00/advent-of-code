from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day4.py < sample.in
echo "=== real ===" ; py day4.py < day4.in
echo "=== sample ===" ; py day4.py < sample.in ; echo "=== real ===" ; py day4.py < day4.in
"""
A = read_input('/dev/stdin')
N = len(A)
R = N

order = map(int, A[0].split(','))

A = A[2:]

idx = 0

boards = []
marked = []

def gen_empty_mark():
    return [[False] * 5 for _ in range(5)]

def is_win(idx):
    mark = marked[idx]
    # row
    for row in mark:
        if all(row):
            return True
    # col
    for j in range(5):
        if all(mark[i][j] for i in range(5)):
            return True
    return False

while True:
    if idx >= len(A):
        break

    board = []
    for i in range(5):
        line = A[idx]
        board.append(map(maybe_int, line.split()))
        idx += 1
    idx += 1
    boards.append(board)
    marked.append(gen_empty_mark())

# print(boards)

N = len(boards)

def sum_unmarked(idx):
    res = 0
    for i in range(5):
        for j in range(5):
            if not marked[idx][i][j]:
                res += boards[idx][i][j]
    return res

already_won = [False] * N

for num in order:
    for idx in range(N):
        for i in range(5):
            for j in range(5):
                if boards[idx][i][j] == num:
                    marked[idx][i][j] = True
    
    for idx in range(N):
        if is_win(idx) and not already_won[idx]:
            already_won[idx] = True
            print(num * sum_unmarked(idx))
