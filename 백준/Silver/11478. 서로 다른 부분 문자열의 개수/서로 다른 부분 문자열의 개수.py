def count_unique_substrings(s):
    substrings = set()  # 부분 문자열을 저장할 집합
    
    # 모든 가능한 부분 문자열 생성
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.add(s[i:j])  # 부분 문자열을 집합에 추가
    
    return len(substrings)  # 고유한 부분 문자열의 개수 반환

# 입력 받기
if __name__ == "__main__":
    s = input().strip()
    print(count_unique_substrings(s))