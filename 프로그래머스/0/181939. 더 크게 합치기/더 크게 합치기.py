def solution(a, b):
    a = str(a)
    b = str(b)
    answer=''
    if int(a+b) > int(b+a):
        answer=a+b
    elif int(a+b) < int(b+a):
        answer=b+a
    else:
        answer=a+b
    
    return int(answer)
        