import sys

def count_consecutive_sums(N):
    count = 0
    start = 1
    end = 1
    current_sum = 1

    while start <= N:
        if current_sum < N:
            end += 1
            current_sum += end
        elif current_sum > N:
            current_sum -= start
            start += 1
        else:  # current_sum == N
            count += 1
            current_sum -= start
            start += 1

    return count

# 입력 처리
input = sys.stdin.read
N = int(input().strip())

# 함수 호출 및 결과 출력
result = count_consecutive_sums(N)
print(result)
