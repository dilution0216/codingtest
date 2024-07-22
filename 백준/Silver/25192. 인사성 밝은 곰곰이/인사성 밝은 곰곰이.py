def solve_problem():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    n = int(data[0])
    chat_logs = data[1:]
    
    unique_users = set()
    total_gomgom_count = 0

    for line in chat_logs:
        if line == "ENTER":
            unique_users.clear()
        elif line not in unique_users:
            unique_users.add(line)
            total_gomgom_count += 1
    
    print(total_gomgom_count)

if __name__ == "__main__":
    solve_problem()
