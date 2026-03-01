import random

import prompt

BRAIN_EVEN_ATTEMPS = 3
BRAIN_EVEN_RULE = (
    'Answer "yes" if the number is even, otherwise answer "no".'
)
BRAIN_EVEN_YES_WRONG_ANSWER = (
    "'yes' is wrong answer ;(. Correct answer was 'no'."
    "\nLet's try again, {name}!"
)
BRAIN_EVEN_NO_WRONG_ANSWER = (
    "'no' is wrong answer ;(. Correct answer was 'yes'."
    "Let's try again, {name}!"
)
BRAIN_EVEN_RIGHT_ANSWER = "Correct!"
BRAIN_EVEN_INCORRECT = 'Incorrect input'


def get_random_number() -> int:
    """Получить случайное целое число от 1 до 99"""
    return random.randint(1, 99)


def is_number_even(number: int) -> bool:
    """Проверка числа: целое или нет"""
    return number % 2 == 0


def ask_if_number_even(number: int) -> str:
    """Спросить пользователя про число и получить ответ"""
    question = f'Question: {str(number)}\nYour answer: '
    answer: str = prompt.string(question)
    return answer


def is_correct_answer(answer: str, number: int, name: str) -> bool:
    """Проверить ответ пользователя"""
    is_correct = False
    is_even = is_number_even(number)
    
    match answer:
        case 'yes':
            if is_even:
                is_correct = True
                print(BRAIN_EVEN_RIGHT_ANSWER)
            else:
                print(BRAIN_EVEN_YES_WRONG_ANSWER.format(name=name))
        case 'no':
            if is_even:
                print(BRAIN_EVEN_NO_WRONG_ANSWER.format(name=name))
            else:
                is_correct = True
                print(BRAIN_EVEN_RIGHT_ANSWER)
        case _:
            print(BRAIN_EVEN_INCORRECT)
        
    return is_correct
