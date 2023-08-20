import prompt


def get_user_name_cli():
    """CLI function for username."""
    cli_user_name = prompt.string('May I have your name? ')
    return cli_user_name


def get_user_answer_cli():
    """CLI function for user answer"""
    cli_user_answer = prompt.string('Your answer: ')
    return cli_user_answer

def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')