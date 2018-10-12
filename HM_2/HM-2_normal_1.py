import math

my_list = [2, -5, 8, 9, -25, 25, 4]

i = 0
j = 0
# Счетчик правильных ответов

l = len(my_list)
# Длина списка


while i < l:

    print("Значение списка: ",
          my_list[i])

    if my_list[i] >= 0:
        
        sqrt_my_list = math.sqrt(float(my_list[i]))
        print("Квадратный корень равен: ", sqrt_my_list)
        
        if (math.trunc(sqrt_my_list) - sqrt_my_list) == 0:

            print("Квадратный корень целый!")

            my_list.append(my_list[i])

            j += 1

        else:

            print("Квадратный корень дробный!")
        
        
    else:
        print("Отрицательное!")
        
    i = i + 1


my_list[:l] = []

print(my_list)

    
       

