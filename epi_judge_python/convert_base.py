from test_framework import generic_test


def convert_base(num_as_string, b1, b2):

    if num_as_string[0] == '-':
        num_as_string = num_as_string[1:]
        convert_str = '-'
    else:
        convert_str = ''

    num_to_sym = {
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F'
    }

    sym_to_num = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
    }


    power = 0
    sum = 0
    for i in reversed(range(len(num_as_string))):
        if num_as_string[i] in sym_to_num:
            sum += sym_to_num[num_as_string[i]] * (b1 ** power)
        else:
                sum += int(num_as_string[i]) * (b1 ** power)
        power += 1

    max_power = 0
    while sum >= (b2 ** max_power):
        max_power += 1

    if max_power == 0:
        max_power = 1

    for i in reversed(range(max_power)):
        if sum >= (b2 ** i):

            digit = sum // (b2 ** i)
            sum -= digit * (b2 ** i)



            if digit > 9:
                digit = num_to_sym[str(digit)]
            convert_str += str(digit)
        else:
            convert_str += '0'

    return convert_str


print(convert_base("4",16,2))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
