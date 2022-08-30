from random import randint

import sys

low_limit = int(sys.argv[1])
top_limit = int(sys.argv[2])

hidden_number = randint(low_limit, top_limit)

counter = 1;
while True:
    try:
        guess = int(input(f"({low_limit} - {top_limit}) What's your guess? "))
        if low_limit <= guess <= top_limit:
            if hidden_number == guess:
                print(f"Congratulations, you guessed the number in {counter} attempt(s)!!")
                break
            else:
                print("Sorry. Try again.")
                counter += 1
        else:
            print(f"Please enter a number between {low_limit} and {top_limit}")
    except ValueError:
        print(f"Please enter a number between {low_limit} and {top_limit}")
