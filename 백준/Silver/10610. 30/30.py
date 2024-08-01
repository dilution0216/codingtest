def main():
    import sys
    input = sys.stdin.read
    
    number = input().strip()
    
    # 숫자 중에 0이 하나도 없다면 30의 배수를 만들 수 없음
    if '0' not in number:
        print(-1)
        return
    
    # 숫자들의 합이 3의 배수가 아니라면 30의 배수를 만들 수 없음
    if sum(map(int, number)) % 3 != 0:
        print(-1)
        return
    
    # 숫자들을 내림차순으로 정렬하여 가장 큰 수를 만듦
    largest_number = ''.join(sorted(number, reverse=True))
    print(largest_number)

if __name__ == "__main__":
    main()
