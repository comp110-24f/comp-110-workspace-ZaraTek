def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    return "no match!"


print(check_first_letter("apple", "a"))


def get_weather_report() -> str:
    print("What is the weather?")
    weather: str = input()
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recogonize this weather.")
    return weather


get_weather_report()
