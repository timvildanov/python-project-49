import prompt

MAX_ATTEMPTS = 3


def get_user_name_cli():
    """CLI function for username."""
    cli_user_name = prompt.string('May I have your name? ')
    return cli_user_name


def get_user_answer_cli():
    """CLI function for user answer"""
    cli_user_answer = prompt.string('Your answer: ')
    return cli_user_answer


def input_user_name():

    user_name = get_user_name_cli()
    print(f'Hello, {user_name}!')
    return user_name


def check_user_answer(user_input, task_answer):

    if user_input == task_answer:
        return True, 'Correct!'
    else:
        return False, (f"'{user_input}' is wrong answer ;(. "
                       f"Correct answer was '{task_answer}'.")


def main_game_loop(game):
    """Main game logic"""
    print('Welcome to the Brain Games!')
    user_name = input_user_name()
    print(game.DESCRIPTION)

    correct_answers = 0

    while correct_answers < MAX_ATTEMPTS:
        question, correct_answer = game.play_game()
        print(question)
        user_response = get_user_answer_cli()
        result, response = check_user_answer(user_response, correct_answer)
        print(response)

        if result:
            correct_answers += 1
        else:
            print(f"Let's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')
