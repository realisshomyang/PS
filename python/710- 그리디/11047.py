n, k = map(int, input().split())

lst = [int(input()) for _ in range(n)]
lst.reverse()
count = 0
while (k):
    for x in lst:
        if (k//x != 0):
            count += (k//x)
            k = k - x*(k//x)
print(count)
