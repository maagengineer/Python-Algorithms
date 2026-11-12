#This algorithm is for calculating the total accounts payable (CXP) in pesos and dollars for a given number of suppliers.

#variables

cantsup, I = int(), int()
MontCXP, TotalCXPpesos, TotalCXPdolares = float(), float(), float()
Moneda = str()

#Repetir hasta que el usuario ingrese un número válido de suplidores
while True:
    try:
        cantsup = int(input("Ingrese la cantidad de suplidores: "))
        if cantsup <= 0:
            print("La cantidad de suplidores debe ser un número positivo. Intente nuevamente.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")

#Introducir los montos de CXP y la moneda para cada suplidor
for I in range(1, cantsup + 1):

    while True:
        Moneda = input("Ingrese la moneda (pesos(p)/dolares(d)): ")
        if Moneda =="p" or Moneda== "d":
            break
        else:
            print("Moneda inválida. Por favor, ingrese 'pesos' o 'dolares'.")

    while True:
        try:
            MontCXP = float(input(f"Ingrese el monto de la CXP del suplidor #{I}: "))
            if MontCXP > 0:
                break
            else:
                print("El monto debe ser un número positivo. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

    if Moneda == "p":
        TotalCXPpesos = TotalCXPpesos + MontCXP
    elif Moneda == "d":
        TotalCXPdolares = TotalCXPdolares + MontCXP        
#Presentar los resultados de la suma de CXP en pesos y dolares, para todos los suplidores.
print(f"El total de CXP en pesos es: {TotalCXPpesos}")
print(f"El total de CXP en dolares es: {TotalCXPdolares}")

