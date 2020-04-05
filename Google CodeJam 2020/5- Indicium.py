

answers = []
num_of_tests = int(input())
for case in range(1, num_of_tests + 1):
    num = []
    # N, B = map(int, input().split())
    N = input()
    for i in range(N):
        num.append(i * N)
    num.append((N(N+1)/2))


    if B in num:
        print("Possible")
    else:
        print("Impossible")