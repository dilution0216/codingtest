import sys
input = sys.stdin.read

def solve_problem():
    
    data = input().strip().split()
    
    a1 = int(data[0])
    a0 = int(data[1])
    c = int(data[2])
    n0 = int(data[3])
    
    if a1 > c:
        print(0)
    else:
        if a1 * n0 + a0 <= c * n0:
            print(1)
        else:
            print(0)

if __name__ == "__main__":
    solve_problem()
