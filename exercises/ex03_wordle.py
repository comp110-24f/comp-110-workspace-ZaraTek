"""EX-3 - Wordle - a fun word game"""

__author__ = "730772738"


def input_guess(num_char: int) -> str:
    """Takes an input from the user that is the correct length"""
    print("Enter a 5 character word")
    guess: str = input()
    while len(guess) != num_char:
        print("That wasn't 5 chars! Try again:")
        guess = input()

    return guess


def contains_char(word: str, char: str) -> bool:
    """Checks if a character is in the word"""
    assert (len(char)) == 1
    idx: int = 0
    while idx < len(word):
        if word[idx] == char:
            return True
        idx += 1
    return False


def emojified(guess: str, word: str) -> str:
    assert len(guess) == len(word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    print(WHITE_BOX, GREEN_BOX, YELLOW_BOX)


print(contains_char("craze", "b"))
emojified("", "")
