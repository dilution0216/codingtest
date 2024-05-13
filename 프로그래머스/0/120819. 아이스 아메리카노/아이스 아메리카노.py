def solution(money):
    answer = []
    coffe_count = int(money//5500)
    answer.append(coffe_count)
    answer.append(money-(5500*coffe_count))
    return answer