from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day16.py < sample.in
echo "=== real ===" ; py day16.py < day16.in
echo "=== sample ===" ; py day16.py < sample.in ; echo "=== real ===" ; py day16.py < day16.in
"""

A = read_input('/dev/stdin')

# f = open('/dev/stdin')
# parts = f.read().strip().split('\n\n')

N = len(A)


bignum = int(A, 16)
bits = map(int, bin(bignum)[2:])
if len(bits) % 4 != 0:
    bits = ([0] * (4 - len(bits) % 4)) + bits

def reassemble(bits):
    r = []
    for b in bits:
        r.append(str(b))
    return int(''.join(r), 2)
sv = 0
def decode(packet, idx):
    global sv
    version = reassemble(packet[idx:idx + 3])
    sv += version
    typ = reassemble(packet[idx + 3:idx + 6])
    idx += 6
    if typ == 4:
        r = []
        while True:
            group = packet[idx:idx + 5]
            idx += 5
            r += group[1:]
            if group[0] == 0:
                # done
                break
        return idx, reassemble(r)
    else:
        length_typ = packet[idx]
        idx += 1
        r = []
        if length_typ == 0:
            total_length = reassemble(packet[idx:idx + 15])
            idx += 15
            orig_idx = idx
            while True:
                idx, rest = decode(packet, idx)
                r.append(rest)
                if idx - orig_idx == total_length:
                    break
                assert idx - orig_idx < total_length

        else:
            count_packets = reassemble(packet[idx:idx + 11])
            idx += 11
            for i in range(count_packets):
                idx, rest = decode(packet, idx)
                r.append(rest)
        if typ == 0:
            # sum
            return idx, sum(r)
        elif typ == 1:
            # product
            return idx, prod(r)
        elif typ == 2:
            # min
            return idx, min(r)
        elif typ == 3:
            # max
            return idx, max(r)
        elif typ == 5:
            assert len(r) == 2
            return idx, 1 if r[0] > r[1] else 0
        elif typ == 6:
            assert len(r) == 2
            return idx, 1 if r[0] < r[1] else 0
        elif typ == 7:
            assert len(r) == 2
            return idx, 1 if r[0] == r[1] else 0
        else:
            assert False


t = decode(bits, 0)
print(sv)
print(t)
