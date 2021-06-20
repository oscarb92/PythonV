poblacion = 2000
mujeres = 1400
hombres = 600

print((int(hombres)+int(mujeres)) == int(poblacion))

#evaluar si la persona pertenece a la categoria
#opcion 1

edad = int(input("Ingrese la edad del jugador: "))
if edad >= 10 and edad <= 14:
    print("El jugador es categoria infantil.")
elif edad >= 15 and edad <= 17:
    print("El jugador es categoria juvenil.")
elif edad >= 18 and edad <= 20:
    print("El jugador es categoria Sub20.")
elif edad > 20:
    print("El jugador es categoria Profesional.")
else: 
    print("El jugador no aplica categoria, muy joven.")

#opcion 3

edad = int(input("Escriba su edad: "))
if edad >= 10 and edad <=14:
    print("Eres de la categoria infantil")
elif edad >= 15 and edad <=17:
    print("Eres de la categoria juvenil")
elif edad >= 18 and edad <=20:
    print("eres de la categoria sub 20")
elif edad > 20:
    print("eres de la categoria profecional")

#el profesor

edad = input("Digite la edad")
edad = int(edad)
if edad > 20:
    print("Categoria profesional")
elif edad >= 18:
    print("Categoria sub 20")
elif edad >= 15:
    print("Categoria juvenil")
elif edad >= 10:
    print("Categoria infantil")
else:
    print("Edad invalida")