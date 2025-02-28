"""
# food = ['apple', 'banana', 'coconut']
# print(food)
# print(food[1])
# food[1] = 'watermelon'
# print(food)
# food.append(True)
# print(food)
# food.extend([   666, 'funny'])
# print(food)
# food.append(food[0:5:2])
# print(food)
# food.remove(food[1])
# print(food)
# print('666' in food)
# print(666 in food)
# print('coconut' not in food)
# tuple_ = 1, 2, 3, True, 'string'
# tuple_2 = (1, 2, 3, 4)
# tuple_3 = tuple([1, 2, 3, 4])
# tuple_[4] = 5
# print(type(tuple_))
# print(tuple_[4])
# list = [1, 2, 3, True, 'string']
# print(tuple_, tuple_.__sizeof__())
# print(list, list.__sizeof__())
# tuple_2 = [1, 2], 3
# print(tuple_2)
# tuple_2 [0] [0] = 5
# print(tuple_2)
# tuple_ = (1, 2) + (3, 4)
# tuple_2 = tuple_ + (5, 6)
# tuple_3 = tuple_ + tuple_2
# print(tuple_)
# print(tuple_2)
# print(tuple_3)
# tuple_4 = tuple_ * 3
# print(tuple_4)
# phone_book = {['Alex']:111111, 'Bob':222222} - TypeError: unhashable type: 'list'
# phone_book = {'Alex':111111, 'Bob':222222}
# print(phone_book)
# print(phone_book['Alex'])
# phone_book['Alex'] = 333333
# print(phone_book)
# phone_book['John'] = 444444
# print(phone_book)
# phone_book.update({'Smith': 555555, 'Den':666666})
# print(phone_book)
# print(phone_book.get('Tom', 'Такого ключа нет')) # .get() в отличии от [] не вносит новые пары
# a = phone_book.pop('John') # .pop() в отличии от .del() не удаляет пары (только ключ),
#                            # а лишь изымает значение из словаря
# print(phone_book)
# print(a)
# list_ = [1, 2, 3, 4]
# list_.pop(2)
# print (list_)
# print(type(list_), list_)
# list_=set(list_)
# print(type(list_), list_)
# print(phone_book.keys())
# print(phone_book.values())
# print(phone_book.items())
# phone_book['Alex'] = [1111, 3333]
# print(phone_book)
# set_ = {1, 2, 3, 4, 2, 1, 3, 5, 4, 4, True, 'Pencil', (5, 6, 7)}
# print(set_)
# list_ = [1, 2, 8, 5, 6, 7, 3, 8, 9, 6, 7, 3, 2, 5, 7 ,5 ,3 , 3, 5, 1, 'penny']
# print(set(list_))
# print(type(list_))
# list_=set(list_)
# print(type(list_),list_)
# # print(list_[0]) в .set() нельза обратиться к элементу по индексу
# print(list_.discard('penny')) #НЕ выдает ошибку, если элемент не найден
# print(list_)
# print(list_.remove(5)) #выдает ошибку, если элемент не найден
# print(list_)
# #list_.pop(8) # изымает значение из множества
# #print(list_)
# print(list_.add(5)) # добавляет в множество элемент (отличается от .append())
# print(list_)
# a = 1 + 2j
# print(a, 'is complex number?', isinstance(a, complex))
# print(a, 'is complex number?', isinstance(1 + 2j, complex))
a = 1234567890123456789
b = 0.1234567890123456789
c = 1 + 2j
print('целое число: ', type(a), a)
print('число с плавающей запятой: ', type(b), b)
print('комплексные числа:', type(c), c)
d = [5,10,15,20,25,30,35,40]
# print('d[2]', d[2])
# print('d[0:3]', d[:3])
print('список: ', type(d), 'd[5:]', d[5:])
# d[2] = 22
# print(d)
t = (5, 'program', 1+3j)
# print('t[1]', t[1])
print('кортеж: ', type(t), 't[:3]', t[:3])
# t[0] = 5
# print(t)
# f = 'простая строка'
# ff = "простая строка"
# g = '''многострочная
# строка'''
"""
'''
gg = """многострочная 
# строка"""
# print(f)
# print(ff)
# print(g)
print('строка: ', type(gg), gg)
j = {1,3,3,2,2,4,4,4,4,4, True, False, 0} # False = o, True = 1, поэтому
                                          # выводится тот, который первым написан
print('множество: ', type(j), j)
k = {1:'value', 'key':2}
print('словарь:', type(k), k)
# print(k[1])
# print(k['key'])
# print(k[2])
print(float(5))
print(int(5.0349854562435687566))
print(int(-4.3453))
print(float('4'))
print(str(-4.645))
print(set([1,2,3]))
print(tuple({1,2,3}))
print(list('hello'))
l = ['h', 'e', 'l', 'l', 'o']
print(''.join(l))
print(dict([[4, 5], [6, 7]]))
print(dict([(8, 9), (10, 11)]))
print(dict([{8, 9}, {10, 11}]))

from time import sleep

a=5
print(a)
print('Я тут')
sleep(4)
print('Фуч, 4 секунды прошло')

name = input('Enter your name ')
if 1 < 5:
    print('ok')
    print('not ok')


list_ = ['one', 'two', 'three']
for i in range (len(list_)):
    list_[i] = ' :('
    print(list_[i])
print(list_)
list_2 = [2, 3, 4, 5, 1]
sum_ = 0
for i in range(len(list_2)):
    sum_ += list_2[i]
print(sum_)

for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} x {j} = {i * j}') # print(i, 'x', j, '=', i * j) # примит.вариант

dict_ = {'a': 1, 'b': 2, 'c': 3}
print(dict_)
for i in dict_:
    print(i, dict_[i])

for i, k in dict_.items():
    print(i, k)

def say_hello(name):
    print('Hello', name)
say_hello('Denis')
say_hello('Max')
say_hello('Anton')
'''
'''
import random
def lottery(mon, tue):
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print(mon, tue)
    return win1, win2
win1, win2 = lottery('mon', 'tue')
print(win1, win2)

def lottery_(*args, **kwargs):
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print(*args)
    return win1, win2
win1, win2 = lottery_(1, 2, 3, 4, 5, 6 ,7, 8, 9, 10)
print(win1, win2)

def test(a=2, b=True):
    print(a, b)

test()
test(False, 'ok')
test([1, 2])
test(*[3, 4])
test(**{'a':55, 'b':99})
test(**{'b':99})
test(**{'a':55})
'''
'''
def draw_area():
    for i in area:
        print(*i)
    print()

area = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
print('Добро пожаловать в крестики-нолики')
print('__________________________________')
draw_area()

row = int(input('Введите число (1, 2, 3) ')) - 1
columt = int(input('Введите число (1, 2, 3) ')) - 1
area[0][0] = 'X'
draw_area()
'''
'''
a = 'kukushka'
b = 'balalayka'
print(a[-2:])
if 'ka' not in a and b or 'ba' in b: # or 'sk' not in a:
    if a != b:
        print('you can')
    else:
        print("you can't")
else:
    print('impossible')
'''
'''
def test_func(*params):
    print('Тип:', type(params))
    print('аргумент:', params)

test_func(1, 2, 3, 4)
'''
'''
def summator (txt, *value, type='sum'):
    s = 0
    for i in value:
        s += i
    return f'{txt} {s} {type}'

print(summator('Сумма чисел:', 2,2, 3, 4, type='summator'))
'''
'''
def info(txt, *types, name_author = 'Den', **values):
    print('тип:', type(values))
    print('аргумент:', values)
    for key, value in values.items():
        print( key, value)
    print('name_author: ', name_author)
    print(types)
info('Пример разнообразия типов:', 1, 2, 3, 4, name_author = 'Denis', name = 'Den', course = 'Python')
'''
'''
def my_sum(n, *args, txt='Сумма чисел: '):
    s = 0
    for i in range(len(args)):
        s += args[i] ** n
    print(txt + ':', s)

my_sum(1, 1, 2, 3, 4, 5)
my_sum(2, 1, 2, 3, 4, 5, txt='Сумма квадратов')
my_sum(3, 1, 2, 3, 4, 5, txt='Сумма кубов')
'''
'''
def summa(n):
    if n == 0:
        return 0
    else:
        return n + summa(n - 1)

print(summa(10))
'''
'''
def find_max(list_):
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i
    return max_

print(find_max([0, 1, 4, -2, 94, 52, -32, 8]))

def count_even(list_):
    counter = 0
    for i in list_:
        if i == 0:
            continue
        if i % 2 == 0:
            counter += 1
    return counter

print(count_even([1, 3, -5, -6, 0, 57, 84, 29, 4, 16]))

def unique(list_):
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(unique([1, 4, 5, 7, 9, 8, 4, 5, 41, 2, 7, 1.0]))
'''
'''
def isPrime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

print(isPrime(11))
'''
'''
import sys

for path in sys.path:
    print(path)
print('----------------')
for argv in sys.argv:
    print(argv)
'''
'''
from dis import dis

def some_funs():
    a = "I'm from second module"
    print("I'm from second MODULE")
    return a

print(some_funs())
dis(some_funs)
'''
'''import math

def print(*args):
    return 'Ok'

def square(x):
    d = x ** 2
    print(1, locals())
    return d

a = 5
b = square(2)
print(a)
print(b)
print(2, globals())
'''
'''a = 10

def outer():
    a = 5

def inner():
    print(a)

inner()
outer()'''
'''import math
d = 7

def square(x):
    d = x ** 2
    def even(x):
        d = x / 2
        if d % 2 == 0:
            print(d, 'Четное')
        else:
            print(d, 'Нечетное')
    even(x)
    return d

a = 5
b = square(7)
print('a', a)
print('b', b)
print('d', d)
'''
'''from module_4.sortfunc import *

data_1 = list(map(int, input('Введите цифры с пробелом: ').split()))
data_2 = list(map(int, input('Введите цифры с пробелом: ').split()))
data_3 = list(map(int, input('Введите цифры с пробелом: ').split()))

print(bubble_sort(data_1))
print(selection_sort(data_2))
print(insertion_sort(data_3))'''
'''class Human:

    head = True

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()

    def say_info(self):
        print(f"Hello, my name's {self.name}. I'm {self.age}")

    def birthday(self):
        self.age += 1
        print(f"Hello, it's my birthday today. I'm {self.age}")

    def __str__(self):
        return f'{self.name}'

    def __len__(self):
        return self.age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __bool__(self):
        return bool(self.age)

    # def __del__(self):
    #     print(f'{self.name} go out')

den = Human('denis', 22)
dim = Human('dmitriy', 22)
print(den == dim)
dim.birthday()
print(dim == den)
print(dim.__len__())
print(len(dim))
if den:
    den.say_info()
print('++++++++++')
a = 6
print(Human.head)'''
'''
# паnтерн Singleton
# __new__(cls) - вызывается перед созданием объекта класса
# super() - позволяет вызывать методы родительского класса (нр., Object)
#           из дочернего класса (нр, User)
# __instance = None - используется в паттерне Singleton. Он хранит ссылку на экземпляр класса,
#                    и если такого экземпляра нет, то атрибут принимает значение None
# setattr() - метод задает для каждого объекта класса соответствующий ключ и
#             сохраняет в него значение self, key, values
class User:
    __instance = None
    def __new__(cls, *args, **kwargs):
        print('Я в НЬЮ')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        print('Я в ИНИТЕ')
        self.args = args
        for key, values in kwargs.items():
            setattr(self, key, values)

other = [1, 2, 3]
user = {'name': 'Denis', 'age': 25, 'gender': 'male'}

user1 = User(*other, **user)
print(user1)
print(user1.args)
print(user1.name)
print(user1.age)
print(user1.gender)'''
'''class User:
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
            user = User(input('Введите логин: '), password := input('Введите пароль: '),
                        password2 := input('Подтвердите пароль: '))
            #        вписать систему проверки пароля: мин 8 символов,
            #        1 заглавная буква и 1 цифра в пароле.
            if password != password2:
                print('Пароли не совпадают, попробуйте еще раз')
                continue
        database.add_user(user.username, user.password)
        print(database.data)'''

