import collections, sys
t= int(sys.stdin.readline())
for i in range(t):
    cnt=0
    flag=0
    fun=input()
    n = int(sys.stdin.readline())
    s=input()[1:-1]
    if n>1:
        a=collections.deque(map(int,s.split(',')))
    elif n==1:
        a=collections.deque([int(s)])
    else:
        a=collections.deque()
    for char in fun:
        if char == 'R':
            cnt+=1
        else:
            if a:
                if cnt%2==0:
                    a.popleft()
                else:
                    a.pop()
            else:
                flag=1
                break
    if cnt%2==1:
        a.reverse()
    if flag:
        print('error')
    else:
        print("[", end="")
        for i in range(len(a)):
            if i == len(a) - 1:
                print(a[i], end="")
            else:
                print(str(a[i]) + ",", end="")
        print("]")
    a.clear()