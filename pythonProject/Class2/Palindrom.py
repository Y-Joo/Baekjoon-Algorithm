while 1:
    flag=0
    n=input()
    if n=='0':
        break
    for i in range(len(n)):
        j=len(n) - i - 1
        if n[i]!=n[j]:
            flag=1
            break
    if flag:
        print("no")
    else:
        print("yes")