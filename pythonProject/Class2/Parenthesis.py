
n = int(input())
for i in range(n):
    stack = []
    s = input()
    flag = 0
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                flag = 1
                break
            if stack.pop() != '(':
                flag = 1
                break
    if stack:
        flag=1

    if flag:
        print("NO")
    else:
        print("YES")
