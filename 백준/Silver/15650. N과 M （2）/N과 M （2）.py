from itertools import combinations

def solve_problem(n, m):
    comb = combinations(range(1, n + 1), m)
    comb_list = []
    for c in comb:
        comb_list.append(' '.join(map(str, c)))
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
