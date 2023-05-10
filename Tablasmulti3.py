def Tablas(num):
    for i in range(1, 11):
        cont = num * i 
        print(f"{num} x {i} = {cont}")
    return "Fin"

tablas = int(input("Ingrese que tabla de multiplicar desea conocer:\n"))
print(Tablas(tablas))