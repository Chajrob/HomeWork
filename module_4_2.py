def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

test_function()

'''
Функция inner_function() вне функции test_function не функционирует и при вызове выдает ошибку:
NameError: name 'inner_function' is not defined
'''