"""A Simple Number Guessing Game"""

__author__ = "730772738"


def guess_a_number() -> None:
    """Takes a number guess from user and compares it to a secret number"""
    secret: int = 7
    print("Guess a number: ")
    guess: int = int(input())
    print("Your guess was", guess)
    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is", secret)
    elif guess > secret:
        print("Your guess was too high! The secret number is", secret)


if __name__ == "__main__":
    guess_a_number()
