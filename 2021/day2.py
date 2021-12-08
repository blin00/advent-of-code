from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *

from util import *

"""
echo "=== sample ===" ; py day2.py < sample.in ; echo "=== real ===" ; py day2.py < day2.in
"""
A = read_input('/dev/stdin')
N = len(A)

s = set()

horiz = 0
depth = 0
aim = 0

for line in A:
    cmd, x = line.split()
    x = int(x)
    if cmd == 'forward':
        horiz += x
        depth += aim * x
    elif cmd == 'down':
        aim += x
    elif cmd == 'up':
        aim -= x

print(horiz, depth, horiz * depth)
