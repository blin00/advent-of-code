try:
    from sortedcontainers import *
    from math import gcd, lcm
except ImportError:
    pass
from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; python3 day21.py < sample.in
echo "=== real ===" ; python3 day21.py < day21.in
echo "=== sample ===" ; python3 day21.py < sample.in ; echo "=== real ===" ; python3 day21.py < day21.in
"""

A = sys.stdin.read().strip().splitlines()
N = len(A)

graph = {}


from z3 import *

for line in A:
    result, ops = line.split(': ')
    ops = ops.split(' ')
    if len(ops) == 1:
        graph[result] = int(ops[0])
    else:
        graph[result] = ops

me = Int('humn')
def get(node):
    assert node in graph
    if node == 'humn':
        return me
    if isinstance(graph[node], int):
        return graph[node]
    else:
        a, op, b = graph[node]
        a = get(a)
        b = get(b)
        if op == '+':
            return a + b
        elif op == '*':
            return a * b
        elif op == '-':
            return a - b
        elif op == '/':
            return a / b

a = get('wrvq')
b = get('vqfc')

s = Solver()
s.add(a == b)
assert s.check() == sat
m = s.model()
a = m[me].as_long()

print(a)
