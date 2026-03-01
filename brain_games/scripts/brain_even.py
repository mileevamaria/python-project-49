from brain_games import congrat, get_name, welcome
from brain_games.even import (
    BRAIN_EVEN_ATTEMPS,
    BRAIN_EVEN_RULE,
    ask_if_number_even,
    get_random_number,
    is_correct_answer,
)


def main():
    name = get_name()
    welcome(name)
    print(BRAIN_EVEN_RULE)
    attempt = 0
    while attempt < BRAIN_EVEN_ATTEMPS:
        number = get_random_number()
        answer = ask_if_number_even(number)
        is_correct = is_correct_answer(
            answer=answer, number=number, name=name)
        if not is_correct:
            return
        attempt += 1
    congrat(name)


if __name__ == '__main__':
    main()
