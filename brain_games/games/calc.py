import operator
from brain_games.randomize import generate_random_number
from random import choice

DESCRIPTION = 'What is the result of the expression?'


def generate_random_operation():  # function to choose math operation
    """Generate random operation. Return str sign and math operator"""

    calc_operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }

    choice_of_operation = choice(list(calc_operations.keys()))
    operation = calc_operations.get(choice_of_operation)
    return choice_of_operation, operation


def play_game():
    """Generates 2 random numbers and calculates result"""
    generated_number1 = generate_random_number()
    generated_number2 = generate_random_number()
    game_operation, math_func = generate_random_operation()
    user_question = (f'Question: {generated_number1} {game_operation}'
                   f'{generated_number2}')
    correct_answer = str(math_func(generated_number1, generated_number2))
    return user_question, correct_answer
