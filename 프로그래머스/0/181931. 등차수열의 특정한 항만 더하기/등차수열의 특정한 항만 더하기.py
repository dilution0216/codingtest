def solution(a, d, included):
    result = 0
    #등차수열 만들기
    bag = []
    for i in range(a, a+(d*len(included)), d):
        bag.append(i)
        
    for j in range(len(included)):
        if included[j] == True:
            result+= bag[j]
    return result