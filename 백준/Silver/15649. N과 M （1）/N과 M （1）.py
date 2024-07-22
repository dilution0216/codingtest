from itertools import permutations

def solve_problem(n, m):
    perm = permutations(range(1, n + 1), m)
    perm_list = [' '.join(map(str, p)) for p in perm]
    return perm_list

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    
    results = solve_problem(n, m)

    for result in results:
        print(result)