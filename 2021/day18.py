from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day18.py < sample.in
echo "=== real ===" ; py day18.py < day18.in
echo "=== sample ===" ; py day18.py < sample.in ; echo "=== real ===" ; py day18.py < day18.in
"""

A = read_input('/dev/stdin')

# f = open('/dev/stdin')
# parts = f.read().strip().split('\n\n')

N = len(A)

def geti(num, L):
    for x in L:
        num = num[x]
    return num

def seti(num, L, val):
    for x in L[:-1]:
        num = num[x]
    num[L[-1]] = val

def addi(num, L, val):
    for x in L[:-1]:
        num = num[x]
    num[L[-1]] += val

def explode_wrapper(num):
    explode_pair_loc = None
    explode_history_idx = None
    def explode(num, depth, stack, num_history):
        nonlocal explode_pair_loc
        nonlocal explode_history_idx
        depth += 1
        if isinstance(num, list):
            assert len(num) == 2
            if isinstance(num[0], int) and isinstance(num[1], int) and depth == 5 and explode_pair_loc is None:
                explode_pair_loc = stack
                explode_history_idx = len(num_history)
            explode(num[0], depth, stack + [0], num_history)
            explode(num[1], depth, stack + [1], num_history)
        else:
            num_history.append(stack)
    num_history = []
    explode(num, 0, [], num_history)
    if explode_pair_loc is not None:
        val_l, val_r = geti(num, explode_pair_loc)
        # the add step
        idx_left = explode_history_idx - 1
        idx_right = explode_history_idx + 2
        if idx_left >= 0:
            addi(num, num_history[idx_left], val_l)
        if idx_right < len(num_history):
            addi(num, num_history[idx_right], val_r)
        seti(num, explode_pair_loc, 0)
        return True
    return False

def split_wrapper(num):
    split_num_loc = None
    def split(num, stack):
        nonlocal split_num_loc
        if isinstance(num, list):
            assert len(num) == 2
            split(num[0], stack + [0])
            split(num[1], stack + [1])
        else:
            if num >= 10 and split_num_loc is None:
                split_num_loc = stack
    split(num, [])
    if split_num_loc is not None:
        val = geti(num, split_num_loc)
        val_l = val // 2
        val_r = val // 2
        if val % 2 == 1:
            val_r += 1
        seti(num, split_num_loc, [val_l, val_r])
        return True
    return False

def mag(num):
    if isinstance(num, list):
        return mag(num[0]) * 3 + mag(num[1]) * 2
    return num

acc = eval(A[0])

for i in range(1, N):
    b = eval(A[i])
    acc = [acc, b]
    while True:
        if explode_wrapper(acc):
            continue
        if split_wrapper(acc):
            continue
        break

print(acc)
print(mag(acc))

res = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        a = eval(A[i])
        b = eval(A[j])
        acc = [a, b]
        while True:
            if explode_wrapper(acc):
                continue
            if split_wrapper(acc):
                continue
            break
        res = max(res, mag(acc))
print(res)
