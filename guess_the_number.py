import random

class NumberGuessGame:

    def __init__(self):
        #defining the range, chances.
        self.lower = 1
        self.higher = 100
        self.max_chances = 10

    #method to genarate the number
    def get_random_number(self):
        return random.randint(self.lower, self.higher)

    def start(self):
        chances = 0
        random_number = self.get_random_number()
        name = (input('Hi! What is your name?'))

        print(f"okay! {name} I have a number between {self.lower} and {self.higher}\n and you have  {self.max_chances} chances to guess.")
        #heart of the game!!
        while True:
            user_number = int(input('enter the number you guessed : '))

            if user_number == random_number:
                print(f"hyrray {name}! You got it in {chances + 1} step{'s' if chances > 1 else ''}!")
                break
            elif chances == self.max_chances:
                print(f'Oh Ohh..! {name} You lost the game. You are out of chances!!')

            elif user_number < random_number:
                print('-> your have to guess higher number!!')
        
            else:
                print("you need to guess lower number!")
            chances += 1

game = NumberGuessGame()
game.start()