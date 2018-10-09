import math

print ("Решение уравнение вида ax**2 + b*x + c")

a = float(input ("Введите а - "))
b = float(input ("Введите b - "))
c = float(input ("Введите с - "))

d = - 4 * a * c + b ** 2

if d < 0:
    print ("Уравнение не имеет решения!")
elif d >= 0:
    resolve_1 = (-b + math.sqrt(d))/2
    resolve_2 = (-b - math.sqrt(d))/2
    print("Корни уравнения: x1 = ", resolve_1, " x2 = ", resolve_2)
