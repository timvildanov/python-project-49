from brain_games.randomize import generate_random_number

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number % 2 == 0:
        return number == 2

    sqrt_num = int(number ** .5)

    for count in range(3, sqrt_num + 1, 2):
        if number % count == 0:
            return False

    return True


def return_binary_result(task_answer):
    return 'yes' if task_answer else 'no'


def play_game():
    """Generates prime number and answer"""
    random_number = generate_random_number()
    question_user_task = f'Question: {random_number}'
    task_answer = is_prime(random_number)
    return question_user_task, return_binary_result(task_answer)
