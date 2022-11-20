#по середине
text = str(input('Введите приветствие: '))
print(text)
centr = text.center(50)
print(centr)


#только +

num1 = int(input('Число 1: '))
num2 = int(input('Число 2: '))
num3 = int(input('Число 3: '))
num4 = int(input(...))
sum = 0
if num1 >= 0:
    sum += num1
if num2 >= 0:
    sum += num2
if num3 >= 0:
    sum += num3

print('Сумма положительных чисел равна: ', sum)


#самописный калькулятор
int_first = int(input('Введите первое целое число: '))
int_second = int(input('Введите второе целое число: '))
string = input('Введите строку: ')
if string == '/' and int_second == 0:
    print('На ноль делить нельзя!')
elif string == '+':
    print(int_first + int_second)
elif string == '/':
    print(int_first / int_second)
elif string == '*':
    print(int_first * int_second)
elif string == '-':
    print(int_first - int_second)
else:
    print('Неверная операция')

#Отрезки
a1 = int(input('Введите а1: '))
b1 = int(input('Введите b1: '))
a2 = int(input('Введите а2: '))
b2 = int(input('Введите b2: '))

if b1 == a2:
    print (b1)
elif b2 == a1:
    print(b2)
elif a1 <= a2 and b1 >= b2:
    print (a2, b2)
elif a2 <= a1 and b2 >= b1:
   print(a1, b1)
elif a2 < b1 and b2 >= a1:
    if b2 > b1:
        print(a2, b1)
    else:
        print(a1, b2)
elif a1 < b2 and b1 >= a2:
    if b1 > b2:
        print(a1, b2)
    else:
        print(a2, b1)
else:
    print('Пустое множество')


#две старушки
v1 = float(input('Скорость первой старушки (м/ч): '))
v2 = float(input('Скорость второй старушки (м/ч): '))
s = float(input('Расстояние (метров): '))
print(f'Старушки встретятся через: {s/(v1 + v2)} секунд')

# гр по Фаренгейту
temp_far = float(input('Укажите температуру по Фаренгейту: '))
print(f'Температура по Цельсию равна: {5/9 * (temp_far - 32)}')






