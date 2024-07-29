from collections import deque

# 입력 받기
n, k = map(int, input().split())

# 큐 초기화
queue = deque(range(1, n + 1))
result = []

# 요세푸스 순열 구하기
while queue:
    queue.rotate(-(k - 1))  # 큐를 k-1만큼 회전
    result.append(queue.popleft())  # k번째 사람을 결과에 추가

# 결과 출력
print('<' + ', '.join(map(str, result)) + '>')
