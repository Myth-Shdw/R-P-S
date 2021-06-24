from stuff import *
from error import error_message

def rps():
    if your_choice in rps_choice:
        if your_choice == 'rock' and computer_choice == 'scissor':
            print('You Won')
        elif your_choice == 'paper' and computer_choice == 'rock':
            print('You Won')
        elif your_choice == 'scissor' and computer_choice == 'paper':
            print('You Won')
        elif computer_choice == 'rock' and your_choice == 'scissor':
            print('You Lose')
        elif computer_choice == 'paper' and your_choice == 'rock':
            print('You Lose')
        elif computer_choice == 'scissor' and your_choice == 'paper':
            print('You Lose')
        elif your_choice == computer_choice:
            print('Draw')
        print(f'Your choice was {your_choice}')
        print(f'Computer choice was {computer_choice}')
    else:
        print(error_message())
        
def run():
    rps()