from typing import List
import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

def find_parent(parent: List[int], x: int) -> int:
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent: List[int], a: int, b: int):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parents = [0] * (n + 1)
for i in range(n + 1):
    parents[i] = i
for i in range(m):
    fc, a, b = map(int, input().split())
    if fc == 1:
        if find_parent(parents, a) == find_parent(parents, b):
            print("YES")
        else:
            print("NO")
    else:
        union_parent(parents, a, b)
