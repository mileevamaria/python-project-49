from typing import Callable

from brain_games.cli import welcome_user
from brain_games.utils import (
    ask_question,
    congrat,
    get_name,
    reply_answer,
    welcome,
)

__all__ = ('welcome_user',)

GAME_ATTEMPTS = 3


def run_game(hint: str, generator: Callable) -> None:
    """
    Движок для запуска любой игры
    Меняется только подсказка, что нужно делать пользователю
    и функция, генерирующая запрос и правильный ответ
    """
    name = get_name()
    welcome(name=name)
    print(hint)
    for _ in range(GAME_ATTEMPTS):
        question, correct_answer = generator()
        answer = ask_question(question)
        reply_answer(answer=answer, correct_answer=correct_answer, name=name)
        if answer != correct_answer:
            return
    congrat(name=name)
