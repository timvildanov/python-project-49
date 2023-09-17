from brain_games.randomize import generate_random_number

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_game():
    """Generate random number and returns the answer"""
    rand_num1 = generate_random_number()
    question_user_task = f'Question: {rand_num1} '

    task_result = ''
    if rand_num1 % 2 == 0:
        task_result += 'yes'
    else:
        task_result += 'no'
    return question_user_task, task_result
