def largest_increasing_subsequence_sum(arr):
    n = len(arr)
    dp = arr[:]  # dp[i] 초기값을 arr[i]로 설정

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + arr[i])
    
    return max(dp)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))
    
    result = largest_increasing_subsequence_sum(arr)
    print(result)

if __name__ == "__main__":
    main()
