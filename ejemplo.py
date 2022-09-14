lista4=["rojo, azul ,amarillo"]
print(lista4)
lista4.append("white")
print(lista4)
lista3=[2,3,6,7,1,4,5]
lista0=[10,20,30]
lista3.sort()
print(lista3)
lista3.extend(lista0)
print(lista3)





tupla=(1,2,3,4,5,6,2,2)
print(tupla.count(2))

diccionario={"gato":"cat","perro":"dog","cerdo":"pig"}
print(diccionario["gato"])


edad=(20)
if edad > 18:
     print("mayor de edad")
else:
     print("menor de edad")   
print("gracias porfesor")    

edad=(-1)
if edad > 18:
     print("mayor de edad")
elif edad <= 0:
    print("tu edad no puede ser menor a 0")  
else:
    print("menor de edad")




print("comienzo")
for i in [0,1,2,3]:
       print("hola", end="")
print()
print("final")

