from test_framework import generic_test


def merge_two_sorted_lists(L1, L2):

    L1_pt, L2_pt = L1, L2


    if L1_pt.data <= L2_pt.data:
        curr_least = L1
        head = L1
        L1_pt = L1_pt.next
    else:
        curr_least = L2
        head = L2


    while L1_pt != L2_pt:

        if L


    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
