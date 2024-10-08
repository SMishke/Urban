def print_params(a=1, b='строка', c=True):
   print(a,b,c)
print_params()
print_params(10)
print_params(b=25)
print_params(c=[1,2,3])

values_list = [42, 'пример', False]
value_dict = {'a':100, 'b': 'Другая строка', 'c': [1,2,3]}

print_params(*values_list)
print_params(**value_dict)

values_list_2 = [54.32, 'строка']
print_params(*values_list_2, 42)


