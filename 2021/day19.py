from sortedcontainers import *

from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; py day19.py < sample.in
echo "=== real ===" ; py day19.py < day19.in
echo "=== sample ===" ; py day19.py < sample.in ; echo "=== real ===" ; py day19.py < day19.in
"""

# A = read_input('/dev/stdin')

f = open('/dev/stdin')
parts = f.read().strip().split('\n\n')

def gen_orientations():
    # 48
    for i in (-1, 1):
        for j in (-1, 1):
            for k in (-1, 1):
                for rest in itertools.permutations(range(3)):
                    yield rest + (i, j, k)

def transform_forward(orientation, coord):
    x, y, z, xp, yp, zp = orientation
    res = [None] * 3
    res[x] = coord[0] * xp
    res[y] = coord[1] * yp
    res[z] = coord[2] * zp
    return tuple(res)

def transform_backward(orientation, coord):
    x, y, z, xp, yp, zp = orientation
    res = [None] * 3
    res[0] = coord[x] * xp
    res[1] = coord[y] * yp
    res[2] = coord[z] * zp
    return tuple(res)

def addc(a, b):
    res = []
    for i in range(len(a)):
        res.append(a[i] + b[i])
    return tuple(res)
def subc(a, b):
    res = []
    for i in range(len(a)):
        res.append(a[i] - b[i])
    return tuple(res)

COMMON = 12
RADIUS = 1000

res = 0

A = defaultdict(list)

for part in parts:
    part = part.strip().splitlines()
    sid = int(part[0].strip().split()[2])
    for line in part[1:]:
        coord = tuple(map(int, line.strip().split(',')))
        A[sid].append(coord)

SCANNERS = len(A)

locations = [None] * SCANNERS
orientations = [None] * SCANNERS
locations[0] = (0, 0, 0)
orientations[0] = (0, 1, 2, 1, 1, 1)

all_beacons = set()

bad = set()

while True:
    for s1 in range(SCANNERS):
        if locations[s1] is None:
            continue
        i_absolute_seen = []
        for coord in A[s1]:
            i_absolute_seen.append(addc(locations[s1], transform_forward(orientations[s1], coord)))
        i_absolute_seen_set = set(i_absolute_seen)
        for s2 in range(SCANNERS):
            if s1 == s2 or locations[s2] is not None or (s1, s2) in bad:
                continue
            # s1 known, s2 is not known
            print('trying', s1, s2)
            for ori in gen_orientations():
                all_rel = []
                for coord in A[s2]:
                    # try it
                    rel = transform_forward(ori, coord)
                    all_rel.append(rel)
                # could s1 and s2 see some subset?
                for i in range(len(i_absolute_seen)):
                    for j in range(len(all_rel)):
                        # assume j is at the absolute position of the point i
                        shift = subc(i_absolute_seen[i], all_rel[j])
                        match_count = 0
                        for j in range(len(all_rel)):
                            pt = addc(all_rel[j], shift)
                            if pt in i_absolute_seen_set:
                                match_count += 1
                                if match_count >= COMMON:
                                    break
                        if match_count >= COMMON:
                            # found it
                            print('found', s2)
                            locations[s2] = shift
                            orientations[s2] = ori
                            break
                    if locations[s2] is not None:
                        break
                if locations[s2] is not None:
                    break
            if locations[s2] is None:
                bad.add((s1, s2))
            if locations[s2] is not None:
                break

    if all(locations):
        break

for s1 in range(SCANNERS):
    for coord in A[s1]:
        all_beacons.add(addc(locations[s1], transform_forward(orientations[s1], coord)))


print(len(all_beacons))
print(locations)
res = 0
for s1 in range(SCANNERS):
    for s2 in range(SCANNERS):
        x, y, z = subc(locations[s1], locations[s2])
        res = max(res, abs(x) + abs(y) + abs(z))
print(res)
