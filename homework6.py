my_dict = {'Sergei': 1980, 'Pavel': 1981}
print(my_dict)
print(my_dict['Sergei'])
print(my_dict.get('Sergei')) #строки 3 и 4 - по сути, одно и тоже?
print(my_dict.get('Ivan'))
my_dict.update({'Masha': 2000,
               'Sasha': 2001})
print(my_dict)
name_two = my_dict.pop('Pavel')
print(my_dict)
print(name_two)

my_set = {1, 1, 2, 2, 'qwerty', 'str', 'str'}
print(my_set)
print(my_set.update({5, 'voice'}))
print(my_set)
print(my_set.discard(2))
print(my_set)