white = 0
blue = 0


def cut(x, y, n):
    global blue, white
    check = nums[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != nums[i][j]:
                cut(x, y, n // 2)
                cut(x + n // 2, y, n // 2)
                cut(x, y + n // 2, n // 2)
                cut(x + n // 2, y + n // 2, n // 2)
                return
    if check == 1:
        blue += 1
        return
    else:
        white += 1
        return


n = int(input())
nums = []
for i in range(n):
    nums.append(list(map(int, input().split())))
cut(0, 0, n)
print(white)
print(blue)
