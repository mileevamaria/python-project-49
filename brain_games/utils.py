import prompt


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
