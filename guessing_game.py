import random

def guessing_game():
    secret_num = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input ("Enter a number from 1 - 100: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
            elif guess < secret_num:
                print ("Guess is too low.")
            elif guess > secret_num:
                print ("Guess is too high.")
            else:
                print (f"Contradulations, you guessed the number {secret_num} in {attempts} attempts.")
                break
        except ValueError:
            print ("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    guessing_game()