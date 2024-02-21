# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
#
# print(new_numbers)

# name = "Angela"
# letter_list = [letter for letter in name]

# range(1,5)
# range_list = [n * 2 for n in range(1, 5)]
# print(range_list)
#
#
# # conditional list comprehension:
# names = ['Alex', 'Beth', "Caroline", 'Dave', 'Eleanor', 'Freddie']
# short_names = [name for name in names if len(name) > 5]
#
#
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# squared_num = [num * num for num in numbers]
# print(squared_num)



list_of_strings = input().split(',')
results = [num for num in list_of_strings if int(input()) % 0]
print(results)