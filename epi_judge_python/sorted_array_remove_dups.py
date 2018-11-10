import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Returns the number of valid entries after deletion.
def delete_duplicates(A):

    swap = len(A)+1

    if len(A) < 2:
        return len(A)

    for i in range(1, len(A)):
        if swap == len(A)+1:
            if A[i-1] == A[i]:
                swap = i
        else:
            if A[(swap)-1] != A[i]:
                A[swap], A[i] = A[i], A[swap]

                swap += 1

    return len(A[:swap])


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_array_remove_dups.py",
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
