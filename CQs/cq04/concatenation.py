__author__ = """730772738"""


def concat(str1: str, str2: str) -> str:
    """returns the concatenation of 2 strings"""
    return str1 + str2


if __name__ == "__main__":
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))
