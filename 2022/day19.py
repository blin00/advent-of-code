from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

from util import *

"""
echo "=== sample ===" ; pypy3 day19.py < sample.in
echo "=== real ===" ; pypy3 day19.py < day19.in
echo "=== sample ===" ; pypy3 day19.py < sample.in ; echo "=== real ===" ; pypy3 day19.py < day19.in
"""

A = sys.stdin.read().strip().splitlines()
N = len(A)

blueprints = []

TL = 32

for line in A:
    idx, ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian = ints(line)
    blueprints.append((ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian))

blueprints = blueprints[:3]

BP_GLOBAL = blueprints[0]

cur_best = 0

dp = {}
def solve(time, state):
    global cur_best
    bp = BP_GLOBAL
    max_ore_cost = max(bp[0], bp[1], bp[2], bp[4])
    max_clay_cost = bp[3]
    max_obsidian_cost = bp[5]
    if time >= TL:
        cur_best = max(cur_best, state[7])
        return state[7]
    new_states = []
    # construct any robots?
    orebot, claybot, obsidianbot, geodebot, ore, clay, obsidian, geode = state
    if orebot >= max_ore_cost and ore >= max_ore_cost:
        ore = max_ore_cost
    if claybot >= max_clay_cost and clay >= max_clay_cost:
        clay = max_clay_cost
    if obsidianbot >= max_obsidian_cost and obsidian >= max_obsidian_cost:
        obsidian = max_obsidian_cost
    best_case = geode
    tmp = geodebot
    for i in range(time, TL):
        best_case += tmp
        tmp += 1
    if best_case < cur_best:
        return 0
    state = (orebot, claybot, obsidianbot, geodebot, ore, clay, obsidian, geode)
    key = (time, state)
    if key in dp:
        return dp[key]
    harvest = [0] * 4 + list(state[:4])
    if orebot >= bp[4] and obsidianbot >= bp[5]:
        if ore >= bp[4] and obsidian >= bp[5]:
            new_states.append((orebot, claybot, obsidianbot, geodebot + 1, ore - bp[4], clay, obsidian - bp[5], geode))
        else:
            new_states.append(state)
    else:
        if ore >= bp[4] and obsidian >= bp[5]:
            new_states.append((orebot, claybot, obsidianbot, geodebot + 1, ore - bp[4], clay, obsidian - bp[5], geode))
        if ore >= bp[2] and clay >= bp[3] and obsidianbot < max_obsidian_cost:
            new_states.append((orebot, claybot, obsidianbot + 1, geodebot, ore - bp[2], clay - bp[3], obsidian, geode))
        if ore >= bp[0] and orebot < max_ore_cost:
            new_states.append((orebot + 1, claybot, obsidianbot, geodebot, ore - bp[0], clay, obsidian, geode))
        if ore >= bp[1] and claybot < max_clay_cost:
            new_states.append((orebot, claybot + 1, obsidianbot, geodebot, ore - bp[1], clay, obsidian, geode))
        new_states.append(state)
    # add the harvest
    ns2 = []
    for state in new_states:
        ns2.append(tuple(map(add, state, harvest)))
    res = 0
    for ns in ns2:
        res = max(res, solve(time + 1, ns))
    dp[key] = res
    return res


res = 1
for idx, bp in enumerate(blueprints):
    cur_best = 0
    dp.clear()
    BP_GLOBAL = bp
    num = solve(0, (1, 0, 0, 0, 0, 0, 0, 0))
    print(idx + 1, num)
    res *= num
# not 1898, 130, 1818, 1936
print('final:', res)
