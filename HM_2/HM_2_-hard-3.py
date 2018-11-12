import math

s = []
sub_s = []

i = 0
j = 0
dim = 0
current = 0
number = 1
floor = 0
place = 0

n = int(input("Введите номер комнаты: "))
              
while i < n:

    dim += 1
    l = 0

    while l < dim and i < n:

        l += 1
        
    
        while j < dim and i < n:


            print("Номер комнаты: ", i + 1)
            print("Номер комнаты в ряду: ", j + 1)
            print("Размер комнаты:", dim)
        
            sub_s.append(i+1)
            print("sub_s = ", sub_s)

            place = j + 1
            print ("Место на этаже: ", place)

            
            j += 1
            i += 1
            

        s.append(sub_s)
        
        sub_s = []
        j = 0
        current += 1
        
        print("________________________________________")
        
        
print("S = ", s)

print("Этаж №: ", len(s))
print ("Место на этаже: ", place)

        
    
