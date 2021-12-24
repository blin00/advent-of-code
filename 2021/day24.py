from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day24.py < sample.in
echo "=== real ===" ; py day24.py < day24.in
echo "=== sample ===" ; py day24.py < sample.in ; echo "=== real ===" ; py day24.py < day24.in
"""

A = read_input('/dev/stdin', strip_lines=False)

N = len(A)


def simulate(inp):
    ip = 0
    assert len(A) % 18 == 0
    res = []
    regs = defaultdict(int)
    while ip < len(A):
        ins = A[ip].split()
        op = ins[0]
        if op == 'inp':
            val = int(next(inp))
            regs[ins[1]] = val
        elif op == 'add':
            a, b = map(maybe_int, ins[1:])
            if isinstance(b, str):
                regs[a] += regs[b]
            else:
                regs[a] += b
        elif op == 'mul':
            a, b = map(maybe_int, ins[1:])
            if isinstance(b, str):
                regs[a] *= regs[b]
            else:
                regs[a] *= b
        elif op == 'div':
            a, b = map(maybe_int, ins[1:])
            if isinstance(b, str):
                regs[a] //= regs[b]
            else:
                regs[a] //= b
        elif op == 'mod':
            a, b = map(maybe_int, ins[1:])
            if isinstance(b, str):
                regs[a] %= regs[b]
            else:
                regs[a] %= b
        elif op == 'eql':
            a, b = map(maybe_int, ins[1:])
            if isinstance(b, str):
                val = regs[b]
            else:
                val = b
            if regs[a] == val:
                regs[a] = 1
            else:
                regs[a] = 0
        ip += 1
        if ip % 18 == 0:
            res.append(regs['z'])
    return res

res = 0

# x = ((z % 26 + A) != inp)
# z /= divz
# z *= (25 * x) + 1
# z += (inp + B) * x

parts = N // 18

B = []

for i in range(parts):
    base = i * 18
    divz = int(A[base + 4].split()[2])
    add1 = int(A[base + 5].split()[2])
    add2 = int(A[base + 15].split()[2])
    B.append((divz, add1, add2))

from z3 import *

inp = [Int('inp{}'.format(i)) for i in range(14)]
s = Solver()
for x in inp:
    s.add(x >= 1)
    s.add(x <= 9)

s.add(inp[0] == 4)
s.add(inp[1] <= 5)
# s.add(inp[2] == 9)
# s.add(inp[3] == 9)
# s.add(inp[4] == 9)
# s.add(inp[5] >= 7)

print(B)

z = Int('z')
s.add(z == 0)
for i in range(len(B)):
    divz, add1, add2 = B[i]
    x = If((z % 26 + add1) != inp[i], 1, 0)
    if divz != 1:
        z = z / divz
    # z = z * ((25 * x) + 1)
    z = If(x == 1, z * 26, z)
    z = If(x == 1, z + inp[i] + add2, z)

s.add(z == 0)


best = int(1e19)

while s.check() == sat:
    m = s.model()
    res = []
    dup = []
    for i, e in enumerate(inp):
        x = m[e].as_long()
        res.append(x)
        dup.append(e != x)
    y = int(''.join(map(str, res)))
    if y < best:
        print(y)
        best = y
    best = min(best, y)
    s.add(Or(*dup))
print('ans:', best)
