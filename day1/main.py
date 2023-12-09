import math
import re

LITERALS = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]


def find_numbers(inp: str):
    found_numbers = []
    print('Reading', inp)
    for char_i in range(0, len(inp)):
        if inp[char_i].isnumeric():
            print('Number at', char_i, 'is', inp[char_i])
            found_numbers.append(int(inp[char_i]))
        else:
            for var_i in range(0, len(LITERALS)):
                substr = inp[char_i:]
                hit = substr.startswith(LITERALS[var_i])
                if hit:
                    print('Word at', char_i, 'is', var_i)
                    found_numbers.append(var_i)
    return found_numbers


if __name__ == '__main__':
    total = 0
    for line in open('input.txt', 'r'):
        lowerline = line.rstrip().lower()
        numbers = find_numbers(lowerline)

        first = numbers[0]
        last = numbers[-1]
        res = str(first) + str(last)
        total += int(res)
        # print("\t", res, "\n", total)
        print('({lowerline} -> {parseline}) -> ({first} + {last} -> {res}) -> {total}'.format(lowerline=lowerline, parseline=numbers, first=first, last=last, res=res, total=total))
    print('Total =', total)

