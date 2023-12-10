if __name__ == '__main__':
    TARGET = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    COLORS = TARGET.keys()
    validRounds = []

    with open('day2/input.txt', 'r') as file:
        for line in file:
            gameAndRounds = line.strip().split(':')
            gameId = int(gameAndRounds[0].replace('Game ', ''))
            gameIsValid = True
            print(f'gameId is {gameId}')

            rounds = gameAndRounds[1].split(';')
            for round in rounds:
                for dice in round.strip().split(','):
                    for color in COLORS:
                        if color in dice and int(dice.strip().split(' ')[0]) > TARGET[color]:
                            print(f'Game {gameId} invalidated by {color}={int(dice.strip().split(" ")[0])}')
                            gameIsValid = False

            if gameIsValid:
                print('Round', gameId, 'is valid.')
                validRounds.append(gameId)

    print(sum(validRounds))

