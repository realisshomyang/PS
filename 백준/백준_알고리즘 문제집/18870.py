import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
sortedarr = []

sortedarr = list(sorted(set(arr)))

dic = {sortedarr[i]:i for i in range (len(sortedarr))}

for i in arr:
    print(dic[i],end=' ')