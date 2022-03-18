# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 15:39:36 2022

@author: alexg
"""

#print("Hola Mundo")

#asdasdas
"""
asdasd
"""

nombre_variable = 3
a="Hola"

"""
Asignar dos números cualesquiera, sumarlos y representarlos por terminal:
    1. Crear variable
    2. Asignar valor
    3. Crear otra variable
    4. Asignar otro valor
    5. Utilizar print para mostrar
Solución:
a=3
b=2
print(a+b)
"""

"""
a=input("Hola como estás?\n")
print(a)
"""

"""
Crear una lista, guardar varios números, coger el primero y el último, y sumarlos.
a=[3,4,5,6,1,2]
print(a[0]+a[-1])
"""



"""
Generar dos secuencias de palabras, de tal manera que si el usuario, dice por terminal la palabra "si"
printe dicha palabra, si responde que no, también printea y si no responde ninguna de las dos, entonces 
printear un 4.

#Solucion:
N=str(input("Ha desayunado hoy? "))
if N=="Si":
    print ("Muy bien, asi se hace")
elif N=="No":
    print ("Hay que desayunar")
else:
    print("No escribas cosas raras")
"""


"""
a=3
b=10
if(a==b):
    print(a)
elif(a>b):
    print(b)
else:
    print(a+b)

if(a==b):
    print(a)
if(a!=b):
    print(b)
    
if(a==b):
   print("son iguales")
elif(a>b):
    print("a es mayor que b")
else:
    print("b es mayor que a")    
"""



"""
for x in range(1,101):
    print(x)
""" 
"""
for x in range(1,101):
    if(x%2==0):
        print(x)

for x in range(0,101,2):
    print(x)
"""
"""
x=3
y=2
3/2 Resto -> 1
4/2 Resto -> 0
"""
"""
for x in range(1,101):
    if(x%2==0 and x>50):
        print(x)

for x in range(50,101):
    if(x%2==0):
        print(x)
"""

"""
a=0
lista=[1,3,34,24]
while(a<4):
    print(a)
    #a = a + 1
    a+=1
"""  
"""
Me hagáis la suma de los números del 1 a 10000, 
pero solo quiero los que sean múltiplos de 3
Solución:
    auxiliar=0
for x in range(0,10001):
    if(x%3==0):
        auxiliar=auxiliar+x

print(auxiliar)
Solución 2:
auxiliar=0
for a in range(0,10001,3):
    auxiliar=auxiliar+a
    
print(auxiliar)
"""    



"""
2 tipos:
    1.For -> iterar o recorrer una lista de elementos, normalmente
    esta lista se crea con range(valorDeInicio,valorFinal,saltos) 
    o una lista cualquiera
    2.While -> requiere una condición y no tiene por qué recorrer una lista
"""



def factorial(numero):
    if(numero>1):
        return factorial(numero-1)*numero
    else:
        return 1
    
def devuelveTexto(texto):
    print(texto)
    return 0
    
def llueve(estado):
    if(estado): #estado==True
        print("Oh no, saca tu paragüas")
    else:
        print("Todo bien, panita")
#print(factorial(3))

#llueve(True)
"""
Implementar la secuencia de fibonacci, de tal manera que yo le diga
cuántos números de la secuencia me tiene que devolver
Pista:
    1.Usar recursividad
    2.Definir valores iniciales
    3.Definir condición de la salida recursividad
"""

#print(devuelveTexto("Hola"))

"""
def a(numero):
    if(numero==0):
        return 0
    elif(numero==1):
        return 1
    else:
        return (a(numero-2)+a(numero-1))
n=int(input("cuantos numeros de secuencia?: \n"))
print("secuencia:")
for n in range(0, n):
  print(a(n))
"""

"""
Dada una cadena o texto, buscar una palabra determinada
"""









