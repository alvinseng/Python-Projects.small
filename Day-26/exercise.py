# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
#
# print(new_numbers)

# name = "Angela"
# letter_list = [letter for letter in name]

range(1,5)
range_list = [n * 2 for n in range(1, 5)]
print(range_list)


# conditional list comprehension:
names = ['Alex', 'Beth', "Caroline", 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) > 5]


long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

