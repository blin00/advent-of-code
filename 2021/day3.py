from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *

from util import *

"""
echo "=== sample ===" ; py day3.py < sample.in ; echo "=== real ===" ; py day3.py < day3.in
"""
A = read_input('/dev/stdin')
N = len(A)

M = len(A[0])

def go(arr, b):
    At = transpose(arr)
    ones = At[b].count('1')
    zeros = At[b].count('0')
    total = len(At[b])
    if ones >= zeros:
        res = '1'
        res2 = '0'
    else:
        res = '0'
        res2 = '1'

    B = []
    C = []
    for line in arr:
        if line[b] == res:
            B.append(line)
        if line[b] == res2:
            C.append(line)
    return B, C

arr1 = A
arr2 = A

for i in range(M):
    if len(arr1) > 1:
        arr1, _ = go(arr1, i)
    if len(arr2) > 1:
        _, arr2 = go(arr2, i)
    if len(arr1) == 1 and len(arr2) == 1:
        break

print(arr1, arr2, int(arr1[0], 2) * int(arr2[0], 2))
