def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])  # 숫자 카드의 개수
    cards = set(map(int, data[1:n + 1]))  # 숫자 카드 목록을 집합으로 저장
    
    m = int(data[n + 1])  # 확인할 숫자의 개수
    targets = list(map(int, data[n + 2:]))  # 확인할 숫자 목록
    
    result = []
    for target in targets:
        if target in cards:
            result.append('1')  # 숫자 카드가 있으면 1
        else:
            result.append('0')  # 숫자 카드가 없으면 0
    
    print(' '.join(result))  # 결과를 공백으로 구분해 출력

if __name__ == "__main__":
    main()
