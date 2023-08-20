from random import randint
from cli import get_user_name_cli, get_user_answer_cli
from games import even

def generate_random_number():
    """Generate random number from 1 to 100."""
    return randint(1, 100)


def get_user_name():

    user_name = get_user_name_cli()
    print(f'Hello, {user_name}!')
    return user_name


def user_answer_checker(user_input, task_answer):

    if user_input == task_answer:
        return True, 'Correct!'
    else:
        return False, f"'{user_input}' is wrong answer ;(. Correct answer was '{task_answer}'."


def game_engine(game):
    """Main game logic"""
    print('Welcome to the Brain Games!')
    user_name = get_user_name()
    print(game.DESCRIPTION)

    correct_answers = 0

    while correct_answers < 3:
        question, correct_answer = game.game_rule()
        print(question)
        user_response = get_user_answer_cli()
        result, response = user_answer_checker(user_response, correct_answer)
        print(response)

        if result:
            correct_answers += 1
        else:
            print(f"Let's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')
