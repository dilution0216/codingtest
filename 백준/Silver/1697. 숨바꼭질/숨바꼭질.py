from collections import deque

def bfs(start, target):
    # 최대 범위 설정 (문제 조건에서 수빈이와 동생의 위치는 0 이상 100000 이하)
    max_range = 100000
    # 방문 여부 및 시간을 저장하는 리스트
    visited = [0] * (max_range + 1)
    
    queue = deque([start])
    
    while queue:
        current = queue.popleft()  # 큐에서 현재 위치를 꺼냄
        
        if current == target:
            return visited[current]  # 동생을 찾으면 소요된 시간 반환
        
        # 현재 위치에서 갈 수 있는 세 가지 경우를 탐색
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos <= max_range and not visited[next_pos]:
                visited[next_pos] = visited[current] + 1  # 방문 시간 갱신
                queue.append(next_pos)  # 큐에 다음 위치 추가

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])  # 수빈이의 위치
    k = int(data[1])  # 동생의 위치
    
    result = bfs(n, k)  # BFS를 통해 최소 시간을 계산
    print(result)  # 결과 출력

if __name__ == "__main__":
    main()
