
def solution(schedules):
    answer = 0    

    dp = [1 for i in range(len(schedules))]

    for i in range(len(schedules)):  
        for j in range(i):
            if schedules[i] > schedules[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return answer
