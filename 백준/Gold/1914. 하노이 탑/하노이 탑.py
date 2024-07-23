import sys
input = sys.stdin.readline

def hanoi(n, start, mid, end):
    if n == 1:
        print(start, end)
    else:
        hanoi(n-1, start, end, mid)
        print(start, end)
        hanoi(n-1, mid, start, end)

def main():

    N = int(input().strip())

    # 이동 횟수 계산
    moves = (1 << N) - 1
    print(moves)

    # N이 20 이하일 때만 이동 순서를 출력
    if N <= 20:
        hanoi(N, 1, 2, 3)

if __name__ == "__main__":
    main()
