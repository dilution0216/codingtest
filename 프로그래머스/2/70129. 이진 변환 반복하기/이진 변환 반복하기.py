def solution(s):
    c = len(s)

    zero = 0 # 0 삭제 개수
    t_cnt = 0 # transformation 횟수

    while s != '1':

        zero_cnt = s.count('0') # 0의 개수
        zero += zero_cnt

        s = s.replace('0', '')
        c = len(s)

        s = str(format(c, 'b')) # 이진수로 변환
        t_cnt += 1




    answer = [t_cnt, zero]
    return answer