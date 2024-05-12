def solution(a, b, c):
    answer = 0
    if a!=b and b!=c and a!=c:
        answer = a+b+c
    elif a==b==c:
        answer = 27*a**6
    elif (a==b and b!=c) or (a==c and a!=b) or (b==c and a!=b):
        answer = (a+b+c)*(a**2+b**2+c**2)
    return answer