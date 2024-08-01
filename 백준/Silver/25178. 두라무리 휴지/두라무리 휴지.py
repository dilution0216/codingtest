def remove_vowels(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return ''.join([char for char in word if char not in vowels])

def check_duramari_effect(word1, word2):
    # 첫 글자와 마지막 글자가 동일한지 확인
    if word1[0] != word2[0] or word1[-1] != word2[-1]:
        return "NO"
    
    # 모음을 제거한 후 비교
    stripped_word1 = remove_vowels(word1)
    stripped_word2 = remove_vowels(word2)
    
    if stripped_word1 != stripped_word2:
        return "NO"
    
    # 두 문자열의 문자 빈도가 같은지 확인
    if sorted(word1) != sorted(word2):
        return "NO"
    
    return "YES"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    word1 = data[1]
    word2 = data[2]
    
    result = check_duramari_effect(word1, word2)
    print(result)

if __name__ == "__main__":
    main()