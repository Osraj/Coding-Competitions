import numpy as np
from collections import Counter

def counter(m):
    _, counts = np.unique(m, return_counts=True)
    return max(counts)

answers = []
num_of_tests = int(input())
for case in range(1, num_of_tests + 1):
    N = int(input())
    lst = [input().split() for _ in range(N)]
    M = np.array(lst).astype('int64')
    k = np.trace(M)

    r = np.apply_along_axis(counter, axis=1, arr=M)
    c = np.apply_along_axis(counter, axis=0, arr=M)

    r = sum(r > 1)
    c = sum(c > 1)

    # print(f'Case #{case}: {k} {r} {c}')
    answers.append('Case #' + str(case) + ': ' + str(k) + ' ' + str(r) + ' ' + str(c))

for answer in answers:
    print(answer)

"""
1
3
2 1 3
1 3 2
1 2 3
"""


