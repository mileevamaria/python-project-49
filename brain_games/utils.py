import prompt

REPLY_WRONG_ANSWER = (
    "'{wrong_answer}' is wrong answer ;(. "
    "Correct answer was '{correct_answer}'."
    "\nLet's try again, {name}!"
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


def reply_answer(answer: str, correct_answer: str, name: str) -> None:
    """Выводит сообщение о результате проверки ответа на вопрос"""
    if answer == correct_answer:
        print(REPLY_RIGHT_ANSWER)
    else:
        print(REPLY_WRONG_ANSWER.format(
            wrong_answer=answer,
            correct_answer=correct_answer,
            name=name,
        ))


def ask_question(question: str) -> str:
    """Спросить пользователя и получить ответ"""
    question = f'Question: {question}\nYour answer: '
    answer: str = prompt.string(question)
    return answer