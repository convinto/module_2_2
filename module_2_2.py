first = int(input('Напишите произвольное число: '))
second = int(input('Напишите произвольное число: '))
third = int(input('Напишите произвольное число: '))

#if first != second and first != third and second != third:
if not first == second and not first == third and not second == third:
    print(0)
elif first == second and first == third and second == third:
    print(3)
else:
    print(2)