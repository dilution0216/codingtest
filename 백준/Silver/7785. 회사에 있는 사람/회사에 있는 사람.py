import sys
input = sys.stdin.readline

def solution():
    # 출입 기록된 수를 입력
    n = int(input().strip())
    # 현재 회사에 있는 사람의 이름을 저장
    people = set()
    
    # 기록의 수만큼 반복
    for _ in range(n):
        # 이름과 상태 입력
        name, status = input().strip().split()
        if status == "enter":
            people.add(name)  # 출근한 경우 이름을 집합에 추가
        elif status == "leave":
            people.discard(name)  # 퇴근한 경우 이름을 집합에서 제거
    
    # 회사에 있는 사람 역순 정렬
    result = sorted(people, reverse=True)
    return "\n".join(result)

if __name__ == "__main__":
    print(solution())