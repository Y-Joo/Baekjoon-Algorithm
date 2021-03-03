from typing import List
import sys

sys.setrecursionlimit(100000)
cnt=0

def find(parents: List[int], x: int):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]


def union(parents: List[int], a: int, b: int):
    global cnt
    cnt+=1
    a = find(parents, a)
    b = find(parents, b)
    if a < b:
        parents[b] = a
    elif a==b:
        return cnt
    else:
        parents[a] = b


n, m = map(int, input().split())
parents = [i for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    ret = union(parents, a, b)
    if ret:
        print(ret)
        sys.exit()
print(0)