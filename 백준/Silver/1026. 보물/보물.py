def minimum_sum(A, B):
    # A는 오름차순으로 정렬
    A.sort()
    # B는 내림차순으로 정렬
    B.sort(reverse=True)

    # 두 배열의 요소를 곱한 후 합산
    result = sum(a * b for a, b in zip(A, B))
    return result

# 입력 받기
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 결과 출력
print(minimum_sum(A, B))
