def dfs(graph, start, visited):
    stack = [start]  # 스택에 시작 노드를 추가
    count = 0  # 방문한 노드 수를 세기 위한 변수
    
    while stack:
        node = stack.pop()  # 스택에서 노드를 꺼냄
        if not visited[node]:  # 노드가 방문되지 않았다면
            visited[node] = True  # 방문 처리
            count += 1  # 방문한 노드 수 증가
            stack.extend(graph[node])  # 노드에 연결된 노드들을 스택에 추가
    
    return count  # 방문한 노드 수 반환

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])  # 컴퓨터의 수
    m = int(data[1])  # 연결된 쌍의 수
    
    graph = [[] for _ in range(n + 1)]  # 그래프 초기화
    
    idx = 2
    for _ in range(m):
        a = int(data[idx])
        b = int(data[idx + 1])
        graph[a].append(b)  # 양방향 연결
        graph[b].append(a)
        idx += 2
    
    visited = [False] * (n + 1)  # 방문 여부 리스트 초기화
    
    result = dfs(graph, 1, visited) - 1  # 1번 컴퓨터 제외한 결과
    
    print(result)  # 결과 출력

if __name__ == "__main__":
    main()
