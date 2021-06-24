import random

rps_choice = ['rock', 'paper', 'scissor']

your_choice = input('Choice from Rock/Paper/Scissor: ').lower()

computer_choice = random.choice(rps_choice)