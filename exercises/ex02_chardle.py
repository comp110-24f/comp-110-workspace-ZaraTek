"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730772738"


def input_word() -> str:
    """Asks user for a 5-letter word"""
    print("Enter a 5-character word:")
    word: str = input()
    if len(word) != 5:  # checks for valid input
        print("Error: Word must contain 5 characters.")
        exit()  # exits if input is invalid
    return word


def input_letter() -> str:
    """Asks user for a single character"""
    print("Enter a single character:")
    character: str = input()
    if len(character) != 1:  # checks for valid input
        print("Error: Character must be a single character.")
        exit()  # exits if input is invalid
    return character


def contains_char(word: str, letter: str) -> None:
    """Counts instances of letter in word"""
    print("Searching for", letter, "in", word)
    count = 0
    # checks each individual character in the word and compares to letter
    # instead of just using a for loop lol
    if word[0] == letter:
        print(letter, "found at index", 0)
        count += 1
    if word[1] == letter:
        print(letter, "found at index", 1)
        count += 1
    if word[2] == letter:
        print(letter, "found at index", 2)
        count += 1
    if word[3] == letter:
        print(letter, "found at index", 3)
        count += 1
    if word[4] == letter:
        print(letter, "found at index", 4)
        count += 1
    if count == 0:
        print("No instances of", letter, "found in", word)
    elif count == 1:
        print(count, "instance of", letter, "found in", word)
    else:
        print(count, "instances of", letter, "found in", word)


def main() -> None:
    """Calls contains_char with input_word and input_letter as parameters"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
