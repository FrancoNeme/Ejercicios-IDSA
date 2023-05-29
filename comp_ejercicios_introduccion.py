#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 21:11:29 2023

###############################################
#                                             #                                                 
# PRIMEROS EJERCICIOS INTRODUCCION A PYTHON   #
#                                             #      
###############################################

@author: 
"""

#%% COMENTARIOS EN GENERAL
# = = = = = = = = = = = = =  

# LA RESPUESTA MAS PROBABLE ES LA MAS SIMPLE

#%% EJERCICIO 1.24
# = = = = = = = = = 

edad = int(input('Ingrese edad: '))

for i in range(1,edad+1):    
    
    print('Cumpleaños ', i)



#%% EJERCICIO 1.27:
# = = = = = = = = =

DS = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

# Forma 1:    
# for i in range(2):
#     DS.pop(-1)

# Forma 2:

DS = DS[:5]
print(DS)



#%% EJERCICIO 1.30:
# = = = = = = = = =

# Tarea 1.30
# Crear una lista l1 con todos los impares de 1 a 5
# Insertar los pares en los lugares correspondientes
# para que la lista quede ordenada


l1 = list(range(1,6,2))

# Forma más óptima (la que hizo el profe):
# ----------------------------------------

l3 = list(range(2,6,2))

l1.extend(l3)
l1.sort()


# Otras formas:
# ------------

l2 = l1.copy()

# ___Forma 1:
    
for i in (l2):
    
    if i < l2[-1]:
        
        l1.insert(i,i+1)

# ___Forma 2:

j = 0

while j < l2[-1]-1:
    
    l1.insert(l1[j],l1[j]+1)
    
    j = j + 2



#%% EJERCICIO 1.40:
# = = = = = = = = = 

# Tarea 1.40
# Crear una diccionario d con todos los días de la
# semana poniendo como clave las siete primeras
# letras del alfabeto
# Imprimir el diccionario


dias = {'a': 'Lunes', 'b': 'Martes', 'c': 'Miércoles', 'd': 'Jueves', 'e': 'Viernes', 'f': 'Sábado', 'g': 'Domingo'}    

for i in dias:
    
    dias[i] = dias[i].upper()

print(dias)


# Forma 2:
# --------

# for i in dias.values():
    
#     i = i.upper()
#     print(i)



#%% EJERCICIO 1.47 - 1.48
# = = = = = = = = = = = = 


# Tarea 1.47 
# Crear una tupla t1 con las longitudes de los meses del año 2023 
# Crear una tupla t2 con los nombres de los meses del año 
# Crear una tupla t3 con los nombres de los dí­as de la semana 
# Recorrer el año mostrando por pantalla el número de dí­a dentro del año,
# el número del dí­a dentro del mes, el nombre del mes y el dia de la semana

# Tarea 1.48
# Crear una lista con las fechas largas que hemos mostrado
# por pantalla en el ejercicio 1.46 (nombre del día dentro de
# la semana, número del día dentro del mes, nombre del
# mes)


t1 = (31,28,31,30,31,30,31,31,30,31,30,31)

t2 = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

t3 = ("Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado")

diames = 1               #Dia dentro del mes
ptr = 0                  #Puntero a las tuplas t1 y t2
largomes = t1[ptr]       #Largo del mes actual
mes = t2[ptr]            #Mes actual

l1 = []

for dia in range(1,366):
    
    if diames > largomes:
        
        diames = 1
        ptr = ptr + 1
        largomes = t1[ptr]
        mes = t2[ptr]
    
    diasemana = t3[(dia-1)%7]
    
    l1.append("Dia %s: %s %s de %s" %(dia, diasemana, diames, mes))
    
    print("Dia", dia, ":", diames, "de", mes, "-", diasemana)
    
    diames = diames + 1



#%% EJERCICIO 1.49
# = = = = = = = = =

# Resolución rápida (era la que tenía que hacer en un principio): 
# ---------------------------------------------------------------

fecha = input('Ingrese fecha, utilizando el siguiente formato: [diames] de [Mes]: ')

for i in l1:
    
    if fecha in l1:
        
        print(i)
        
        break



#%% EJERCICIO 1.50
# = = = = = = = = =

# Generar una lista l1 con los números del 1 al 10
# Generar una lista l2 que tenga una lista con los números
# del uno al 10 en cada uno de sus 10 elementos
# Recorrer l2 con un for anidado dentro de otro for
# mostrando el producto de ambas coordenadas.

# Resolución 1:
# --------------

l1 = list(range(1,11)) 

l2 = []


for i in l1:
    
    l2.append(l1)


l3 = []


for i in l1:
    
    for j in l2:
        
        l3.append(i*j)
        # print(i*j)



#%% EJERCICIO 1.51
# = = = = = = = = =

# Generar para cada provincia una tupla con el nombre de la
# provincia, su capital, su población y su PBI.


# La forma que creeo que pide:
# ----------------------------

Provincia = ["CABA", "Buenos Aires", "Catamarca", "Chaco", "Chubut", "Córdoba", "Corrientes", "Entre Ríos", "Formosa", "Jujuy", "La Pampa", "La Rioja", "Mendoza", "Misiones", "Neuquén", "Río Negro", "Salta", "San Juan", "San Luis", "Santa Cruz", "Santa Fe", "Santiago del Estero", "Tierra del Fuego", "Antártida e Isla del Atlántico Sur", "Tucumán"]

Capital = ["Ciudad Autónoma de Buenos Aires", "La Plata", "San Fernando del Valle de Catamarca", "Resistencia", "Rawson", "Córdoba", "Corrientes", "Paraná", "Formosa", "San Salvador de Jujuy", "Santa Rosa", "La Rioja", "Mendoza", "Posadas", "Neuquén", "Viedma", "Salta", "San Juan", "San Luis", "Río Gallegos", "Santa Fe", "Santiago del Estero", "Ushuaia", "San Miguel de Tucumán"]

Poblacion = [3075646, 17541141, 415438, 1204541, 618994, 3760450, 1120801, 1385961, 605193, 770881, 358428, 393531, 1990338, 1261294, 664057, 747610, 1424397, 781217, 508328, 365698, 3536418, 978313, 173432, 1694656]

PBI = [154863803, 292689868, 6150949, 69363739, 7968013, 9832643, 17747854, 20743409, 3807057, 6484938, 6990262, 5590516, 33431369, 9646826, 22564106, 10264584, 13438835, 8262309, 11780849, 11663738, 81588690, 8387859, 13856199, 7049276]


lg = []

for i in range(len(Provincia)-1):
    
    tupla = (Provincia[i], Capital[i], Poblacion[i], PBI[i])
    
    lg.append(tupla)


# Armar un diccionario donde cada valor sea la tupla de una
# provincia y la clave sea el nombre de la provincia.

dcp = dict()

for i in lg:
    
    dcp[i[0]] = (i[1:])

# Mostrar para cada provincia su PBI per capita.

for i in dcp:
    
    print('PBI %s:' %i, dcp[i][2])



#%% EJERCICIO 1.52
# = = = = = = = = =

# Construya un generador que vaya
# recorriendo la sucesión aritmética:
# 1, 2, 3, 4, 5 ...
# Imprima por pantalla los 10 primeros
# valores


def suc():
    
    vi = 1
    
    while True:
    
        yield vi
        
        vi = vi + 1


a = suc()
    
for i in range(10):
    
    print(next(a))



#%% EJERCICIO 1.53 (lo hizo el profe)
# = = = = = = = = = = = = = = = = = = = = 

# Construya un generador que vaya
# recorriendo la serie que va sumando la
# sucesión aritmética:
# 1, 2, 3, 6, 10, 15, 21 ...
# Imprima por pantalla los 10 primeros valores

def arit():
	numero = 0
	paso = 1
	while True:
		numero = numero + paso
		yield numero
		paso = paso + 1


serie = arit()

for i in range(70):
	print(next(serie))



#%% EJERCICIO 1.54 (hecho por el profe)
# = = = = = = = = = = = = = = = = = = =

# Tarea 1.54 
# Construya un generador que vaya recorriendo la serie geométrica: 1, 2, 4, 8, 16, 32, 64 …
# Imprima por pantalla los 10 primeros valores

def arit2():
	numero = 1
	while True:
		yield numero
		numero = numero * 2

#Programa

serie = arit2()

for i in range(100):
	print(next(serie), end = " ")
print("\n")


#%% EJERCICIO 1.55
# = = = = = = = = =

def generador():
    
    vi = 1
    
    while True:
        
        yield vi
        
        vi = vi*2 + 1


a = generador()

for i in range(10):
    
    print(next(a))


#%% EJERCICIO 1.56
# = = = = = = = = = 

# A partir del programa anterior recorrer las
# letras de las tres primeras ciudades de la
# lista y mostrar cada letra por pantalla en un
# nuevo renglón.


j = 0

for i in dcp:
    
    if j < 3:
    
        for k in i:
        
            print(k)
            
    j = j + 1



#%% EJERCICIO PARECIDO AL 1.58 (lo hizo el profe en clase):
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

#Programa que divide dos numeros ingresados por teclado por un usuario no muy inteligente

while True:
	try:
		num1 = int(input("Ingrese dividendo: "))
		break
	except ValueError:
		print("Valor incorrecto para el dividendo")

while True:
	try:
		num2 = int(input("Ingrese divisor: "))
		break
	except ValueError:
		print("Valor incorrecto para el divisor")

try:
	res = num1/num2
	print("El cociente entre", num1, "y", num2, "es", res)
except ZeroDivisionError:
	print("No se puede dividir por cero")

print("\n\nEND\n")



#%% EJERCICIO 1.77
# = = = = = = = = =

# Construya una clase que describa un
# modem genérico de los que los clientes
# tienen en sus casas.
# Ejemplo de propiedades:
# DNS primario
# DNS secundario
# Método: Usar DHCP


class modem():
    
    __DNS_1 = 123
    DNS_2 = 456
    
    def UsarDHCP(self):
        
        print('Acaba de usar DHCP')
    
    def verDNSPrimario(self):
        
        return self.__DNS_1
    
    def __str__(self):
        
        return "Se imprime esto en lugar de la direccion de memoria.\n"



hogar1 = modem()

print('El DNS primario es', hogar1.verDNSPrimario())
print('El DNS secundario es', hogar1.DNS_2)

hogar1.UsarDHCP()

print(hogar1)



#%% EJERCICIO 1.83-185...

# Creacion de clase
# -----------------

class modem():
    
    def __init__(self,marca1):
        
        self.__marca = marca1
        self.__modelo = "generico"
        self.__bytes = 0
    
    # Gets
    # ----
    
    def verMarca(self):
        
        return self.__marca
    
    def verModelo(self):
        
        return self.__modelo
    
    def verBytes(self):
        
        return self.__bytes
    
    
    # Sets
    # ----
    
    def modificarMarca(self, marca1):
        
        self.__marca = marca1
    
    def modificarModelo(self,modelo1):
        
        self.__modelo = modelo1
    
    def modificarBytes(self, cantidad = int()):
        
        self.__bytes = self.__bytes + cantidad


# Programa
# --------

# Crear una lista con 10 objetos del tipo modem.

ls = []

for i in range(10):
    
    modem_n = modem("generica")
    
    ls.append(modem_n)

# Reflejar una transmisión de 100 bytes por el
# primero, 200 por el segundo, ... y así hasta llegar
# al décimo.

j = 100
    
for i in ls:
    
    i.modificarBytes(j)
    
    j = j + 100

# Impresion de resultados de Bytes por modem
    
for i in range(1,11):
    
    print('El modem %s ha transmitido'%i , ls[i-1].verBytes(), 'bytes')


# Tomar la lista producida y sumar la cantidad total
# transmitida.
# Mostrar el total transmitido por pantalla.

j = 0

for i in ls:
    
    j = j + i.verBytes()

print('\nSe han transmitido en total %s Bytes' %j)

#%% EJERCICIO 1.86
# = = = = = = = = =

# Tarea 1.86
# Generar una clase Dispositivo con marca, modelo,
# potencia
# Generar una clase Switch que herede a
# Dispositivo
# Agregarle la propiedad encapsulada bocas que se
# podrá setear en el constructor y consultar


class Dispositivo():
    
    marca = "marca1"
    modelo = "modelo1"
    potencia = "potencia1"
    

# Generar una clase Switch que herede a
# Dispositivo
# Agregarle la propiedad encapsulada bocas que se
# podrá setear en el constructor y consultar

class Switch(Dispositivo):
    
    def __init__(self, bocas1):
        
        self.__bocas = bocas1
    
    def verBocas(self):
        
        return self.__bocas
        
# Programa

sw = Switch(3)

print("\nMarca de sw:", sw.marca)
print("Modelo de sw:", sw.modelo)
print("Potencia de sw:", sw.potencia)
print("N° de bocas de sw:", sw.verBocas())

#%% EJERCICIO 1.87
# = = = = = = = = =

# Continuando con la tarea 1.86
# Generar una clase Hub que herede a Dispositivo.
# Agregar una propiedad bocas, que esté
# encapsulada, pueda consultarse y modificarse.

class Hub(Dispositivo):

    def __init__(self, bocas1):
        
        self.__bocas = bocas1
        
    def verBocas(self):
            
        return self.__bocas
        
    def modificarBocas(self,bocasM):
        
        self.__bocas = bocasM


# Programa
 
hb = Hub(4)

print("\nN° de bocas de hb al instanciar la clase:", hb.verBocas())

hb.modificarBocas(10)

print("N° de bocas tras set", hb.verBocas())
