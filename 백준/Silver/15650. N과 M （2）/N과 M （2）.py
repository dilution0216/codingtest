from itertools import combinations

def solve_problem(n, m):
    comb = combinations(range(1, n + 1), m)
    comb_list = [' '.join(map(str, c)) for c in comb]
    return comb_list

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    
    results = solve_problem(n, m)

    for result in results:
        print(result)