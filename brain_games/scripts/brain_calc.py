from brain_games import (
    GAME_ATTEMPS,
    ask_question,
    congrat,
    get_name,
    reply_answer,
    welcome,
)
from brain_games.tools import BRAIN_CALC_RULE, generate_calc_expression


def main():
    name = get_name()
    welcome(name)
    print(BRAIN_CALC_RULE)
    attempt = 0
    while attempt < GAME_ATTEMPS:
        question, correct_answer = generate_calc_expression()
        answer = ask_question(question=question)
        reply_answer(answer=answer, correct_answer=correct_answer, name=name)
        if answer != correct_answer:
            return
        attempt += 1
    congrat(name)


if __name__ == '__main__':
    main()
