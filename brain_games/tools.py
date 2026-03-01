import random

BRAIN_EVEN_RULE = (
    'Answer "yes" if the number is even, otherwise answer "no".'
)
BRAIN_CALC_RULE = "What is the result of the expression?"


def get_random_number() -> int:
    """Получить случайное целое число от 1 до 99"""
    return random.randint(1, 99)


def is_number_even(number: int) -> str:
    """Проверка числа: целое или нет"""
    return 'yes' if number % 2 == 0 else 'no'


def generate_calc_expression() -> tuple[str, str]:
    """Сгенерировать выражение для калькулятора"""
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
