from collections import Counter

def count_words(word):
    return Counter(word)

def remove_nouns_from_word(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return "".join([w for w in list(word) if w not in vowels])

def duramuri_huji(word1, word2):
    answer = "NO"
    cnt1, cnt2 = count_words(word1), count_words(word2)
    
    word1_non_vowel = remove_nouns_from_word(word1)
    word2_non_vowel = remove_nouns_from_word(word2)
    
    condition1 = cnt1 == cnt2
    condition2 = (word1[0] == word2[0]) and (word1[-1] == word2[-1])
    condition3 = word1_non_vowel == word2_non_vowel
    
    if condition1 and condition2 and condition3:
        answer = "YES"
        
    return answer

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    word1 = data[1]
    word2 = data[2]
    
    print(duramuri_huji(word1, word2))
