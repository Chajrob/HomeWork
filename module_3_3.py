#1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a, b ,c)

print_params()
print_params(a = 1, b = 'строка')
#print_params(a, b, c) NameError: name 'a' is not defined
print_params(b = 25)
print_params(c = [1,2,3])

#2.Распаковка параметров:
values_list = ['string', False, 5]
values_dict = {'a': False, 'b': 4, 'c': 'цифра'}
print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
values_list_2 = [7, 'шаг']
print_params(*values_list_2, 42)