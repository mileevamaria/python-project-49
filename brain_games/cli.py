import prompt


def welcome_user():
    """Приветствие пользователя"""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name.capitalize()}!')
