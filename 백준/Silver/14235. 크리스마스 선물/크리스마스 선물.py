import heapq
import sys

input = sys.stdin.readline

def main():
    n = int(input().strip())  # 명령의 개수 N을 입력받음
    max_heap = []  # 빈 리스트를 최대 힙으로 사용
    
    for _ in range(n):
        command = list(map(int, input().strip().split()))
        
        if command[0] == 0:  # 선물을 받아야 하는 경우
            if max_heap:
                # 힙이 비어있지 않으면 가장 큰 선물 출력 후 제거
                print(-heapq.heappop(max_heap))
            else:
                # 힙이 비어있으면 -1 출력
                print(-1)
        else:
            # 산타가 선물을 추가하는 경우
            for gift in command[1:]:
                heapq.heappush(max_heap, -gift)  # 최대 힙을 유지하기 위해 음수로 변환하여 추가

if __name__ == "__main__":
    main()
