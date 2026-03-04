import random

EVEN_GAME_HINT = 'Answer "yes" if the number is even, otherwise answer "no".'
EVEN_MIN = 1
EVEN_MAX = 99


def _is_number_even(number: int) -> bool:
    return number % 2 == 0 


def generate_number_for_even() -> tuple[str, str]:
    """
    Сгенерировать число для проверки чет/нечет и правильный ответ
    """
    number = random.randint(EVEN_MIN, EVEN_MAX)
    correct_answer = 'yes' if _is_number_even(number) else 'no'
    return str(number), correct_answer
