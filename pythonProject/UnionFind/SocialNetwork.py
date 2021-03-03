from typing import List
import sys
import collections

input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def find(parents: dict, x: str):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]


def union(parents: dict, a: str, b: str, cnt: dict):
    a = find(parents, a)
    b = find(parents, b)
    if a < b:
        parents[b] = a
        cnt[a] += cnt[b]
    elif a == b:
        return
    else:
        parents[a] = b
        cnt[b] += cnt[a]


t = int(input())
for i in range(t):
    n = int(input())
    parents = collections.defaultdict()
    cnt = collections.defaultdict()
    for j in range(n):
        a, b = input().split()
        if a not in parents.keys():
            parents[a] = a
            cnt[a] = 1
        if b not in parents.keys():
            parents[b] = b
            cnt[b] = 1
        union(parents, a, b, cnt)
        print(cnt[find(parents, a)])
