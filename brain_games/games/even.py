from brain_games.game_logic import generate_random_number

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_rule():
    """Generate random number and returns the answer"""
    rand_num1 = generate_random_number()
    asking_user_task = f'Question: {rand_num1} '

    task_result = ''
    if rand_num1 % 2 == 0:
        task_result += 'yes'
    else:
        task_result += 'no'
    return asking_user_task, task_result
