def solution(num_list):
    a=1
    b=0
    for i in num_list:
        a=a*i
    for j in num_list:
        b=b+j
    if a<b**2:
        answer = 1
    else:
        answer = 0
    return answer