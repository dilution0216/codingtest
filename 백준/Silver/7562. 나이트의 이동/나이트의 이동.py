from collections import deque

def bfs(start, end, l):
    # 나이트의 이동 방향 8가지 정의
    directions = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    # 방문 여부를 저장하는 2차원 리스트
    visited = [[False] * l for _ in range(l)]
    # BFS를 위한 큐, 초기 위치와 이동 횟수를 함께 저장
    queue = deque([(start[0], start[1], 0)])  # (x, y, 이동 횟수)
    
    while queue:
        x, y, moves = queue.popleft()  # 큐에서 현재 위치와 이동 횟수를 꺼냄
        
        # 목표 위치에 도달하면 이동 횟수를 반환
        if (x, y) == end:
            return moves
        
        # 나이트의 모든 이동 방향에 대해 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 새로운 위치가 체스판 안에 있고, 방문하지 않은 곳이라면
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True  # 방문 표시
                queue.append((nx, ny, moves + 1))  # 큐에 새로운 위치와 이동 횟수 추가
    
    return -1  # 도달할 수 없는 경우 (문제 조건상 이 경우는 없음)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])  # 테스트 케이스 수
    idx += 1
    results = []
    
    for _ in range(t):
        l = int(data[idx])  # 체스판의 크기
        idx += 1
        start = (int(data[idx]), int(data[idx + 1]))  # 시작 위치
        idx += 2
        end = (int(data[idx]), int(data[idx + 1]))  # 목표 위치
        idx += 2
        results.append(bfs(start, end, l))  # 각 테스트 케이스에 대해 bfs 실행
    
    for result in results:
        print(result)  # 결과 출력

if __name__ == "__main__":
    main()
