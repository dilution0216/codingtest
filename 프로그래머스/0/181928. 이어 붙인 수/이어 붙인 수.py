def solution(num_list):
    a=""
    b=""
    for i in num_list:
        if i%2==1:
            a=a+str(i)
        if i%2==0:
            b=b+str(i)
    answer = int(a)+int(b)
    return answer