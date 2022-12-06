from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day6.py < sample.in
echo "=== real ===" ; py day6.py < day6.in
echo "=== sample ===" ; py day6.py < sample.in ; echo "=== real ===" ; py day6.py < day6.in
"""

A = sys.stdin.read().strip()


for i in range(0, len(A) - 13):
    if len(set(A[i:i+14])) == 14:
        print(i + 14)
        break
