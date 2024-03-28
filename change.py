def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print()
    print("Vuelto")
    print()
    print("Pesos:")
    print(int(vuelto))
    print("Centavos:")
    vuelto_en_float = (vuelto-int(vuelto)*(int(money)))
    print(int(vuelto_en_float))
