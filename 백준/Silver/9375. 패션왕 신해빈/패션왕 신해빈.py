def solve():
    import sys
    input = sys.stdin.readline

    T = int(input().strip())  # 테스트 케이스 수
    results = []

    for _ in range(T):
        n = int(input().strip())
        clothes = {}

        for _ in range(n):
            name, kind = input().strip().split()
            if kind in clothes:
                clothes[kind] += 1
            else:
                clothes[kind] = 1

        combinations = 1
        for kind in clothes:
            combinations *= (clothes[kind] + 1)  # 해당 종류의 옷을 입지 않는 경우 포함

        results.append(combinations - 1)  # 아무것도 입지 않는 경우 제외

    for result in results:
        print(result)

if __name__ == "__main__":
    solve()
