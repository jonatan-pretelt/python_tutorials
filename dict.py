student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompScie'] }

# print(student['courses'])


# print(student.get('phone', 'Not Found'))


# student['phone'] = '555-555'
# student['name'] = 'Jane'

# # print(student)

# student.update({'name':'Jen', 'age': 26, 'phone': '444-444'})

# print(student)

# del student['age']

# print(student)


# age=student.pop('age')

# print(student)
# print(age)

# print(len(student))

# print(student.keys())

# print(student.values())

# print(student.items())

# for key in student:
# 	print(key)


for key, value in student.items():
	print(key, value)