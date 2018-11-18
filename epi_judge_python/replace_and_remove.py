import functools
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):


    i, next_char, final_size = 0, 0, size

    for i in range(size):


        if s[i] == 'b':
            final_size -= 1
        elif s[i] == 'a':
            final_size += 1
            s[next_char] = s[i]
            next_char += 1
        else:
            s[next_char] = s[i]
            next_char += 1


    array_pt = final_size - 1
    for i in reversed(range(next_char)):
        if s[i] == 'a':
            s[array_pt] = 'd'
            s[array_pt - 1] = 'd'
            array_pt -= 2
        else:
            s[array_pt] = s[i]
            array_pt -= 1

    return final_size








@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
