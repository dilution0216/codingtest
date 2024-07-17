import sys

def solution():
    input = sys.stdin.read
    data = input().strip().split()
    
    # 첫 번째 값은 1m^2당 자라는 참외의 개수
    chamoe_per_sqm = int(data[0])
    
    # 방향과 길이를 저장할 리스트
    directions_lengths = []
    for i in range(1, len(data), 2):
        direction = int(data[i])
        length = int(data[i+1])
        directions_lengths.append((direction, length))
    
    # 가장 긴 변과 그 다음 긴 변을 찾는다.
    max_width = 0
    max_height = 0
    width_index = -1
    height_index = -1
    
    for i in range(len(directions_lengths)):
        direction, length = directions_lengths[i]
        if direction in (1, 2):  # 동, 서 방향
            if length > max_width:
                max_width = length
                width_index = i
        else:  # 남, 북 방향
            if length > max_height:
                max_height = length
                height_index = i
    
    # 작은 직사각형의 가로, 세로 길이를 계산
    small_width = abs(directions_lengths[(width_index - 1) % 6][1] - directions_lengths[(width_index + 1) % 6][1])
    small_height = abs(directions_lengths[(height_index - 1) % 6][1] - directions_lengths[(height_index + 1) % 6][1])
    
    # 총 면적에서 작은 직사각형의 면적을 뺀다.
    large_area = max_width * max_height
    small_area = small_width * small_height
    total_area = large_area - small_area
    
    # 참외의 개수 계산
    chamoe_count = total_area * chamoe_per_sqm
    
    # 결과 반환
    return chamoe_count

if __name__ == "__main__":
    print(solution())
