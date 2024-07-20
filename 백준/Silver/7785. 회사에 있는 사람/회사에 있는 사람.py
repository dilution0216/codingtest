import sys

input = sys.stdin.readline

def solution():
    n = int(input().strip())  # 기록의 수를 입력받습니다.
    people = set()  # 현재 회사에 있는 사람들의 이름을 저장할 집합입니다.
    
    for _ in range(n):
        name, status = input().strip().split()  # 이름과 상태를 입력받습니다.
        if status == "enter":
            people.add(name)  # 출근한 경우 이름을 집합에 추가합니다.
        elif status == "leave":
            people.discard(name)  # 퇴근한 경우 이름을 집합에서 제거합니다.
    
    # 회사에 남아 있는 사람들의 이름을 사전 역순으로 정렬하여 준비합니다.
    result = sorted(people, reverse=True)
    return "\n".join(result)  # 정렬된 이름들을 하나의 문자열로 반환합니다.

if __name__ == "__main__":
    print(solution())
