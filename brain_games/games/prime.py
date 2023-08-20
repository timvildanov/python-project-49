from brain_games.project_libs import generate_random_number

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number % 2 == 0:
        return number == 2

    sqrt_num = int(number ** .5)

    for count in range(3, sqrt_num + 1, 2):
        if number % count == 0:
            return False

    return True


def game_rule():
    """Generates prime number and answer"""
    random_number = generate_random_number()
    asking_user_task = f'Question: {random_number}'
    task_answer = is_prime(random_number)
    task_result = ''
    if task_answer:
        task_result += 'yes'
    else:
        task_result += 'no'
    return asking_user_task, str(task_result)
