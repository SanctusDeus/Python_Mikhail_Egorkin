from random import randint

def create_battle_field(size): # Создает поле для игры, размерность size, пока для примера со случайными крестиками, ноликами и пустыми полями
        
        support_field = []
        field = []
        for i in range(size):
                for j in range(size):
                        a = randint(0, 2)
                        if a == 0: support_field.append("-")

                        elif a == 1: support_field.append("X")

                        elif a == 2: support_field.append("O")

                field.append(support_field)
                support_field = []
        return field


def shooting(field, cell, symbol): # Ставит крестик или нолик на поле!


        dy = cell//10 + 1

        if cell < 10:
                dx = cell
        else:
                while cell > 10:
                        cell = cell - 10
                dx = cell

        if dx > len(field) or dy > len(field):
                print("Указаны неверные координаты!")
                pass
        
        if player == "X":
                shoot = "X"
        elif player == "O":
                shoot = "O"
        else:
                print("Поле игрок может принимать значения X или O")
                pass
        
        support_field = field[dy]

        if support_field[dx] == "-":
                support_field[dx] = shoot
                field[dy] = support_field
        else: print("Неправильный ход. На данном месте уже есть метка!")

        return field

def element(field, dx, dy): # Выводит элемент с координатами
        
        support_line = []
        support_line = field[dy]

        return support_line[dx]

def line_field(field): #Разворачивает поле в одномерный список
        line = []
        s = []
        for i in range(len(field)):
                for j in range(len(field)):
                        s = field[i]
                        line.append(s[j])
                s = []
        return line

def moves(field): #Возвращает координаты всех возможных ходов с пустыми клетками
        line = line_field(field)
        all_moves = []
        
        for i in range(len(line)):
                if line[i] is "-": all_moves.append(i)
                
        return all_moves


def lines_of_game(field): # Раскладывает поле на все возможные линии выигрыша

        g_lines = []
        support_line_1 = []
        support_line_2 = []
        support_line_3 = []
        support_line_4 = []
        support_line_5 = []
        support_line_6 = []

        for i in range(len(field)):
                for j in range(len(field)):
                        support_line_1.append(element(field, i, j))
                        support_line_2.append(element(field, j, i))                                
                g_lines.append(support_line_1)
                g_lines.append(support_line_2)
                support_line_1 = []
                support_line_2 = []

        for i in range(len(field)):
                for j in range(i + 1):
                        support_line_3.append(element(field, i - j, j))
                        support_line_5.append(element(field, len(field)- j - 1, i - j))
                g_lines.append(support_line_3)
                g_lines.append(support_line_5)
                support_line_3 = []
                support_line_5 = []
                        
        for i in range(len(field) - 1):
                for j in range(i + 1):
                        support_line_4.append(element(field, len(field) - i + j - 1, len(field) - j - 1))
                        support_line_6.append(element(field, j, len(field) - i + j - 1))
                g_lines.append(support_line_4)
                g_lines.append(support_line_6)
                support_line_4 = []
                support_line_6 = []
                        
        return g_lines
                
        

def max_abreast(field): # Подсчитывает максимальное количество крестиков и ноликов по возможным линиям игры
        
        glines = lines_of_game(field)
        support_line = []
        max_len_1 = 1
        max_len_2 = 1
        abreast_X = 1
        abreast_Y = 1

        for i in range(len(glines)):
                support_line = glines[i]

                for j in range(len(support_line)):
                        if support_line[j] == "X":
                                for l in range(len(support_line) - j - 1):
                                        if support_line[j + l] == support_line[j + l + 1] and support_line[j + l + 1] == "X":
                                                max_len_1 += 1

                        if support_line[j] == "O":
                                for l in range(len(support_line) - j - 1):
                                        if support_line[j + l] == support_line[j + l + 1] and support_line[j + l + 1] == "O":
                                                max_len_2 += 1

                                                
                        if max_len_1 > abreast_X: abreast_X = max_len_1

                        if max_len_2 > abreast_Y: abreast_Y = max_len_2

                        max_len_1 = 1
                        max_len_2 = 1


        return abreast_X, abreast_Y





