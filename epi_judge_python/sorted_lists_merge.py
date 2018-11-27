from test_framework import generic_test
from list_node import ListNode

def merge_two_sorted_lists(L1, L2):

    if not L1:
        return L2
    if not L2:
        return L1

    dummy_head = current_node = ListNode()

    L1_pointer, L2_pointer = L1, L2

    while min(L1_pointer.data , L2_pointer.data) < float("inf"):

        if L1_pointer.data < L2_pointer.data:
            current_node.next = L1_pointer

            if L1_pointer.next:
                L1_pointer = L1_pointer.next
            else:
                L1_pointer = ListNode(float("inf"))

        else:
            current_node.next = L2_pointer

            if L2_pointer.next:
                L2_pointer = L2_pointer.next
            else:
                L2_pointer = ListNode(float("inf"))

        current_node = current_node.next

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
