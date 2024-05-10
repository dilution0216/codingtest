def solution(my_string, overwrite_string, s):
    s = int(s)
    t = len(overwrite_string)
    answer = my_string[:s] + overwrite_string + my_string[s+t:]
    return answer