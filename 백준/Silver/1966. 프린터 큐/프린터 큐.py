from collections import deque
import sys
input = sys.stdin.read

data = input().split()
num_tests = int(data[0])
index = 1

results = []

for _ in range(num_tests):
    n = int(data[index])
    m = int(data[index + 1])
    priorities = list(map(int, data[index + 2: index + 2 + n]))
    index += 2 + n
    
    queue = deque([(priority, idx) for idx, priority in enumerate(priorities)])
    count = 0
    
    while queue:
        current = queue.popleft()
        if any(current[0] < item[0] for item in queue):
            queue.append(current)
        else:
            count += 1
            if current[1] == m:
                results.append(count)
                break

for result in results:
    print(result)
