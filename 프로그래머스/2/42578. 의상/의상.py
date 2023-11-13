def solution(clothes):
    answer = 1							# 정답 변수
    types = [y for x, y in clothes]		# 의상 종류만 담기
    counts = [types.count(type) for type in set(types)]	# 종류별 개수 세기
    # 각 의상 종류별 (의상 개수+1) 곱하기
    for c in counts:
        answer *= c+1
    return answer -1	# 모두 입지 않는 경우의 수 제외



def solution2(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1
