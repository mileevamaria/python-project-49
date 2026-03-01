import random

from brain_games import run_game

PRIME_GAME_HINT = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)


def _generate_number_for_prime() -> tuple[str, str]:
    """
    Сгенерировать число для проверки простое или нет
    и правильный ответ
    """
    number = random.randint(1, 99)
    is_prime = True
    for delimetr in range(2, number // 2 + 1):
        if number % delimetr == 0:
            is_prime = False
            break
    is_prime_str = 'yes' if is_prime else 'no'
    return str(number), is_prime_str


def main():
    run_game(
        hint=PRIME_GAME_HINT, 
        generator=_generate_number_for_prime,
    )


if __name__ == '__main__':
    main()
