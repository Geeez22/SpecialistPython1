# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    if len(str(ticket_number)) != 6:
        return 'необходимо ввести 6 символов'
    else:
        ticket_number = str(ticket_number)
        a = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
        b = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])
        if a == b:
            return 'Билет счастливый'

        return 'Билет не счастливый'


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))


