def verificar_mayor(edad1, edad2, edad3, edad4):
    if edad1 > edad2 > edad3 > edad4 :
        print("1 " * str(edad1))
    elif edad2 > edad3 > edad4 :
        print("2 " + str(edad2))
    elif edad3 > edad4 :
        print("3 " + str(edad3))
    else:
        print("4 " + str(edad4))


verificar_mayor(15, 48, 45, 25)
verificar_mayor(15, 28, 25, 35)
verificar_mayor(15, 58, 45, 65)
