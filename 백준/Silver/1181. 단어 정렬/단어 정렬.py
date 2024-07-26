import sys
input = sys.stdin.read

# 입력 받기
data = input().split()
n = int(data[0])
words = data[1:]

# 중복 제거
unique_words = list(set(words))

# 정렬
unique_words.sort(key=lambda x: (len(x), x))

# 결과 출력
for word in unique_words:
    print(word)
