import random

from brain_games import run_game

CALC_GAME_HINT = 'What is the result of the expression?'


def _generate_numbers_for_calc() -> tuple[str, str]:
    """
    Сгенерировать выражение для игры калькулятора
    Возвращает выражение и правильный ответ
    """
    list_operators = ['+', '-', '*']
    param1 = random.randint(1, 50)
    param2 = random.randint(1, 9)
    operator = random.choice(list_operators)
    answer = 0
    match operator:
        case '+':
            answer = param1 + param2
        case '-':
            answer = param1 - param2
        case '*':
            answer = param1 * param2
    return f'{param1} {operator} {param2}', str(answer)


def main():
    run_game(
        hint=CALC_GAME_HINT, 
        generator=_generate_numbers_for_calc,
    )


if __name__ == '__main__':
    main()
