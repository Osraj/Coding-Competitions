import numpy as np


def counter(m):
    _, counts = np.unique(m, return_counts=True)
    return max(counts)


num_of_tests = int(input())
for case in range(1, num_of_tests + 1):
    N = int(input())
    L = [input().split() for _ in range(N)]
    M = np.array(L).astype('int64')
    ans_trace = np.trace(M)
    row_repeats = np.apply_along_axis(counter, axis=1, arr=M)
    col_repeats = np.apply_along_axis(counter, axis=0, arr=M)
    row_repeats = sum(row_repeats > 1)
    col_repeats = sum(col_repeats > 1)

    print(f'Case #{case}: {ans_trace} {row_repeats} {col_repeats}')