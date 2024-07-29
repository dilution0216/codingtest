import sys
input = sys.stdin.read

# 초기 문자열과 명령어 입력 받기
data = input().splitlines()
initial_string = data[0]
commands = data[1:]

# 왼쪽 스택과 오른쪽 스택 사용
left_stack = list(initial_string)  # 초기 문자열을 왼쪽 스택에 넣음
right_stack = []

# 명령어 처리
for command in commands:
    if command.startswith('L'):
        if left_stack:
            right_stack.append(left_stack.pop())  # 왼쪽 스택에서 오른쪽 스택으로 이동
    elif command.startswith('D'):
        if right_stack:
            left_stack.append(right_stack.pop())  # 오른쪽 스택에서 왼쪽 스택으로 이동
    elif command.startswith('B'):
        if left_stack:
            left_stack.pop()  # 왼쪽 스택에서 삭제
    elif command.startswith('P'):
        left_stack.append(command.split()[1])  # 왼쪽 스택에 추가

# 최종 문자열 합치기
final_string = ''.join(left_stack + right_stack[::-1])
print(final_string)
