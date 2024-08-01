def minimum_decreases(levels):
    decreases = 0
    
    # 뒤에서 두 번째 요소부터 시작하여 앞쪽으로 탐색
    for i in range(len(levels) - 2, -1, -1):
        if levels[i] >= levels[i + 1]:
            # 현재 레벨의 점수가 다음 레벨의 점수보다 크거나 같으면 감소시킴
            decreases += (levels[i] - levels[i + 1] + 1)
            levels[i] = levels[i + 1] - 1
    
    return decreases

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    levels = [int(data[i]) for i in range(1, n + 1)]
    
    result = minimum_decreases(levels)
    print(result)

if __name__ == "__main__":
    main()
