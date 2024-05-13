def solution(n):
    answer = []
    if n[-1] > n[-2]:
        n.append(n[-1]-n[-2])
    elif n[-1] <= n[-2]:
        n.append(2*n[-1])
    return n