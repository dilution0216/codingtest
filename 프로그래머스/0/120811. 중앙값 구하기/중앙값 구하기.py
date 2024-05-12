def solution(array):
    n=len(array)
    #버블정렬 오름차순
    for i in range(n):
        for j in range(n-1):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
        
    answer = array[int(len(array)/2)]
    return answer