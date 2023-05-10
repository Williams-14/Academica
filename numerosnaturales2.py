def NumerosNaturales(num):
    
    for i in range(num + 1):
        cubo = (i + 1) ** 3
        print(f"El cubo de {i+1} es: {cubo}")

    return "Numeros naturales", str(num)

numbers = int(input("Ingresa un numero natural mayor a 0:\n"))   
print(NumerosNaturales(numbers))
