import random

PRIME_GAME_HINT = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)
PRIME_MIN = 1
PRIME_MAX = 99


def generate_number_for_prime() -> tuple[str, str]:
    """
    Сгенерировать число для проверки простое или нет
    и правильный ответ
    """
    number = random.randint(PRIME_MIN, PRIME_MAX)
    is_prime = True
    for delimetr in range(2, number // 2 + 1):
        if number % delimetr == 0:
            is_prime = False
            break
    is_prime_str = 'yes' if is_prime else 'no'
    return str(number), is_prime_str
