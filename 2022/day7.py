from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day7.py < sample.in
echo "=== real ===" ; py day7.py < day7.in
echo "=== sample ===" ; py day7.py < sample.in ; echo "=== real ===" ; py day7.py < day7.in
"""

A = sys.stdin.read().strip().splitlines()

tree = {}

i = 0
cd = []
while i < len(A):
    line = A[i]
    assert line.startswith('$')
    args = line.split()
    if args[1] == 'cd':
        if args[2] == '/':
            cd = []
        elif args[2] == '..':
            cd.pop()
        else:
            cd.append(args[2])
        i += 1
    elif args[1] == 'ls':
        while True:
            i += 1
            if i >= len(A):
                break
            entry = A[i].split()
            if entry[0] == 'dir':
                pass
            elif entry[0] == '$':
                break
            else:
                size, fname = entry
                size = int(size)
                cur = tree
                for d in cd:
                    if d not in cur:
                        cur[d] = {}
                    cur = cur[d]
                cur[fname] = size

ans = 0

def get_size(dir):
    global ans
    me = 0
    for k, v in dir.items():
        if isinstance(v, int):
            me += v
        else:
            me += get_size(v)
    if me <= 100000:
        ans += me
    return me
used = get_size(tree)

print(ans)

total = 70000000
tgt_unused = 30000000
cur_unused = total - used
ans = 99e99

def get_size2(dir):
    global ans
    me = 0
    for k, v in dir.items():
        if isinstance(v, int):
            me += v
        else:
            me += get_size2(v)
    if me >= tgt_unused - cur_unused:
        ans = min(ans, me)
    return me
get_size2(tree)

print(ans)