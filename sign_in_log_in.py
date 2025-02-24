class User:
    def __init__(self, username, password, password_config):
        self.username = username
        if password == password_config:
            self.password = password

class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password

if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input('Приветствую! Выберите действие:\n1 - Вход\n2 - Регистрация\n'))
        if choice == 1:
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен, {login}')
                    break
                else:
                    print('Неверный пароль')
            else:
                print('Пользователь не найден.')
        if choice == 2:
            user = User(login := input('Введите логин: '), password := input('Введите пароль: '),
                        password2 := input('Подтвердите пароль: '))
            if (len(password) >= 8 and not password.isalpha() and not password.isdigit()
                    and not password.islower() and not password.isupper()):
                if password == password2:
                    print(f'{login} успешно зарегистрирован.')
                else:
                    print('Пароли не совпадают, попробуйте еще раз.')
                    continue
            else:
                print('Требование к паролю:'
                      '\n - не менее 8 символов'
                      '\n - использование заглавных'
                      '\n - использование строчных букв'
                      '\n - использование цифр'
                      '\n попробуйте еще раз.')
                continue
            database.add_user(user.username, user.password)
        print(database.data)