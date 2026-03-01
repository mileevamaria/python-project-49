import random

from brain_games import run_game

PROGRESSION_GAME_HINT = 'What number is missing in the progression?'


def _generate_numbers_for_progression() -> tuple[str, str]:
    """
    Сгенерировать числa для ариф прогрессии и правильный ответ
    """
    progression_length = 10
    missing_index = random.randint(0, progression_length - 1)
    step = random.randint(1, 10)
    first_number = random.randint(1, 15)
    counter = first_number
    progression, correct_answer = '', ''
    
    for index in range(progression_length):
        if index == missing_index:
            progression += '.. '
            correct_answer = str(counter)
        else:
            progression += f'{counter} '
        counter += step
    return progression.strip(), correct_answer


def main():
    run_game(
        hint=PROGRESSION_GAME_HINT, 
        generator=_generate_numbers_for_progression,
    )


if __name__ == '__main__':
    main()
