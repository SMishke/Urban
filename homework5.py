immutable_var = 1, 2, 'root'
print(immutable_var)
#immutable_var[2] = 'food'
# с точки зрения безопасности, хранения и снижения объема данных кортежи неизменяемые

mutable_list = ['root', 'food', 'foot']
print(mutable_list)
mutable_list[0] = 'good'
print(mutable_list)