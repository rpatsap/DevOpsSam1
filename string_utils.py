def print_string(s):
    if not isinstance(s, str):
        print("Помилка: очікується рядок.")
        return
    print(s)


def detect_case(s):
    if not isinstance(s, str):
        return "Помилка: очікується рядок."

    if s.isupper():
        return "Всі букви великі"
    elif s.islower():
        return "Всі букви малі"
    else:
        return "Змішаний регістр"


def uppercase_list():
    return [letter.upper() for letter in "smogtether"]
