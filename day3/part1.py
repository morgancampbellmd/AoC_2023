import re

def clamp(low: int, val: int, high: int):
    return max(low, min(val, high))

def scanline(line: str, index: int, iter: 1 | -1 | 0, acc: list[str]) -> str:
    if 0 <= index <= len(line) - 1:
        char = line[index]
        if char.isnumeric():
            acc.append(char) if iter > 0 else acc.insert(0, char)
            if iter != 0 and 0 < index < len(line) - 1:
                scanline(line, index + iter, iter, acc)
    
    return ''.join(acc)



def search_grid(array2d: list[str], row: int, col: int):
    curr_line = array2d[row]
    prev_line = '' if row <= 0 else array2d[row - 1]
    next_line = '' if row >= len(array2d) - 1 else array2d[row + 1]

    to_int = lambda x: 0 if len(x) == 0 else int(x)


    top_left  = scanline(prev_line, col-1, -1, [])
    top       = scanline(prev_line, col, 0, [])
    top_right = scanline(prev_line, col+1, 1, [])

    left      = scanline(curr_line, col-1, -1, [])
    right     = scanline(curr_line, col+1, 1, [])

    bot_left  = scanline(next_line, col-1, -1, [])
    bot       = scanline(next_line, col, 0, [])
    bot_right = scanline(next_line, col+1, 1, [])

    if len(top) > 0:
        top_n = to_int(''.join([top_left, top, top_right]))
    else:
        top_n = to_int(top_left) + to_int(top_right)

    left_n = to_int(left)
    right_n = to_int(right)

    if len(bot) > 0:
        bot_n = to_int(''.join([bot_left, bot, bot_right]))
    else:
        bot_n = to_int(bot_left) + to_int(bot_right)

    sym = curr_line[col]
    print(f'{top_left}{top}{top_right}\n{left}{sym}{right}\n{bot_left}{bot}{bot_right}')

    return top_n + left_n + right_n + bot_n

if __name__ == '__main__':
    working_dir = "/".join(__file__.split('/')[:-1])

    filename = f'{working_dir}/input.txt'

    with open(filename, 'r') as file:
        array2d = file.readlines()
        height = len(array2d)
        total = 0
        for row, line  in enumerate(array2d):
            width = len(line)
            for col, char in enumerate(line.strip()):
                if not (char == '.' or char.isnumeric()):
                    total += search_grid(array2d, row, col)
        print(total)

                        
