def create_card_string(n, cards):
    result = [cards[0]]  # 첫 번째 카드는 무조건 첫 번째 위치에 놓음
    
    for i in range(1, n):
        if cards[i] <= result[0]:
            result.insert(0, cards[i])  # 카드가 현재 문자열의 첫 번째 문자보다 작거나 같으면 앞에 추가
        else:
            result.append(cards[i])  # 그렇지 않으면 뒤에 추가
    
    return ''.join(result)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    results = []
    for _ in range(t):
        n = int(data[index])
        cards = data[index+1:index+n+1]
        index += n + 1
        result = create_card_string(n, cards)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()