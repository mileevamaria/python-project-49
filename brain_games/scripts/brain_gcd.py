import random

from brain_games import run_game

EVEN_GAME_HINT = 'Find the greatest common divisor of given numbers.'


def _generate_number_for_gcd() -> tuple[str, str]:
    """
    Сгенерировать числa для проверки НОД и правильный ответ
    """
    number1, number2 = random.randint(0, 50), random.randint(0, 50)
    numbers_str = f'{number1} {number2}'
    if number2 == 0:
        correct_answer = str(number1)
    else:
        while number2 != 0:
            number1, number2 = number2, number1 % number2     
        correct_answer = str(number1)
    return numbers_str, correct_answer


def main():
    run_game(
        hint=EVEN_GAME_HINT, 
        generator=_generate_number_for_gcd,
    )


if __name__ == '__main__':
    main()
