import sys
input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

# 누적 합 배열 계산
prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix_sum[i][j] = array[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

# 쿼리 처리
k = int(input())
queries = [list(map(int, input().split())) for _ in range(k)]

for x1, y1, x2, y2 in queries:
    result = (prefix_sum[x2][y2]
              - prefix_sum[x1 - 1][y2]
              - prefix_sum[x2][y1 - 1]
              + prefix_sum[x1 - 1][y1 - 1])
    print(result)
