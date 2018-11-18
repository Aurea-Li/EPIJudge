from test_framework import generic_test


def convert_to_int(c):
    return ord(c) - 64

def ss_decode_col_id(col):

    sum, power = 0, len(col)-1
    for c in col:
        sum += convert_to_int(c) * 26 ** power
        power -= 1

    return sum



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spreadsheet_encoding.py",
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
