my_dict = {'Alex':1998, 'Boris':2005, 'Vlad': 2007, 'Ivan':1993}
print('my_dict:', my_dict)
print('Existing value (Alex):', my_dict['Alex'])
print('Not existing value (Stas):', my_dict.get('Stas'))
my_dict.update({'German': 1994, 'Igor': 1987})
print('Deleted value (Vlad):', my_dict.pop('Vlad'))
print('Modified my_dict', my_dict)

my_set = {1, 2, 'book', 3, 2, True, 5, 7, 9, 'book', 5, (5, 2), 1, 9, 9}
print('Set:', my_set)
my_set.update({'paper', 12})
my_set.discard(5)
print('Modified Set:', my_set)

