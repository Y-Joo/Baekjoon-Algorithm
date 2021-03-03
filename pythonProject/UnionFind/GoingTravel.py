from typing import List
import sys

sys.setrecursionlimit(100000)


def find(parents: List[int], x: int):
    if parents[x] != x:
        parents[x]= find(parents, parents[x])
    return parents[x]


def union(parents: List[int], a: int, b: int):
    a = find(parents, a)
    b = find(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


n=int(input())
m=int(input())
parents=[i for i in range(n+1)]

for i in range(n):
    nums=list(map(int,input().split()))
    for j in range(n):
        if nums[j]==1:
            union(parents, i+1,j+1)
plan=list(map(int, input().split()))
cycle=parents[plan[0]]
flag=0
for i in range(len(plan)):
    if parents[plan[i]]!=cycle:
        print("NO")
        flag=1
        break
if flag==0:
    print("YES")
