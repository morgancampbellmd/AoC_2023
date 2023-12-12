if __name__ == '__main__':
    working_dir = "/".join(__file__.split('/')[:-1])
    filename = 'input.txt'

    with open(f'{working_dir}/{filename}', 'r') as file:
        total = 0
        for i, card in enumerate(file):
            nums = card.strip().split(':')[1]
            winning_nums = list(filter(len, nums.split('|')[0].split(' ')))
            selected_nums = list(filter(len, nums.split('|')[1].split(' ')))

            match_count = 0
            for s_num in selected_nums:
                if s_num in winning_nums:
                    match_count += 1
            card_score = 0 if match_count < 1 else 2 ** (match_count - 1)
            total += card_score
            print(f'Card {i + 1} score: {card_score} ({match_count})')

        print(total)