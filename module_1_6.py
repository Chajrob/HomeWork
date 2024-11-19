my_dict = {'Alex':1998, 'Boris':2005, 'Vlad': 2007, 'Ivan':1993}
print(my_dict)
print(my_dict['Alex'])
my_dict['Stas'] = 2003
print(my_dict['Stas'])
my_dict.update({'German': 1994, 'Igor': 1987})
print(my_dict.pop('Vlad'))
print(my_dict)

my_set = {1, 2, 'book', 3, 2, True, 5, 7, 9, 'book', 5, (5, 2), 1, 9, 9}
print(my_set)
my_set.update({'paper', 12})
my_set.discard(5)
print(my_set)

