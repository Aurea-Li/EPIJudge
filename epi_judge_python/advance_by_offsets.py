from test_framework import generic_test

def can_reach_end(A):
    threshold = 1

    for i in reversed(range(len(A)-1)):
        if A[i] >= threshold:
            threshold = 1
        else:
            threshold += 1

    if threshold == 1:
        return True
    else:
        return False



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
