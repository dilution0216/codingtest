import sys
input = sys.stdin.readline

# 오목판 입력
board = []
for _ in range(19):
    board.append(list(map(int, input().split())))

# 방향 벡터 (오른쪽, 아래, 오른쪽 아래 대각선, 오른쪽 위 대각선)
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if board[x][y] != 0:
            current_color = board[x][y]

            for direction in range(4):
                count = 1
                nx, ny = x + dx[direction], y + dy[direction]

                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == current_color:
                    count += 1
                    if count == 5:
                        # 6목 체크
                        if 0 <= x - dx[direction] < 19 and 0 <= y - dy[direction] < 19 and board[x - dx[direction]][y - dy[direction]] == current_color:
                            break
                        if 0 <= nx + dx[direction] < 19 and 0 <= ny + dy[direction] < 19 and board[nx + dx[direction]][ny + dy[direction]] == current_color:
                            break
                        # 육목이 아니면 성공한 것이므로 종료
                        print(current_color)
                        print(x + 1, y + 1)
                        sys.exit(0)
                    nx += dx[direction]
                    ny += dy[direction]

print(0)
