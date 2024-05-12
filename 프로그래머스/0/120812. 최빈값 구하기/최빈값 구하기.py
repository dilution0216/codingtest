def solution(array):
    counts = {}  # 각 값의 빈도를 저장할 딕셔너리

    # 배열의 각 요소의 빈도를 세기
    for num in array:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    max_count = max(counts.values())  # 가장 높은 빈도
    mode = [num for num, count in counts.items() if count == max_count]  # 최빈값들을 모은 리스트

    if len(mode) > 1:  # 최빈값이 여러 개인 경우
        return -1
    else:
        return mode[0]  # 최빈값 반환