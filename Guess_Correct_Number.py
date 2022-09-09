import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 end {x}: "))
        if guess < random_number:
            print("sorry! guess again. too low.")
        elif guess > random_number:
            print("sorry! guess again. too high.")
    print(f"Congrats! you have guessed the right number {random_number}.")


# when the computer will guess the number
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'C':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be = high
        feedback = input(f"Is {guess} is too high (H) to low (L) or correct (C) ?").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Congrats! the computer guessed right your number, {guess}")
guess(10)
