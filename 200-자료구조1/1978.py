a = input()
b = list(map(int, input().split()))
result = []
flag = 0
for x in b:
    flag = 0
    if x == 1:
        continue
    else:
        for i in range(2, x):
            if x % i == 0:
                flag = 1
        if flag == 0:
            result.append(x)


print(len(result))
