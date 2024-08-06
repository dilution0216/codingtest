def count_occurrences(document, word):
    count = 0  # 단어가 중복되지 않게 등장하는 횟수
    index = 0  # 문서에서 탐색 중인 현재 위치
    word_length = len(word)  # 찾으려는 단어의 길이

    while index <= len(document) - word_length:
        # 현재 위치에서 단어의 길이만큼의 부분 문자열이 찾으려는 단어와 같은지 확인
        if document[index:index + word_length] == word:
            count += 1  # 단어가 발견되면 횟수 증가
            index += word_length  # 단어의 길이만큼 건너뜀
        else:
            index += 1  # 그렇지 않으면 한 칸씩 이동

    return count  # 최종적으로 단어가 등장한 횟수를 반환

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    document = data[0]  # 첫 번째 줄은 문서
    word = data[1]  # 두 번째 줄은 찾으려는 단어
    
    result = count_occurrences(document, word)
    print(result)

if __name__ == "__main__":
    main()
