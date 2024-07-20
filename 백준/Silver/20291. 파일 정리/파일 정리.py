import sys

input = sys.stdin.readline

def solution():
    n = int(input().strip())  # 파일의 수를 입력받습니다.
    ext_count = {}  # 확장자의 개수를 저장할 딕셔너리입니다.
    
    # 파일의 수만큼 반복
    for _ in range(n):
        file_name = input().strip()  # 파일 이름을 입력받습니다.
        ext = file_name.split('.')[-1]  # 파일 이름에서 확장자를 추출합니다.
        
        # 확장자를 딕셔너리에 추가하거나 개수를 증가시킵니다.
        if ext in ext_count:
            ext_count[ext] += 1
        else:
            ext_count[ext] = 1
    
    # 확장자를 사전 순으로 정렬하여 출력합니다.
    sorted_ext = sorted(ext_count.items())
    result = "\n".join(f"{ext} {count}" for ext, count in sorted_ext)
    return result

if __name__ == "__main__":
    print(solution())
