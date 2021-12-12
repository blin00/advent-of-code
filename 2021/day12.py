from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day12.py < sample.in
echo "=== real ===" ; py day12.py < day12.in
echo "=== sample ===" ; py day12.py < sample.in ; echo "=== real ===" ; py day12.py < day12.in
"""

A = read_input('/dev/stdin')
N = len(A)

res = 0

def is_small(s):
    return all(x.islower() for x in s)

graph = defaultdict(list)

for line in A:
    u, v = line.split('-')
    graph[u].append(v)
    graph[v].append(u)

stack = []
ctr = Counter()
ree = False

def dfs(root):
    global res, ree
    if root == 'start' and ctr['start'] >= 1:
        return
    if root == 'end':
        # print(','.join(stack))
        res += 1
        return
    if is_small(root) and root in stack:
        # maybe visit again
        if not ree:
            ree = True
            stack.append(root)
            ctr[root] += 1
            for v in graph[root]:
                dfs(v)
            ctr[root] -= 1
            stack.pop()
            ree = False
        return
    stack.append(root)
    ctr[root] += 1
    for v in graph[root]:
        dfs(v)
    ctr[root] -= 1
    stack.pop()

dfs('start')
print(res)
