"""
from functools import lru_cache
import sys

sys.setrecursionlimit(20000)

@lru_cache
def height(x):
    if l[x] == -1:
        return 1
    else:
        return height(l[x]) + 1

n = int(input())
l = [int(i) for i in input().split()]
l2 = [height(i) for i in range(len(l))]
print(max(l2))
"""


from sys import setrecursionlimit

setrecursionlimit(20_000)


def height(x):
    if x in d:
        return max([height(i) for i in d[x]]) + 1
    return 1


d = {}
n = int(input())
l = [int(i) for i in input().split()]

for i, x in enumerate(l):
    if x in d:
        d[x].append(i)
    else:
        d[x] = [i]

for i, x in enumerate(l):
    if x == -1:
        print(height(i))
        break
