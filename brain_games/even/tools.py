import random

import prompt


BRAIN_EVEN_ATTEMPS = 3
BRAIN_EVEN_RULE = (
    'Answer "yes" if the number is even, otherwise answer "no".'
)


def get_random_number() -> int:
    """Получить случайное целое число от 1 до 99"""
    return random.randint(1, 99)


def is_number_even(number: int) -> str:
    """Проверка числа: целое или нет"""
    return 'yes' if number % 2 == 0 else 'no'


def ask_if_number_even(number: int) -> str:
    """Спросить пользователя про число и получить ответ"""
    question = f'Question: {str(number)}\nYour answer: '
    answer: str = prompt.string(question)
    return answer
