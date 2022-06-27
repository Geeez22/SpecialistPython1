# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.
import random

numbers = []
n = int(input())
for _ in range(n):
    number = random.randint(-100, 100)
    if number > 0:
        numbers.append(number)
sum = 0
for new_number in numbers:
    sum += new_number

print(sum)


