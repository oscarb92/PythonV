def calcular_total(num1, num2, num3):
    return num1 + num2 + num3

print(calcular_total(5, 4, 4))

def saludar() -> str:
    return 'Hola mundo'

print(saludar())

def calcular_total(num1, num2, num3):
    total_local = num1 + num2 + num3
    return total_local

def promedio():
    numero_1 = int(input('Primer número: '))
    numero_2 = int(input('Segundo número: '))
    numero_3 = int(input('Tercero número: '))
    total = calcular_total(numero_1, numero_2, numero_3)
    return total / 3
    
print(promedio())