lst = [int(input()) for _ in range(9)]
lst.sort()
all = sum(lst)

for i in range(9):
    for j in range(i+1, 9):
        if all - lst[i] - lst[j] == 100:
            a = lst[i]
            b = lst[j]

lst.remove(a)
lst.remove(b)

for x in lst:
    print(x)
