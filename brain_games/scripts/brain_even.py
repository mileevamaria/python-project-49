import random

from brain_games import run_game

EVEN_GAME_HINT = 'Answer "yes" if the number is even, otherwise answer "no".'


def _generate_number_for_even() -> tuple[str, str]:
    """
    Сгенерировать число для проверки чет/нечет и правильный ответ
    """
    number = random.randint(1, 99)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return str(number), correct_answer


def main():
    run_game(hint=EVEN_GAME_HINT, generator=_generate_number_for_even)


if __name__ == '__main__':
    main()
