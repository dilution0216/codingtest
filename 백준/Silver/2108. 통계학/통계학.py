import sys
from collections import Counter

def calculate_statistics(numbers):
    # 산술 평균 계산
    arithmetic_mean = round(sum(numbers) / len(numbers))
    
    # 중앙값 계산
    numbers.sort()
    median = numbers[len(numbers) // 2]
    
    # 최빈값 계산
    count = Counter(numbers).most_common()
    if len(count) > 1 and count[0][1] == count[1][1]:
        mode = count[1][0]
    else:
        mode = count[0][0]
    
    # 범위 계산
    range_value = numbers[-1] - numbers[0]
    
    return arithmetic_mean, median, mode, range_value

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    numbers = [int(data[i]) for i in range(1, n + 1)]
    
    arithmetic_mean, median, mode, range_value = calculate_statistics(numbers)
    
    print(arithmetic_mean)
    print(median)
    print(mode)
    print(range_value)

if __name__ == "__main__":
    main()
