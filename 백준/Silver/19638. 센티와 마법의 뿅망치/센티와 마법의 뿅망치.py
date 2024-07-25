import heapq
import sys
input = sys.stdin.readline


def solve(n, h, t, giants):
    max_heap = [-giant for giant in giants]
    heapq.heapify(max_heap)
    
    count = 0
    for _ in range(t):
        largest = -heapq.heappop(max_heap)
        if largest < h:
            heapq.heappush(max_heap, -largest)
            print("YES")
            print(count)
            return
        if largest == 1:
            heapq.heappush(max_heap, -largest)
            break
        largest //= 2
        heapq.heappush(max_heap, -largest)
        count += 1

    maxV = -max_heap[0]
    if maxV < h:
        print("YES")
        print(count)
    else:
        print("NO")
        print(maxV)

n, h, t = map(int, input().split())
giants = [int(input()) for _ in range(n)]

solve(n, h, t, giants)
