from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def arithmetic_progression():
    """Generates progression"""
    start_number = randint(1, 100)
    increment = randint(1, 10)
    elements_num = 10
    random_element_to_hide = randint(4, 7)
    prog_list = list(range(start_number,
                           start_number + elements_num * increment,
                           increment))
    return prog_list, random_element_to_hide


def game_rule():
    """Generates progression and returns the answer"""
    progression, random_el = arithmetic_progression()
    secret_element = progression[random_el]
    for index, value in enumerate(progression):
        if value == secret_element:
            progression[index] = '..'

    return 'Question: ' + " ".join(map(str, progression)), str(secret_element)
