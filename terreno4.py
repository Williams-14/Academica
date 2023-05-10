def Inversion(invertido, año):
    anual = (invertido * 15) /100
    ganancia = anual * (2023 - año)
    total = ganancia + invertido

    return total

print("Total ganado por su inversión:")
print(Inversion(1500, 1961))

