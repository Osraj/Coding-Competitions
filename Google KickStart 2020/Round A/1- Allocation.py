"""
## A Possible Solution

# T = int (input())
# for t in range(1, T+1):
# 	n, b = [int(_) for _ in input().split()]
# 	arr = sorted([int(_) for _ in input().split()])
# 	res = 0
# 	for a in arr:
# 		if a <= b:
# 			b -= a
# 			res += 1
# 		else:
# 			break
# 	print ("Case #{}: {}".format(t, res))
"""


import sys


def solve(li, B):
    houses = 0
    B = int(B)
    for cost in li:
        if B < int(cost):
            return houses
        else:
            houses += 1
            B -= int(cost)
    return houses


# ---------------------------------------------
T = int(input())

cases = 0
for _ in range(T):
    cases += 1
    N, B = map(int, input().split())

    # making the numbers workable
    l = input()
    c = list(l.split())
    d = list(map(int, c))

    print ( "Case #" + str(cases) + ": " + str(solve(d, B)) )






