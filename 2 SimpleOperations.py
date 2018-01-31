#about you
name = input("Введите ваше имя: ") #variable 'name' and function input to write name
age = input("Введите ваш возраст: ")
print("Вас зовут "+name+"") #function print
print("Вам "+age+" лет")

#calc
n1 = input("Введите первое число: ")
n2 = input("Введите второе число: ")
a = int(n1)
b = int(n2)
r1 = (a + b) #sum n1 and n2
r2 = (a - b)
r3 = (a * b)
r4 = (a ** b)
r5 = (a / b)
r6 = (a % b)
print("Сумма чисел: " + str(r1))#print sum and convert sum from int to string
print("Разность чисел: " + str(r2))
print("Произведение чисел: " + str(r3))
print("a в степени b: " + str(r4))
print("Деление чисел: " + str(r5))
print("Остаток от деления первого числа на второе: " + str(r6))
