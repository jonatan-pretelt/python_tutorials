def hello_func(greeting, name='You'):
	return '{}, {}'.format(greeting, name)

print(hello_func('Hi', name = 'Jon'))