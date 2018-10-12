import math
import random

i = 0

random_list = []

n = int(input("Введите, пожалуйста, длину списка: "))

while i < n:

    random_list.append(random.randint(-100,100))
    i += 1

print(random_list)

