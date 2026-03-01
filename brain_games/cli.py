import prompt


def welcome_user():
    """Приветствите пользователя"""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name.capitalize()}!')
