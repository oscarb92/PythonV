
diccionario = {'clave':'valor'}
diccionario = {'nombre1':'Marco', 
               'edad1':31, 
               'lenguajes':{1:'Python',
                            2:'C++',
                            3:'Java',
                            4:'PHP',
                            5:'JavaScript',
                            6:'C#'}
               }
print(diccionario['lenguajes'])

#para contar usamos len

print(len(diccionario["lenguajes"]))

autos = {'autos':{
        1:{'marca':'Tesla',
           'modelos':{
               1:'Model S',
               2:'Model E',
               3:'Model X',
               4:'Model Y',
               }
           },
        2:{'marca':'Toyota',
           'modelos':{
               1:'Fortuner',
               2:'Prado',
               3:'Tundra',
               4:'Corola',
               }
           },
        3:{'marca':'Range Rover',
           'modelos':{
               1:'Evoque',
               2:'Defender',
               }
           },
        4:{'marca':'Mazda',
           'modelos':{
               1:'Mazda 3',
               2:'Mazda 2',
               3:'CX 30',
               }
           },
        5:{'marca':'Audi',
           'modelos':{
               1:'A7',
               2:'A5',
               3:'A3',
               }
           }
        }
        }
#crear una condicional para saber cual es la marca de autos que tiene mas modelos
#se puede crear una variable para contar a cantidad de modelos

m1 = len(autos["autos"][1]["modelos"])
m2 = len(autos["autos"][2]["modelos"])
m3 = len(autos["autos"][3]["modelos"])
m4 = len(autos["autos"][4]["modelos"])
m5 = len(autos["autos"][5]["modelos"])

print(m1,m2,m3,m4,m5)
#aqui me muestra la cantidad de modelos en cada auto. Y ahi empiezo con la condicional para saber ahora si, la marca de aut q tiene mas mod

