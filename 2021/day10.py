from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day10.py < sample.in
echo "=== real ===" ; py day10.py < day10.in
echo "=== sample ===" ; py day10.py < sample.in ; echo "=== real ===" ; py day10.py < day10.in
"""
A = read_input('/dev/stdin')
N = len(A)

res = 0

table = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

opp = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

t2 = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

scores = []
for line in A:
    stack = []
    found = None
    for i, e in enumerate(line):
        if e in opp:
            if stack:
                if stack[-1] == opp[e]:
                    stack.pop()
                else:
                    found = i
                    break
            else:
                assert False
        else:
            stack.append(e)
    if found is not None:
        ill = line[i]
        res += table[ill]
    else:
        score = 0
        while stack:
            c = stack.pop()
            score *= 5
            score += t2[c]
        scores.append(score)
        

print(res)
scores.sort()
print(scores[len(scores) // 2])
