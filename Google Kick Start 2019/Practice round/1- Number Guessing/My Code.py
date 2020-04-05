import sys


def solve(a, b):
    middle = (a + b) // 2
    print(middle)
    sys.stdout.flush()
    g_answer = input()
    if g_answer == "CORRECT":
        return
    elif g_answer == "TOO_SMALL":
        a = middle + 1
    else:
        b = middle - 1
    solve(a, b)


T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    _ = int(input())
    solve(a + 1, b)

