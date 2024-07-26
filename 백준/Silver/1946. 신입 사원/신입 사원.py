import sys
input = sys.stdin.read

data = input().split()
t = int(data[0])
index = 1

results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    applicants = []

    for i in range(n):
        doc, interview = int(data[index]), int(data[index + 1])
        applicants.append((doc, interview))
        index += 2

    # 서류 성적 기준으로 오름차순 정렬
    applicants.sort()

    # 최소 면접 성적을 현재 최대값으로 초기화
    min_interview = applicants[0][1]
    count = 1  # 첫 번째 지원자는 무조건 선발

    # 두 번째 지원자부터 확인
    for i in range(1, n):
        if applicants[i][1] < min_interview:
            min_interview = applicants[i][1]
            count += 1

    results.append(count)


for result in results:
    print(result)
