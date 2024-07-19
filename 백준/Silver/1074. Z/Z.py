def z_order(n, r, c):
    # 기본 크기가 1x1인 경우
    if n == 0:
        return 0
    
    # 절반 크기 계산
    half = 2 ** (n - 1)
    
    # 첫 번째 사분면
    if r < half and c < half:
        return z_order(n - 1, r, c)
    
    # 두 번째 사분면
    elif r < half and c >= half:
        return half * half + z_order(n - 1, r, c - half)
    
    # 세 번째 사분면
    elif r >= half and c < half:
        return 2 * half * half + z_order(n - 1, r - half, c)
    
    # 네 번째 사분면
    else:
        return 3 * half * half + z_order(n - 1, r - half, c - half)

# 입력 받기
n, r, c = map(int, input().split())
# 결과 출력
print(z_order(n, r, c))