
with open('input.txt', 'r') as file:
    data = file.read().split('\n')

print(data)

sum = 0
for card in data:
    your_nums = card.split('|')[1]
    your_nums = ' '.join(your_nums.split()).split(' ')
    print(your_nums)

    winning_nums = card.split('|')[0].split(':')[1]
    winning_nums = ' '.join(winning_nums.split()).split(' ')
    print(winning_nums)

    num_of_match = 0
    for num in your_nums:
        if num in winning_nums:
            print('You win!')
            num_of_match += 1

    print(f'You matched {num_of_match} numbers')
    if num_of_match > 0:
        sum += 2 ** (num_of_match-1)

print(f'You matched {sum} numbers in total')