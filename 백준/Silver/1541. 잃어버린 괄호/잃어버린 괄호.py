def calculate_min_expression(expression):
    # '-'로 나눠서 분리
    parts = expression.split('-')
    
    # 첫 번째 부분은 무조건 더해야 한다
    first_part = sum(map(int, parts[0].split('+')))
    
    # 나머지 부분은 모두 뺀다
    total = first_part
    for part in parts[1:]:
        total -= sum(map(int, part.split('+')))
    
    return total

def main():
    import sys
    input = sys.stdin.read
    
    # 입력받은 수식
    expression = input().strip()
    
    # 최소값 계산
    result = calculate_min_expression(expression)
    
    # 결과 출력
    print(result)

if __name__ == "__main__":
    main()
