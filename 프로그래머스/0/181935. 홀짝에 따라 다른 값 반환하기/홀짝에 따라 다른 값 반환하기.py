def solution(n):
    answer=0
    #홀수
    if n%2==1:
        for i in range(1,n+1,2):
            answer+=i
    else:
        #짝수
        for j in range(2,n+1,2):
            answer+=j*j
    return answer