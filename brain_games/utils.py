import prompt


REPLY_WRONG_ANSWER = (
    "'{wrong_answer}' is wrong answer ;(. Correct answer was '{right_answer}'."
    "Let's try again, {name}!"
)
REPLY_RIGHT_ANSWER = "Correct!"


def get_name() -> str:
    """Получить имя игрока"""
    name: str = prompt.string('May I have your name? ')
    return name.capitalize()


def welcome(name: str) -> None:
    """Поприветствовать игрока"""
    print(f'Hello, {name}!')


def congrat(name: str) -> None:
    """Поздравить игрока"""
    print(f'Congratulations, {name}!')


def reply_answer(answer, correct_answer, name):
    """Выводит сообщение о результате проверки ответа на вопрос"""
    if answer == correct_answer:
        print(REPLY_RIGHT_ANSWER)
    else:
        print(REPLY_WRONG_ANSWER.format(
            wrong_answer=answer,
            correct_answer=correct_answer,
            name=name,
        ))