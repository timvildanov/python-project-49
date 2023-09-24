from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def generate_game_condition():
    """Generates progression"""
    start_number = randint(1, 100)
    increment = randint(1, 10)
    elements_num = 10
    hidden_element_index = randint(4, 7)
    prog_list = list(range(start_number,
                           start_number + elements_num * increment,
                           increment))
    return prog_list, hidden_element_index


def play_game():
    """Generates progression and returns the answer"""
    progression, random_el_index = generate_game_condition()
    question_index = progression[random_el_index]
    for index, value in enumerate(progression):
        if value == question_index:
            progression[index] = '..'

    return 'Question: ' + " ".join(map(str, progression)), str(question_index)
