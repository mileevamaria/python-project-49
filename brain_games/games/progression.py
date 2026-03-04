import random

PROGRESSION_GAME_HINT = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10
MIN_STEP = 1
MAX_STEP = 10
MIN_FIRST_NUMBER = 1
MAX_FIRST_NUMBER = 15


def generate_numbers_for_progression() -> tuple[str, str]:
    """
    Сгенерировать числa для ариф прогрессии и правильный ответ
    """
    missing_index = random.randint(0, PROGRESSION_LENGTH - 1)
    step = random.randint(MIN_STEP, MAX_STEP)
    first_number = random.randint(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)
    counter = first_number
    progression, correct_answer = '', ''
    
    for index in range(PROGRESSION_LENGTH):
        if index == missing_index:
            progression += '.. '
            correct_answer = str(counter)
        else:
            progression += f'{counter} '
        counter += step
    return progression.strip(), correct_answer
