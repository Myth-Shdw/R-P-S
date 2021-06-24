import random

rps_choice_list = ['Rock', 'Paper', 'Scissor']

your_choice = input('Choice your RPS: ')

your_choice = your_choice.lower()

computer_random_choice = random.choice(rps_choice_list)

computer_random_choice = computer_random_choice.lower()

if computer_random_choice == 'rock' and your_choice == 'rock':
    print('Draw')
else:
    print('Computer choice is not same as yours')

print(f'Computer choice was {computer_random_choice}')