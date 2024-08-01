def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    MAX_HEIGHT = 256
    MIN_HEIGHT = 0
    N = int(data[0])  # 땅의 세로 크기
    M = int(data[1])  # 땅의 가로 크기
    B = int(data[2])  # 인벤토리 블록의 수
    
    ground = []
    index = 3
    for i in range(N):
        row = []
        for j in range(M):
            row.append(int(data[index + j]))
        ground.append(row)
        index += M
    
    height_cnt = [0 for _ in range(MAX_HEIGHT + 1)]
    answer_cost = float('inf')
    answer_height = 0
    sum_height = B

    # 각 높이의 개수를 저장하는 리스트 입력받기
    for row in ground:
        for val in row:
            height_cnt[val] += 1
            sum_height += val
    
    # 가능한 높이값들을 저장
    min_h = min(map(min, ground))
    max_h = sum_height // (N * M)

    # 각 높이를 평탄화 하는데 걸리는 시간 탐색
    for h in range(min_h, max_h + 1):
        cost = 0
        usable_blocks = B
        for i in range(MIN_HEIGHT, MAX_HEIGHT + 1):
            if h < i:
                cost += height_cnt[i] * (i - h) * 2
                usable_blocks += height_cnt[i] * (i - h)
            else:
                cost += height_cnt[i] * (h - i)
                usable_blocks -= height_cnt[i] * (h - i)

        if usable_blocks >= 0 and cost <= answer_cost:
            answer_cost = cost
            answer_height = h

    print(answer_cost, answer_height)

if __name__ == "__main__":
    main()
