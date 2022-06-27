# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

numbers_list = []
new_number_list = []
if first_number >= second_number:
    for n in range(second_number, first_number):
        numbers_list.append(n)
elif second_number >= first_number:
    for n in range(first_number, second_number):
        numbers_list.append(n)
for numbers in numbers_list:
    if numbers % 3 == 0:
        new_number_list.append(numbers)
print(new_number_list)

