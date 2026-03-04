import random

GCD_GAME_HINT = 'Find the greatest common divisor of given numbers.'
GCD_MIN_NUMBER = 0
GCD_MAX_NUMBER = 50


def generate_number_for_gcd() -> tuple[str, str]:
    """
    Сгенерировать числa для проверки НОД и правильный ответ
    """
    number1 = random.randint(GCD_MIN_NUMBER, GCD_MAX_NUMBER)
    number2 = random.randint(GCD_MIN_NUMBER, GCD_MAX_NUMBER)
    numbers_str = f'{number1} {number2}'
    if number2 == 0:
        correct_answer = str(number1)
    else:
        while number2 != 0:
            number1, number2 = number2, number1 % number2     
        correct_answer = str(number1)
    return numbers_str, correct_answer
