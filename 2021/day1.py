from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *

from util import *

"""
echo "=== sample ===" ; py day1.py < sample.in ; echo "=== real ===" ; py day1.py < day1.in
"""

L = read_input('/dev/stdin', t=int)
N = len(L)

s = set()

res = 0
for i in range(1, N):
    if L[i] > L[i-1]:
        res += 1
print(res)

res = 0

for i in range(1, N):
    a = sum(L[i:i+3])
    b = sum(L[i - 1:i+2])
    if a > b:
        res += 1
print(res)