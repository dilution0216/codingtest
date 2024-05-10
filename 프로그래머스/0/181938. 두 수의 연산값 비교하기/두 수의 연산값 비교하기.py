def solution(a, b):
    str_a = str(a)
    str_b = str(b)
    if int(str_a+str_b) > 2*a*b:
        answer = int(str_a+str_b)
    elif int(str_a+str_b) < 2*a*b:
        answer = 2*a*b
    else:
        answer = int(str_a+str_b)
    return answer