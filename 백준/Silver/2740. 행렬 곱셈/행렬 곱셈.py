def matrix_multiplication(A, B):
    n = len(A)          # A의 행 수
    m = len(A[0])       # A의 열 수 (== B의 행 수)
    k = len(B[0])       # B의 열 수
    
    # 결과 행렬 C를 0으로 초기화
    C = [[0] * k for _ in range(n)]
    
    # 행렬 곱셈 수행
    for i in range(n):
        for j in range(k):
            for l in range(m):
                C[i][j] += A[i][l] * B[l][j]
    
    return C

# 입력 받기
n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

m, k = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(m)]

# 행렬 곱셈 수행
C = matrix_multiplication(A, B)

# 결과 출력
for row in C:
    print(' '.join(map(str, row)))
