import random

class GuessTheNumberGame:
    def __init__(self):
        self.target = random.randint(1, 100)
        self.attempts = 0

    def start(self):
        print("Welcome to the Guess the Number Game!")
        print("I have chosen a number between 1 and 100. Try to guess it.\n")

        for _ in range(1, 101):
            try:
                guess = int(input("Enter your guess: "))
                self.attempts += 1

                if guess == self.target:
                    print(f"Congratulations! You guessed the number in {self.attempts} attempts!")
                    break
                elif guess < self.target:
                    print("Try a higher number")
                else:
                    print("Try a lower number")

            except ValueError:
                print("Please enter a valid number!")

        else:
            print(f"Sorry, you're out of attempts. The number was: {self.target}")


game = GuessTheNumberGame()
game.start()
