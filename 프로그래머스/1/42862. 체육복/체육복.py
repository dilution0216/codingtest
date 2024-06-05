def solution(n, lost, reserve):
    # 여벌 체육복이 있지만 도난당한 학생을 제외
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    
    # 체육복을 빌려주는 과정
    for r in reserve_set:
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)
    
    # 최종적으로 체육복을 입을 수 있는 학생의 수
    return n - len(lost_set)