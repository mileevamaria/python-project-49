from brain_games import run_game
from brain_games.games import EVEN_GAME_HINT, generate_number_for_even


def main():
    run_game(
        hint=EVEN_GAME_HINT, 
        generator=generate_number_for_even,
    )


if __name__ == '__main__':
    main()
