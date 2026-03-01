from brain_games import congrat, get_name, reply_answer, welcome
from brain_games.even import (
    BRAIN_EVEN_ATTEMPS,
    BRAIN_EVEN_RULE,
    ask_if_number_even,
    get_random_number,
    is_number_even,
)


def main():
    name = get_name()
    welcome(name)
    print(BRAIN_EVEN_RULE)
    attempt = 0
    while attempt < BRAIN_EVEN_ATTEMPS:
        number = get_random_number()
        answer = ask_if_number_even(number)
        correct_answer = is_number_even(number)
        reply_answer(answer=answer, correct_answer=correct_answer, name=name)
        if answer != correct_answer:
            return
        attempt += 1
    congrat(name)


if __name__ == '__main__':
    main()
