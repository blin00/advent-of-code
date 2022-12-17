# from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; pypy3 day16.py < sample.in
echo "=== real ===" ; pypy3 day16.py < day16.in
echo "=== sample ===" ; pypy3 day16.py < sample.in ; echo "=== real ===" ; pypy3 day16.py < day16.in
"""

A = sys.stdin.read().strip().splitlines()
# A = sys.stdin.read().strip().split('\n\n')

graph = {}

m = {}
m2 = {}

flow = {}

target = -1

for line in A:
    tokens = line.split(' ')
    valve = tokens[1]
    neighbors = ''.join(tokens[9:]).split(',')
    graph[valve] = neighbors
    flow[valve] = ints(line, 1)[0]
    idx = len(m)
    m[valve] = idx
    m2[idx] = valve

    if valve == 'AA':
        target = idx
ans = 0

@cache
def dp(time, idx, mask):
    global ans
    cur_flow = 0
    for i, e in enumerate(mask):
        if e:
            cur_flow += flow[m2[i]]
    if time == 30:
        return 0
    else:
        # turn it on
        nm = list(mask)
        r1 = 0
        if not mask[idx] and flow[m2[idx]] > 0:
            nm[idx] = True
            r1 = cur_flow + dp(time + 1, idx, tuple(nm))

        # don't turn it on
        r2 = 0
        for nb in graph[m2[idx]]:
            r2 = max(r2, dp(time + 1, m[nb], tuple(mask)))

        return max(r1, cur_flow + r2)

dpc = {}

def dp2(time, idx, idx2, mask):
    if time == 26:
        return 0
    if idx > idx2:
        idx, idx2 = idx2, idx
    do_work = False
    cur_flow = 0
    for i in range(len(m)):
        if mask & (1 << i):
            cur_flow += flow[m2[i]]
        else:
            if flow[m2[i]] > 0:
                do_work = True
    key = (time, idx, idx2, mask)
    if key in dpc:
        return dpc[key]
    
    if not do_work:
        return cur_flow * (26 - time)
    
    r1 = r2 = 0    
    if do_work:
        nm = mask
        if not (mask & (1 << idx)) and flow[m2[idx]] > 0:
            # i turn on
            nm |= 1 << idx
            for nb2 in graph[m2[idx2]]:
                r1 = max(r1, dp2(time + 1, idx, m[nb2], nm))
            if not (mask & (1 << idx2)) and flow[m2[idx2]] > 0:
                nm |= 1 << idx2
                r1 = max(r1, dp2(time + 1, idx, idx2, nm))
        # i move
        nm = mask
        if not (mask & (1 << idx2)) and flow[m2[idx2]] > 0:
            nm |= 1 << idx2
        for nb in graph[m2[idx]]:
            r2 = max(r2, dp2(time + 1, m[nb], idx2, nm))
        nm = mask
        for nb in graph[m2[idx]]:
            for nb2 in graph[m2[idx2]]:
                r2 = max(r2, dp2(time + 1, m[nb], m[nb2], nm))

    res = cur_flow + max(r1, r2)
    dpc[key] = res
    return res

def get_flow(mask):
    do_work = False
    cur_flow = 0
    for i in range(len(m)):
        if mask & (1 << i):
            cur_flow += flow[m2[i]]
        else:
            if flow[m2[i]] > 0:
                do_work = True
    return cur_flow, do_work

def bfs(s):
    q = deque()
    q.append((s, -1))
    prv = {}
    prv[s] = -1
    while q:
        u, p = q.popleft()
        for v in graph[m2[u]]:
            v = m[v]
            if v not in prv:
                prv[v] = u
                q.append((v, u))
    paths = {}
    for i in range(len(m)):
        if i == s:
            continue
        cur = i
        path = []
        while cur != -1:
            path.append(cur)
            cur = prv[cur]
        paths[i] = path[::-1]
    return paths

interesting = [i for i in range(len(m)) if flow[m2[i]] > 0]
all_paths = {}
for v in interesting:
    all_paths[v] = bfs(v)


@cache
def dp3(time, idx1, idx2, mask, t1, t2):
    if time == 26:
        return 0
    if idx1 > idx2:
        idx1, idx2 = idx2, idx1
        t1, t2 = t2, t1
    cur_flow, do_work = get_flow(mask)
    if not do_work:
        return cur_flow * (26 - time)
    
    # am i going somewhere?
    # if t1 == 


# not 2137
print(dp2(0, target, target, 0))
