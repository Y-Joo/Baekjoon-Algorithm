n=int(input())
strs=[]
for i in range(n):
    word=input()
    cnt=len(word)
    strs.append((word, cnt))
strs=list(set(strs))
strs.sort(key=lambda word:(word[1],word[0]))
for word in strs:
    print(word[0])