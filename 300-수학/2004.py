import math
a, b = map(int, input().split())


def count_num(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count


print(min(count_num(a, 2) - count_num(a - b, 2) - count_num(b, 2),
      count_num(a, 5) - count_num(a - b, 5) - count_num(b, 5)))
