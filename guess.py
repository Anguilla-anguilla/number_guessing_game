
from random import randint
from time import sleep


class HighScore():
    def __init__(self):
        self.easy_score = []
        self.medium_score = []
        self.hard_score = []

    def add_score(self, score, level):
        if level == 1:
            self.easy_score.append(score)
        elif level == 2:
            self.medium_score.append(score)
        elif level == 3:
            self.hard_score.append(score)

    def show_high_score(self):
        if len(self.easy_score) != 0:
            print(f'Easy level: {min(self.easy_score)}')
        else:
            print('Easy level: no scores')
        if len(self.medium_score) != 0:
            print(f'Medium level: {min(self.medium_score)}')
        else:
            print('Medium level: no scores')
        if len(self.hard_score) != 0:
            print(f'Hard level: {min(self.hard_score)}')
        else:
            print('Hard level: no scores')


def welcome():
    print('Welcome to the Number Guessing Game!')
    print('')
    sleep(1)
    print('Try to guess a randomly generated number between 1 and 100')
    print('You can choose a level with a varying number of attempts to guess')
    print('the correct number.')
    print('')
    sleep(3)
    print('Easy:')
    print('Attempts: 15')
    print('A good starting point for beginners.')
    print('')
    sleep(3)
    print('Medium:')
    print('Attempts: 10')
    print('A balanced level for intermediate players.')
    print('')
    sleep(3)
    print('Hard:')
    print('Attempts: 5')
    print('A challenging level for experienced players.')
    print('')
    sleep(3)


def level():
    while True:
        print('Choose a level:')
        print('1. Easy')
        print('2. Medium')
        print('3. Hard')
        choice = int(input('Enter your choice:'))
        print('')
        if choice in range(1, 4):
            return choice
        print('Wrong choice!')


def attempts(choice):
    if choice == 1:
        attempts = 15
    elif choice == 2:
        attempts = 10
    elif choice == 3:
        attempts = 5
    print(f'OK! You have {attempts} attempts.')
    return attempts


def hint(random):
    if random < 10:
        low = 0
    if random > 90:
        high = 100
    else:
        low = random + randint(0, 6)
        high = random - randint(0, 6)
    print(f'The number is between {low} and {high}.')


def game(attempts):
    print("Let's start!")
    random = randint(1, 101)
    print(random)
    n = 0
    while attempts > 0:
        try:
            guess = int(input('Enter your choice:'))
            print('')
            n += 1
            attempts -= 1
            if guess == random:
                print('Congratulations! Your choice is correct!')
                print(f'Number of attempts: {n}')
                print('')
                return True, random, n
            elif guess < random:
                print('The number is greater than the guess.')
                print(f'{attempts} attempts left.')
                print('')
            elif guess > random:
                print('The number is less than the guess.')
                print(f'{attempts} attempts left.')
                print('')
            else:
                return False
        except ValueError:
            print('Invalid input! Please enter a number.')
            
        
        if n == 7:
            y = input("Press 'y' if you want a hint or anything else if not:")
            if y == 'y':
                hint(random)
            
    return False, random, n


def main():
    high_score = HighScore()
    quit_game = False
    # welcome()
    while not quit_game:
        choice = level()
        attempts_count = attempts(choice)
        game_result, rand_numb, number_of_attempts = game(attempts_count)
        if not game_result:
            print('No attempts left.')
            print(f'The correct number was {rand_numb}.')
            print('')
        else:
            high_score.add_score(score=number_of_attempts, level=choice)
            print('High scores:')
            high_score.show_high_score()
            print('')

        print('Would you like to play again?')
        quit = input('Press "q" to quit or anything else to continue:')
        print('')
        if quit == 'q':
            print('Thanks for playing!')
            quit_game = True


if __name__ == '__main__':
    main()
