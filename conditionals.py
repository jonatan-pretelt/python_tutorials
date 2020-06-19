# language = 'Python'

# if language == 'Python':
# 	print('Language is Python')

# else: 
# 	print('No match')

# user = 'Admin'
# logged_in = True

# if user == 'Admin' and logged_in:
# 	print('Admin Page')

# else: print('Bad Creds')


a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))
print(a is b)
print(a==b)


print('\n')

a = [1, 2, 3]
b =a

print(id(a))
print(id(b))
print(a is b)
print(a==b)