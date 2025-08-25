# TECNICATURA UNIVERSITARIA EN PROGRAMACION A DISTANCIA
# UNIVERSIDAD TECNOLOGICA NACIONAL

# ALUMNO: Daniel Nicolas Dominguez Coria, DNI: 35085946
# MATERIA: Programación 1
#Trabajo Practico Unidad 3, estructuras condicionales

# 1) Escribir un programa que solicite la edad del usuario.
#    Si el usuario es mayor deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad_usuario= int(input("ingrese su edad: " ))
if edad_usuario > 18:
    print("Es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario.
#    Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”;
#    en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota_usuario= int(input("ingrese la nota recibida: " ))
if nota_usuario >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares.
#   Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par";
#   en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".
#   Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

numero_usuario= int(input("ingrese un numero: "))

if numero_usuario % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#  ● Niño/a: menor de 12 años.
#  ● Adolescente: mayor o igual que 12 años y menor que 18 años.
#  ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#  ● Adulto/a: mayor o igual que 30 años.

edad_usuario= int(input("Ingrese su edad: "))
if edad_usuario < 0:
    print ("Edad no valida, por favor ingrese una edad valida")
elif edad_usuario >= 0 and edad_usuario <= 11:
    print("Usted pertenece a la categoría Niño")
elif edad_usuario >= 12 and edad_usuario <= 17:
    print("Usted pertenece a la categoría Adolescente")
elif edad_usuario >= 18 and edad_usuario <= 29:
    print("Usted pertenece a la categoría Adulto/a joven")
else:
    print ("Usted pertenece a la categoría Adulto/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14).
#  Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta";
#  en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
#  Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

contrasenia_usuario= input("Ingrese una contraseña que contenga entre 8 y 14 caracteres: ")
longitud_contrasenia= len(contrasenia_usuario)

if longitud_contrasenia >= 8 and longitud_contrasenia <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y
#   las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mode, median, mean
import random

numeros_aleatorios= [random.randint(1,100) for i in range(50) ]
moda= mode(numeros_aleatorios)
mediana= median(numeros_aleatorios)
media= mean(numeros_aleatorios)

print(f"Lista de 50 números aleatorios entre 1 y 100: {numeros_aleatorios}")

if media > mediana and mediana > moda:
    print(f"La lista contiene un SESGO POSITIVO ya que la media es {media}, la mediiana es {mediana} y la moda es {moda}.")
elif media < mediana and mediana < moda:
    print(f"La lista contiene un SESGO NEGATIVO ya que la media es {media}, la mediana es {mediana} y la moda es {moda}.")
else:
    print(f"La lista no contiene sesgo ya que la media es {media}, la mediana es {mediana} y la moda es {moda}")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal,
#   añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario,
#   dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

palabra_usuario= input("Ingrese una palabra o frase: ")
palabra_minuscula= palabra_usuario.lower()
if palabra_minuscula[-1] == "a" or palabra_minuscula[-1] == "e" or palabra_minuscula[-1] == "i" or palabra_minuscula[-1] == "o" or palabra_minuscula[-1] == "u":
    resultado = palabra_usuario + "!"
else:
    resultado = palabra_usuario

print(resultado)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#   1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#   2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#   3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#   El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.
#   Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre_usuario= input("Ingrese su nombre completo: ")
print("sellecione como le gustaría que se escriba su nombre:")
print(" - ingrese 1 si quiere su nombre en mayúsculas ")
print(" - ingrese 2 si quiere su nombre en minúsculas ")
print(" - ingrese 3 si quiere su nombre en mayúsculas ")
seleccion= int(input("ingrese su opción: "))

if seleccion == 1:
    print(nombre_usuario.upper())
elif seleccion == 2:
    print(nombre_usuario.lower())
elif seleccion == 3:
    print(nombre_usuario.title())
else:
    print("el numero ingresado no es valido")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes 
# categorías según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud_terremoto= float(input("Ingrese la magrnitud del terremoto: "))

if magnitud_terremoto > 0 and magnitud_terremoto < 3:
    print("Terremoto Muy Leve (imperceptible)")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    print("Terremoto Leve (ligeramente perceptible)")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
    print("Terremoto Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
    print("Terremoto Fuerte (puede causar daños en estructuras débiles)")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
    print("Terremoto Muy Fuerte (puede causar daños significativos)")
elif magnitud_terremoto >= 7:
    print("Terremoto Extremo (puede causar graves daños a gran escala)")
else:
    print("no ocurrió terremoto")

# 10) Utilizando la información aportada en la tabla sobre las estaciones del año 
#   escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es.
#   El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio= input("ingrese en que hemisferio se encuentra (Norte o Sur): ")
hemis_min= hemisferio.lower() # pasa a minuscula el dato de hemisferio ingresado
mes= input("especifique el mes del año: ")
mes_min= mes.lower() # pasa a minuscula el dato de mes ingresado

dia= int(input("por último, ingrese el día del mes: "))

if hemis_min == "sur" and ((mes_min == "diciembre" and dia > 20 and dia < 32) or (mes_min == "enero" and dia > 0 and dia < 32) or (mes_min == "febrero" and dia > 0 and dia < 30) or (mes_min == "marzo" and dia > 0 and dia < 21)): 
    print(f"Si usted está en el hemisferio {hemisferio}, en la fecha {dia} de {mes}, Usted se encuentra en VERANO") # Desde el 21 de diciembre hasta el 20 de marzo SUR
elif hemis_min == "norte" and ((mes_min == "diciembre" and dia > 20 and dia < 32) or (mes_min == "enero" and dia > 0 and dia < 32) or (mes_min == "febrero" and dia > 0 and dia < 30) or (mes_min == "marzo" and dia > 0 and dia < 21)):
    print(f"Si usted está en el hemisferio {hemisferio}, en la fecha {dia} de {mes}, Usted se encuentra en INVIERNO") # Desde el 21 de diciembre hasta el 20 de marzo NORTE
elif hemis_min == "sur" and ((mes_min == "marzo" and dia > 20 and dia < 32) or (mes_min == "abril" and dia > 0 and dia < 31) or (mes_min == "mayo" and dia > 0 and dia < 30) or (mes_min == "junio" and dia > 0 and dia < 21)):
    print(f"Si usted está en el hemisferio {hemisferio}, en la fecha {dia} de {mes}, Usted se encuentra en OTOÑO") # Desde el 21 de marzo hasta el 20 de junio SUR
elif hemis_min == "norte" and ((mes_min == "marzo" and dia > 20 and dia < 32) or (mes_min == "abril" and dia > 0 and dia < 31) or (mes_min == "mayo" and dia > 0 and dia < 31) or (mes_min == "junio" and dia > 0 and dia < 21)):
    print(f"Si usted está en el hemisferio {hemisferio}, en la fecha {dia} de {mes}, Usted se encuentra en PRIMAVERA") # Desde el 21 de marzo hasta el 20 de junio NORTE
elif hemis_min == "sur" and ((mes_min == "junio" and dia > 20 and dia < 31) or (mes_min == "julio" and dia > 0 and dia < 32) or (mes_min == "agosto" and dia > 0 and dia < 32) or (mes_min == "septiembre" and dia > 0 and dia < 21)):
    print(f"Si usted está en el hemisferio {hemisferio}, en la fecha {dia} de {mes}, Usted se encuentra en INVIERNO") # Desde el 21 de junio hasta el 20 de septiembre SUR
elif hemis_min == "norte" and ((mes_min == "junio" and dia > 20 and dia < 31) or (mes_min == "julio" and dia > 0 and dia < 32) or (mes_min == "agosto" and dia > 0 and dia < 32) or (mes_min == "septiembre" and dia > 0 and dia < 21)):
    print(f"Si usted está en el hemisferio {hemisferio}, en la fecha {dia} de {mes}, Usted se encuentra en VERANO") # Desde el 21 de junio hasta el 20 de septiembre NORTE
elif hemis_min == "sur" and ((mes_min == "septiembre" and dia > 20 and dia < 31) or (mes_min == "octubre" and dia > 0 and dia < 32) or (mes_min == "noviembre" and dia > 0 and dia < 31) or (mes_min == "diciembre" and dia > 0 and dia < 21)):
    print(f"Si usted está en el hemisferio {hemisferio}, en la fecha {dia} de {mes}, Usted se encuentra en PRIMAVERA") # Desde el 21 de septiembre hasta el 20 de diciembre SUR
elif hemis_min == "norte" and ((mes_min == "septiembre" and dia > 20 and dia < 31) or (mes_min == "octubre" and dia > 0 and dia < 32) or (mes_min == "noviembre" and dia > 0 and dia < 31) or (mes_min == "diciembre" and dia > 0 and dia < 21)):
    print(f"Si usted está en el hemisferio {hemisferio}, en la fecha {dia} de {mes}, Usted se encuentra en OTOÑO") # Desde el 21 de septiembre hasta el 20 de diciembre NORTE
else:
    print(f"usted ingresó los datos: hemisrefio {hemisferio}, dia {dia} del mes de {mes}.")
    print("algún dato fue mal ingresado, revise la ortografia o la fecha ingresada e intente nuevamente") #por si se ingresan datos no validos en la estructura condicional