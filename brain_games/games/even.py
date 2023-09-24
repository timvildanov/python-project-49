from brain_games.randomize import generate_random_number

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_game():
    """Generate random number and returns the answer"""
    rand_num1 = generate_random_number()
    question_user_task = f'Question: {rand_num1} '

    return question_user_task, 'yes' if rand_num1 % 2 == 0 else 'no'
