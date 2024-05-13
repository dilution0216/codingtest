def solution(numLog):
    key = {1:'w', -1:'s', 10:'d', -10:'a'}
    answer = ''
    n=0
    for i in range(len(numLog)-1):
        j=numLog[i+1]-numLog[i]
        answer+=key[j]
    return answer