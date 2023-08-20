from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def arithmetic_progression():
    """Generates progression"""
    start_number = randint(1, 100)
    increment = randint(1, 10)
    length_of_progress = 10
    random_element_to_hide = randint(1, length_of_progress)
    return list(range(start_number, start_number + length_of_progress*increment,
                      increment)), random_element_to_hide


def game_rule():
    """Generates progression and returns the answer"""
    progression, random_el = arithmetic_progression()
    secret_element = progression[random_el]
    for index, value in enumerate(progression):
        if value == secret_element:
            progression[index] = '..'

    return " ".join(map(str, progression)), str(secret_element)
