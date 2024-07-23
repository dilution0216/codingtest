# 입력 처리
n = int(input())  # 스위치의 개수
switches = list(map(int, input().split()))  # 스위치 상태
students_count = int(input())  # 학생 수
students = [tuple(map(int, input().split())) for _ in range(students_count)]  # 학생 정보

# 학생의 명령에 따른 스위치 상태 변경
for gender, number in students:
    if gender == 1:  # 남학생
        for i in range(number - 1, n, number):
            switches[i] = 1 - switches[i]
    elif gender == 2:  # 여학생
        left = right = number - 1
        while left >= 0 and right < n and switches[left] == switches[right]:
            switches[left] = 1 - switches[left]
            if left != right:  # 같은 스위치를 두 번 바꾸지 않도록
                switches[right] = 1 - switches[right]
            left -= 1
            right += 1

# 결과 출력 (20개씩 출력)
for i in range(0, n, 20):
    print(' '.join(map(str, switches[i:i+20])))