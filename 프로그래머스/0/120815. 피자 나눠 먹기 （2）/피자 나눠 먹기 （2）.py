import math

def lcm(x, y):
    return x * y // math.gcd(x, y)


def solution(n):
    zz = 0
    zz = lcm(6,n)
    
    answer = zz//6
    return answer