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
'''

# list_ = ['one', 'two', 'three']
# for i in range (len(list_)):
#     list_[i] = ' :('
# #    print(list_[i])
# print(list_)
# list_2 = [2, 3, 4, 5, 1]
# sum_ = 0
# for i in range(len(list_2)):
#     sum_ += list_2[i]
# print(sum_)

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i} x {j} = {i * j}') # print(i, 'x', j, '=', i * j) # примит.вариант

# dict_ = {'a': 1, 'b': 2, 'c': 3}
# print(dict_)
# for i in dict_:
#     print(i, dict_[i])
#
# for i, k in dict_.items():
#     print(i, k)