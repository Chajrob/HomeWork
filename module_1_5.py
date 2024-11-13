immutable_var = [1, 7], 2, True, 'pencil'
print('immutable_var: ', immutable_var)
#immutable_var[3]=5
# Выдает ошибку: "TypeError: 'tuple' object does not support item assignment"
# Элементы кортежа неизменяемые, что позволяет использовать кортеж для защиты данных от любых изменений.
mutable_list = [1, 2, 3, False, 'book']
mutable_list[3] = True
print('mutable_list: ',mutable_list)