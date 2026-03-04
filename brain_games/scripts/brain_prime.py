from brain_games import run_game
from brain_games.games import PRIME_GAME_HINT, generate_number_for_prime


def main():
    run_game(
        hint=PRIME_GAME_HINT, 
        generator=generate_number_for_prime,
    )


if __name__ == '__main__':
    main()
