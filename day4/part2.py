from enum import Enum

def clamp(low: int, val: int, high: int):
    return max(low, min(val, high))

def to_int(x: str):
    if len(x) == 0:
        return 0
    else:
        return int(x)

def scan(line: str, index: int, dir: -1 | 0 | 1, acc: list[str]) -> str:
    if 0 <= index <= len(line) - 1:
        char = line[index]
        if char.isnumeric():
            acc.append(char) if dir > 0 else acc.insert(0, char)
            if dir != 0 and 0 < index < len(line) - 1:
                scan(line, index + dir, dir, acc)
    
    return ''.join(acc)

def scanline(line: str, index: int) -> str:
    left  = scan(line, index, -1, [])
    cent  = scan(line, index, 0, [])
    right = scan(line, index, 1, [])

    return left, cent, right


def search_grid(array2d: list[str], row: int, col: int):
    curr_line = array2d[row]
    prev_line = '' if row <= 0 else array2d[row - 1]
    next_line = '' if row >= len(array2d) - 1 else array2d[row + 1]


    top_left, top, top_right       = scanline(prev_line, col)
    cur_left, nan, cur_right       = scanline(curr_line, col)
    bot_left, bot, bot_right       = scanline(next_line, col)

    if len(top) > 0:
        top_n = [to_int(''.join([top_left, top, top_right]))]
    else:
        top_n = [to_int(top_left), to_int(top_right)]

    left_n = [to_int(cur_left)]
    right_n = [to_int(cur_right)]

    if len(bot) > 0:
        bot_n = [to_int(''.join([bot_left, bot, bot_right]))]
    else:
        bot_n = [to_int(bot_left), to_int(bot_right)]

    parts = [*top_n, *left_n, *right_n, *bot_n]
    parts = list(filter(lambda x: x > 0, parts))
    return 0 if len(parts) != 2 else parts[0] * parts[1]

if __name__ == '__main__':
    working_dir = "/".join(__file__.split('/')[:-1])

    filename = f'{working_dir}/input.txt'

    with open(filename, 'r') as file:
        array2d = file.readlines()
        height = len(array2d)
        total = 0
        for row, line in enumerate(array2d):
            width = len(line)
            for col, char in enumerate(line.strip()):
                if not (char == '.' or char.isnumeric()):
                    total += search_grid(array2d, row, col)
        print(total)
