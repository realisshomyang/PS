def solution(s, N):
    answer = 0
    lst = [x for x in range(1,N+1)]
    print(lst)
    for i in range(len(s)-N+1):
        tmp = s[i:i+N]
        tmpnum = int(''.join(tmp))
        sorted_tmp = list(map(int,sorted(tmp)))
        if (sorted_tmp == lst):
            print(sorted_tmp)
            if (answer < tmpnum):
                answer = tmpnum
    if(answer == 0):
        return -1

    return answer

print(solution("1451232125",2))