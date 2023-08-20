from math import gcd
from brain_games.project_libs import generate_random_number

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def game_rule():
    """Generate 2 random numbers and returns the answer"""
    rand_num1 = generate_random_number()
    rand_num2 = generate_random_number()
    asking_user_task = f'Question: {rand_num1} {rand_num2}'
    task_answer = str(gcd(rand_num1, rand_num2))
    return asking_user_task, task_answer
