from brain_games import run_game
from brain_games.games import CALC_GAME_HINT, generate_numbers_for_calc


def main():
    run_game(
        hint=CALC_GAME_HINT, 
        generator=generate_numbers_for_calc,
    )


if __name__ == '__main__':
    main()
