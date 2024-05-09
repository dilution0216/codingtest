str = input()
for char in str:
    if char.isupper():
        print(char.lower(), end='')
    if char.islower():
        print(char.upper(), end='')


# # 주어진 문자열 입력
# str = input()

# # 문자열을 한 글자씩 반복하여 처리
# for char in str:
#     # 대문자인 경우 소문자로 변환하여 출력
#     if char.isupper():
#         print(char.lower(), end='')
#     # 소문자인 경우 대문자로 변환하여 출력
#     elif char.islower():
#         print(char.upper(), end='')

# # 줄 바꿈
# print()
