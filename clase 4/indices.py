#los indices en programacion son numericos y empiezan desde cero

palabra = "Un texto de varias palabras"
print(palabra [0])
print(palabra [10])

#para reemplazar una letra por otra
print(palabra.replace("a" , "i"))

#si no quiero cambiarla en todas las palabras si no una sola
print(palabra.replace("e" , "a" , 5))

print(palabra[0:5])
print(palabra[-5:])
print(palabra[::1])
print(palabra[::2])
print(palabra[::-1])