def quad(x, y, n):
    check = nums[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != nums[i][j]:
                print("(",end="")
                quad(x, y, n // 2)
                quad(x, y + n // 2, n // 2)
                quad(x + n // 2, y, n // 2)
                quad(x + n // 2, y + n // 2, n // 2)
                print(")", end="")
                return
    print(check,end="")
    return

num = int(input())
nums = []
for i in range(num):
    nums.append(input())
quad(0,0,num)
