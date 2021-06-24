import random

rps_choice_list = ['Rock', 'Paper', 'Scissor']

your_choice = input('Choice your RPS: ')

computer_random_choice = random.choice(rps_choice_list)

if computer_random_choice == 'Rock' and your_choice == 'Rock':
    print('Draw')
else:
    print('Computer choice is not same as yours')

print(f'Computer choice was {computer_random_choice}')