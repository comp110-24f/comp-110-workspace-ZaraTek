"""EX03 - Wordle - a fun word game"""

__author__ = "730772738"


def input_guess(num_char: int) -> str:
    """Takes an input from the user that is the correct length"""
    print("Enter a", num_char, "character word")
    guess: str = input()
    while len(guess) != num_char:
        print("That wasn't", num_char, "chars! Try again:")
        guess = input()

    return guess


def contains_char(word: str, char: str) -> bool:
    """Checks if a character is in the word"""
    assert (len(char)) == 1  # throws error if char is not length of 1
    idx: int = 0
    while idx < len(word):
        if word[idx] == char:
            return True
        idx += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Checks if characters are in the right spot, in the word at all, or neither;
    prints corresponding emojis"""
    assert len(guess) == len(
        secret
    )  # throws error if guess and secret are not matching lengths
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emojis: str = ""
    i: int = 0
    while i < len(guess):
        if guess[i] == secret[i]:  # char is in correct spot
            emojis += GREEN_BOX
        elif contains_char(secret, guess[i]):  # char is in the word
            emojis += YELLOW_BOX
        else:  # char is not in the word
            emojis += WHITE_BOX
        i += 1

    return emojis


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn_number: int = 6
    i: int = 0
    won: bool = False
    while i < turn_number and not won:  # exits loop if you win or hit 6 turns
        print("=== Turn ", (i + 1), "/", turn_number, " ===", sep="")
        guess: str = input_guess(len(secret))
        emojis: str = emojified(guess, secret)
        print(emojis)
        if emojis == "\U0001F7E9" * len(secret):
            # had to multiply green emoji by the length of the word
            # so it works for every case
            won = True
        i += 1
    if won:
        print("You won in ", i, "/6" " turns!", sep="")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="clench")
