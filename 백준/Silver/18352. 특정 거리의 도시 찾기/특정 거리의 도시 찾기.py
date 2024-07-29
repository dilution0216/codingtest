from collections import deque

def find_cities_at_distance(n, m, k, x, roads):
    # 그래프 초기화
    graph = [[] for _ in range(n + 1)]
    for road in roads:
        a, b = road
        graph[a].append(b)  # 도로 정보로 그래프 구축
    
    # 거리 저장 배열 초기화
    distance = [-1] * (n + 1)
    distance[x] = 0  # 시작 도시의 거리는 0으로 설정
    
    # BFS를 위한 큐 초기화
    queue = deque([x])
    
    while queue:
        current = queue.popleft()  # 큐에서 현재 도시를 꺼냄
        
        for neighbor in graph[current]:
            if distance[neighbor] == -1:  # 방문하지 않은 도시라면
                distance[neighbor] = distance[current] + 1  # 거리 갱신
                queue.append(neighbor)  # 큐에 추가
    
    # 거리 k인 도시 찾기
    result = []
    for i in range(1, n + 1):
        if distance[i] == k:
            result.append(i)  # 거리 k인 도시를 결과 리스트에 추가
    
    return result  # 결과 반환

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])  # 도시의 개수
    m = int(data[idx + 1])  # 도로의 개수
    k = int(data[idx + 2])  # 거리 정보
    x = int(data[idx + 3])  # 출발 도시 번호
    idx += 4
    
    roads = []
    for _ in range(m):
        a = int(data[idx])
        b = int(data[idx + 1])
        roads.append((a, b))  # 도로 정보를 리스트에 저장
        idx += 2
    
    result = find_cities_at_distance(n, m, k, x, roads)  # 거리 k인 도시 찾기
    
    if result:
        for city in sorted(result):  # 결과를 정렬하여 출력
            print(city)
    else:
        print(-1)  # 결과가 없으면 -1 출력

if __name__ == "__main__":
    main()