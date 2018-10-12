import math
import random

i = 0

r_list = []

n = int(input("Введите, пожалуйста, длину списка: "))

while i < n:

    r_list.append(random.randint(-100,100))
    i += 1

print(r_list)


