if __name__ == '__main__':
    TARGET = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    COLORS = TARGET.keys()
    validRounds = []

    with open('day2/input.txt', 'r') as file:
        power = 0
        get_count = lambda x: int(x.strip().split(' ')[0])
        get_color = lambda x: x.strip().split(' ')[1]
        for line in file:
            gameAndRounds = line.strip().split(':')
            gameId = int(gameAndRounds[0].replace('Game ', ''))

            rounds = gameAndRounds[1].split(';')
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
            roundPower = red * green * blue
            print(f'red={red};green={green};blue={blue};power={roundPower}')
            power += roundPower

        print(power)

