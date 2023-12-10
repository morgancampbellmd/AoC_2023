if __name__ == '__main__':
    working_dir = __file__.split('/')[:-1]

    filename = '/'.join(working_dir) + '/input.txt'
    with open(filename, 'r') as file:
        power = 0
        get_count = lambda x: int(x.strip().split(' ')[0])
        get_color = lambda x: x.strip().split(' ')[1]
        for line in file:
            game_and_rounds = line.strip().split(':')
            game_id = int(game_and_rounds[0].replace('Game ', ''))

            rounds = game_and_rounds[1].split(';')
            red = blue = green = int(0)
            for round in rounds:
                for dice in round.strip().split(','):
                    count = get_count(dice)
                    color = get_color(dice)

                    match color:
                        case 'red':
                            red = max(red, count)
                        case 'green':
                            green = max(green, count)
                        case 'blue':
                            blue = max(blue, count)
            round_power = red * green * blue
            print(f'red={red};green={green};blue={blue};power={round_power}')
            power += round_power

        print(power)