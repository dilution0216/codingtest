from collections import Counter
import sys

input = sys.stdin.readline

def solution():
    word = input().strip()  # 표준 입력에서 한 줄을 읽어와서 공백을 제거
    
    # 대문자로 변환
    word = word.upper()
    
    # 각 알파벳 등장 횟수 세기
    counter = Counter(word)
    
    # 가장 많이 등장한 횟수를 max_c에 저장
    max_c = max(counter.values())
    
    # 가장 많이 등장한 알파벳
    most_f = []  # 리스트 초기화
    
    # Counter 객체의 모든 알파벳, 횟수 쌍을 반복
    for key, value in counter.items():
        # 현재 알파벳 등장 횟수가 max_c와 같다면
        if value == max_c:
            most_f.append(key)  # most_f 리스트에 저장
    
    # 가장 많이 등장한 알파벳의 개수 확인
    if len(most_f) > 1:
        return "?"
    else:
        return most_f[0]

if __name__ == "__main__":
    print(solution())
