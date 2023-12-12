import re

def run(target_file):
    working_dir = "/".join(__file__.split('/')[:-1])
    with open(f'{working_dir}/{target_file}', 'r') as file:
        cards = file.readlines()
        i = 0
        while i < len(cards):

            card = cards[i]
            cardId = int(re.search(r'Card *(\d+):', card).group(1))


            nums = card.strip().split(':')[1]
            winning_nums = list(filter(len, nums.split('|')[0].split(' ')))
            selected_nums = list(filter(len, nums.split('|')[1].split(' ')))

            match_count = 0
            for s_num in selected_nums:
                if s_num in winning_nums:
                    match_count += 1
            
            if match_count > 0:
                cards.extend(cards[cardId:cardId + match_count])

            print(f'Card {cardId}: {match_count}')

            i += 1

        print(len(cards))
    return len(cards)

if __name__ == '__main__':
    real_filename = 'input.txt'
    test_filename = 'test1.txt'
    expected = 30

    actual = run(test_filename)
    assert actual == expected, f'Expected {actual} to equal {expected}'

    print(run(real_filename))