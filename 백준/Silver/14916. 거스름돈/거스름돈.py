def min_coins(n):
    # 5원 동전을 최대한 많이 사용
    count_5 = n // 5
    
    # 남은 금액을 2원 동전으로 거슬러 줄 수 있는지 확인
    while count_5 >= 0:
        remaining = n - (count_5 * 5)
        if remaining % 2 == 0:
            count_2 = remaining // 2
            return count_5 + count_2
        count_5 -= 1
    
    return -1  # 거슬러 줄 수 없는 경우

def main():
    import sys
    input = sys.stdin.read
    n = int(input().strip())
    
    result = min_coins(n)
    print(result)

if __name__ == "__main__":
    main()
