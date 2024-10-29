"""Practice functions with dictionaries"""

__author__ = 730772738


def invert(inp_dict: dict[str, str]) -> dict[str, str]:
    """Invert the key value pairs in a dictionary"""
    seen_values: list[str] = []  # keep track of values we have seen
    new_dict: dict[str, str] = {}

    for key in inp_dict:
        value = inp_dict[key]
        if value in seen_values:  # check for duplicate to raise error
            raise KeyError("No duplicate values allowed")
        seen_values.append(value)
        new_dict[value] = key

    return new_dict


def favorite_color(inp_dict: dict[str, str]) -> str:
    """Return the value (color) that is most frequent in dictionary"""
    # create a new dictionary to count frequencies of each color
    counter_dict: dict[str, int] = {}
    for key in inp_dict:
        value_str: str = inp_dict[key]
        if value_str in counter_dict:
            counter_dict[value_str] += 1
        else:
            counter_dict[value_str] = 1

    # find which frequency in counter_dict is highest and return key
    most_frequent: str = ""
    max: int = 0
    for key in counter_dict:
        value: int = counter_dict[key]
        if value > max:
            max = value
            most_frequent = key
    return most_frequent


def count(inp_list: list[str]) -> dict[str, int]:
    """Return the counts of each item in the input list"""
    counter_dict: dict[str, int] = {}
    for item in inp_list:
        if item in counter_dict:
            counter_dict[item] += 1
        else:
            counter_dict[item] = 1

    return counter_dict


def alphabetizer(inp_list: list[str]) -> dict[str, list[str]]:
    """Return a dictionary where each key is a unique letter in the alphabet
    and each value is a list of words that begin with that letter"""
    alph_dict: dict[str, list[str]] = {}  # create new alphabet dictionary
    for item in inp_list:
        first_letter = item[0].lower()  # make first_letter index 0 of the item
        if (
            first_letter in alph_dict
        ):  # if the first_letter key already exists, add to the list value
            alph_dict[first_letter].append(item)
        else:  # if it doesn't exist, create a new key value pair
            alph_dict[first_letter] = [item]
    return alph_dict


def update_attendance(inp_dict: dict[str, list[str]], day: str, student: str) -> None:
    """Update attendance dictionary with new day and student"""
    if day not in inp_dict:  # check if day already exists
        inp_dict[day] = []  # if it doesn't, create a new list
    if student not in inp_dict[day]:
        inp_dict[day].append(student)  # add the student to the day if not already there


print(invert({"apple": "cat", "orange": "dog"}))
print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))
print(count(["blue", "blue", "red", "orange", "orange", "blue"]))
print(alphabetizer((["cat", "apple", "boy", "angry", "bad", "car"])))

attendance_log: dict[str, list[str]] = {
    "Monday": ["Vrinda", "Kaleb"],
    "Tuesday": ["Alyssa"],
}
update_attendance(attendance_log, "Tuesday", "Vrinda")
update_attendance(attendance_log, "Wednesday", "Kaleb")
print(attendance_log)
