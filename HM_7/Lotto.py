from random import randint, choice


def ticket(l):

    l = []
    line = []
    line_h = []
    numbers = []
    max_c = 89
    current = 0

    for i in range(90): numbers.append(i+1)

    
    for i in range(3):
        for j in range(5):
            line_h.append(numbers.pop(randint(1,max_c)))
            max_c -= 1
                
        line_h.sort()

        for j in range(9):
            rand_index = randint(0,1)
            if (rand_index != 0 and len(line_h) > 0) or current > 3:
                line.append(line_h.pop(0))
            elif current < 4:
                line.append(0)
                current += 1
                      
        l.append(line)
        line = []
        line_h = []
        current = 0
    return l

    

p = []
p = ticket(p)

comp = []
comp = ticket(comp)
numbers = []
n = 0
max_c = 89
answer = ""
exit_x = 0
current_errors = 0
sup = []
sup_c = []
win_p = 0
win_comp = 0

for i in range(90): numbers.append(i+1)


while exit_x != 1:

    n += 1
    current = numbers.pop(randint(1,max_c))
    max_c -= 1


    if win_p == 15:
        print("Поздравляем, вы победили!")
    if win_comp == 15:
        print("Победил ваш противник!")

    print("\n======================Новый раунд!======================\n")
    print("Вам осталось до победы: ", 15 - win_p)
    print("Противнику осталось до победы:", 15 - win_comp)
    print("Номер раунда: ", n)
    print("Выпал бочонок №: ", current)


    print("Ваша карточка")
    print("------------------------------------")

    for i in range(3):
        print(p[i])

    print("------------------------------------")
    print("Карточка противника")
    print("------------------------------------")

    for i in range(3):
        print(comp[i])

    answer = str(input("\nУ вас есть совпадение с выпавшим числом? (y/n)"))

    if answer == "y":
        for i in range(3):
            sup = p[i]
            if sup.count(current) > 0:
                sup[sup.index(current)] = 0
                win_p += 1
            else:
                current_errors += 1
                print("Нет совпадения")
            p[i] = sup
        if current_errors == 3:
            print("Проигрыш! Такого числа у вас нет!")
            exit_x = 1

        for i in range(3):
            sup_c = comp[i]
            if sup_c.count(current) > 0:
                sup_c[sup_c.index(current)] = 0

                win_comp += 1
            comp[i] = sup_c
            
    


        
    elif answer == "n":
        for i in range(3):
            if p[i].count(current) > 0:
                print("Проигрыш, совпадение найдено!")
                exit_x = 1
    
                
    else:
        print("Нет такого ответа!")
        exit_x = 1
    






