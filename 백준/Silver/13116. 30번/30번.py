def find_lca(a, b):
    # 주어진 노드 a와 b의 경로를 추적합니다.
    path_a = []
    path_b = []

    # 루트 노드부터 a까지의 경로
    while a >= 1:
        path_a.append(a)
        a //= 2
    
    # 루트 노드부터 b까지의 경로
    while b >= 1:
        path_b.append(b)
        b //= 2
    
    # 공통 조상 찾기
    path_a = set(path_a)
    for node in path_b:
        if node in path_a:
            return node

# 입력을 처리하여 문제를 해결합니다.
def solve_problem(pairs):
    results = []
    for a, b in pairs:
        lca = find_lca(a, b)
        results.append(lca * 10)
    return results

# 표준 입력 처리
import sys
input = sys.stdin.read
data = input().split()

# 입력 형식 처리
num_cases = int(data[0])
pairs = [(int(data[i*2+1]), int(data[i*2+2])) for i in range(num_cases)]

# 문제 해결 및 출력
results = solve_problem(pairs)
for result in results:
    print(result)
