number = int(input("Введите целое число - "))

current = 10
max = 0
modulo = 0

while modulo != number:
    modulo = number % current
    i = modulo // (current//10)
    current = current * 10
    if i > max:
        max = i

print("Макимальная цифра в числе - ", max)
