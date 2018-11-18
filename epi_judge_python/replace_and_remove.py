import functools
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):

    i = 0
    while i < size:

        if s[i] == 'a':
            s[i] = 'd'
            s.insert(i, 'd')
            i +=  2
            size += 1
        elif s[i] == 'b':
            s.pop(i)
            size -= 1
        else:
            i += 1

    return size



@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
