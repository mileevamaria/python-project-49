from brain_games import run_game
from brain_games.games import (
    PROGRESSION_GAME_HINT,
    generate_numbers_for_progression,
)


def main():
    run_game(
        hint=PROGRESSION_GAME_HINT, 
        generator=generate_numbers_for_progression,
    )


if __name__ == '__main__':
    main()
