edad = 58
genero = "F"
semanas = 240

if edad >= 58 and genero == "F" and semanas >= 250:
    print("Se puede pensionar")
else: 
    print("No se puede pensionar")

# o tambien

if genero == 'F':
    if edad >= 58:
        if semanas >= 250:
            print('Se puede pensionar')
        else:
            print('Le faltan '+str( 250 - semanas ) +' semanas')
    else:    
        print('Le faltan '+str( 58 - edad ) +' años')