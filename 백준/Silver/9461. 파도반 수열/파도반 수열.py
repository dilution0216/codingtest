def padovan_sequence(n):
    # 미리 계산된 파도반 수열 값 저장 리스트 초기화
    if n <= 5:
        return dp[n]
    
    for i in range(6, n+1):
        dp[i] = dp[i-1] + dp[i-5]
    
    return dp[n]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])  # 테스트 케이스의 수
    test_cases = [int(data[i]) for i in range(1, t+1)]
    
    # 미리 계산된 파도반 수열 값 저장 리스트
    global dp
    dp = [0] * 101
    dp[1] = dp[2] = dp[3] = 1
    dp[4] = dp[5] = 2
    
    results = [padovan_sequence(n) for n in test_cases]
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
