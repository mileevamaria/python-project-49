import random

CALC_GAME_HINT = 'What is the result of the expression?'
CALC_FIRST_PARAM_MIN = 1
CALC_FIRST_PARAM_MAX = 50
CALC_SECOND_PARAM_MIN = 1
CALC_SECOND_PARAM_MAX = 9
CALC_OPERATORS = ['+', '-', '*']


def generate_numbers_for_calc() -> tuple[str, str]:
    """
    Сгенерировать выражение для игры калькулятора
    Возвращает выражение и правильный ответ
    """
    param1 = random.randint(CALC_FIRST_PARAM_MIN, CALC_FIRST_PARAM_MAX)
    param2 = random.randint(CALC_SECOND_PARAM_MIN, CALC_SECOND_PARAM_MAX)
    operator = random.choice(CALC_OPERATORS)
    answer = 0
    match operator:
        case '+':
            answer = param1 + param2
        case '-':
            answer = param1 - param2
        case '*':
            answer = param1 * param2
    return f'{param1} {operator} {param2}', str(answer)
