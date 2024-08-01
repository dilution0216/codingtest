def longest_decreasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # 모든 원소를 1로 초기화 (각각 자기 자신만으로 수열을 이룸)

    for i in range(1, n):
        for j in range(0, i):
            if arr[j] > arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))
    
    result = longest_decreasing_subsequence(arr)
    print(result)

if __name__ == "__main__":
    main()
