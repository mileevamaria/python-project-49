from brain_games import run_game
from brain_games.games import GCD_GAME_HINT, generate_number_for_gcd


def main():
    run_game(
        hint=GCD_GAME_HINT, 
        generator=generate_number_for_gcd,
    )


if __name__ == '__main__':
    main()
