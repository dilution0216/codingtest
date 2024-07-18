import sys

# 입력 처리
input = sys.stdin.read
data = input().split()
N = int(data[0])
M = int(data[1])
A = list(map(int, data[2:]))

def count_subsequences_with_sum_sliding_window(A, N, M):
    count = 0
    start = 0
    end = 0
    current_sum = 0

    while end < N:
        current_sum += A[end]
        end += 1

        while current_sum >= M:
            if current_sum == M:
                count += 1
            current_sum -= A[start]
            start += 1

    return count

# 함수 호출
result_sliding_window = count_subsequences_with_sum_sliding_window(A, N, M)
print(result_sliding_window)