def Impuestos(auto, tipo):
    if tipo == 1:
        return (auto * 10) / 100
        
    elif tipo == 2:
        return (auto * 7) / 100
        
    else:
        return (auto * 3) /100
        
    

carro = Impuestos(250000, 2)
print("Total de impuestos a pagar:\n",carro)
