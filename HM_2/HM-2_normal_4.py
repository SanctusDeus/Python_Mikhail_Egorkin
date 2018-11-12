import math
import random

r = [1, 2, 4, 5, 6, 45, 2, 5, 2, 6, 6, 6, 45, 45]
i = 0

l = len(r)

r.sort()

resolve_2 = []

print(r)

while i < l:

    print("Рассматриваем номер элемента: ", i)
    print("Элемент равен:", r[i])

    if r[i] != r[i+1]:
        resolve_2.append(r[i])
    
    while r[i] == r[i+1]:
        del(r[i])
        print("Был удален повторяющийся элемент:", r[i])
        l = len(r)-1
        print("Длина списка: ", l)

        if l < i + 1: break

    i += 1
    
    print(r)
    print("====================================")

resolve_2.append(r[l])

print("Неповторяющиеся элементы исходного списка:", r)

print("Элементы не имеющие повторений:", resolve_2)
