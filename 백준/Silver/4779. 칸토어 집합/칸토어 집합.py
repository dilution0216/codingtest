def cantor_set(n):
    if n == 0:
        return "-"
    else:
        prev = cantor_set(n - 1)
        return prev + " " * len(prev) + prev

while True:
    try:
        n = int(input())
        print(cantor_set(n))
    except EOFError:
        break
