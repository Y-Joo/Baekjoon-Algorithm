n=int(input())
users=[]
for i in range(n):
    age, name=input().split()
    age=int(age)
    users.append((age, name))
users.sort(key=lambda user : user[0])
for user in users:
    print(user[0], user[1])