# TECNICATURA UNIVERSITARIA EN PROGRAMACION A DISTANCIA
# UNIVERSIDAD TECNOLOGICA NACIONAL

# ALUMNO: Daniel Nicolas Dominguez Coria, DNI: 35085946
# MATERIA: Programación 1
#Trabajo Practico Unidad 4, estructuras repetitivas

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#   (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for num in range (101):
    print(num)


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero_usuario= int(input("ingrese un numero entero: "))
numero_usuario_original = numero_usuario # guarda el valor original del numero ingresado
contador_digitos= 0

if numero_usuario != 0:
    while numero_usuario > 0:
        numero_usuario //= 10
        contador_digitos += 1
    print (f"el numero {numero_usuario_original} tiene {contador_digitos} digitos")
else:
    print( "el numero 0 contiene 1 digito")


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

numero_usuario_inicial= int(input("ingrese un numero inicial: "))
numero_usuario_final= int(input("ingrese un numero final: "))
suma= 0

if numero_usuario_inicial == numero_usuario_final:
    print("los numeros ingresados son iguales, ingrese numeros con valor diferente")
elif numero_usuario_inicial > numero_usuario_final:
    numero_usuario_inicial, numero_usuario_final = numero_usuario_final, numero_usuario_inicial

for digito in range (numero_usuario_inicial+1,numero_usuario_final):
    suma += digito 

print(f"la suma de los numero comprendidos entre {numero_usuario_inicial} y {numero_usuario_final} (excluyendolos) es {suma}")


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia.
#    El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

numero_usuario= int(input("ingrese un numero entero distinto de cero: "))
suma= 0

while numero_usuario != 0:
    suma += numero_usuario
    print("Resultado parcial:", suma)
    numero_usuario = int(input("ingrese otro numero entero para ser sumado o 0 para terminar: "))

print ("la suma total de los numeros ingresados es:", suma)


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9.
#    Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero_a_adivinar= random.randint(0,9)
print("el juego consiste en adivinar un numero secreto.")
numero_usuario=  int(input("Por favor, ingrese un número entero entre 0 y 9: "))
intentos= 0

if numero_usuario >= 0 and numero_usuario < 10:
    while numero_a_adivinar != numero_usuario:
        intentos += 1
        numero_usuario=  int(input("Incorrecto, intente nuevamente: "))

print(f"Felicidades, el numero secreto es {numero_a_adivinar}")
print(f"numero de intentos: {intentos}")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for numero in range (100,-1,-2):
    print(numero)


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#    número entero positivo indicado por el usuario.

numero_final= int(input("Por favor ingrese un numero entero positivo y distinto de cero: "))
suma= 0
if numero_final > 0:
    for numero_inicial in range(0,numero_final):
        suma += numero_inicial

    print(f"la suma de todos los numeros entre 0 y {numero_final} es {suma}")
else:
    print("el numero ingresado no es valido")


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#    programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#    negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#    menor, pero debe estar preparado para procesar 100 números con un solo cambio).

numeros_pares= 0
numeros_impares= 0
numeros_positivos= 0
numeros_negativos= 0
ceros_ingresados= 0

for iterador in range(100):
    numero_usuario= int(input("Ingrese un numero entero (puede ser positivo o negativo, pero no cero): "))
    
    if numero_usuario != 0:
        if numero_usuario % 2 == 0:
            numeros_pares += 1
        else: 
            numeros_impares += 1
    else:
        ceros_ingresados += 1
            #ACLARACION: se permite al usuario ingresar el numero cero no suma como para, impar, positivo o negativo.
                    # Si bien el ejercicio no lo solicita, como adicional se agregó una variable que cuanta los ceros que se ingresaron.  
    if numero_usuario > 0:
        numeros_positivos += 1
    elif numero_usuario < 0:
        numeros_negativos += 1

print(f"Usted ingresó {numeros_pares} numeros pares, {numeros_impares} numeros impares, {numeros_positivos} numeros positivos y {numeros_negativos} numeros negativos")
print(f"Tambien ingresó {ceros_ingresados} el numero cero")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#   media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#   poder procesar 100 números cambiando solo un valor).

ingresos= 100 #cantidad de numeros que se permite ingresar
suma= 0

for i in range(ingresos): #i es iterador
    numero_usuario= int(input("ingrese un numero entero: "))
    suma += numero_usuario

media= suma/ingresos 
print(f" la media de los numero ingresados es {media}")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#    usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero_usuario= int(input("Ingrese un numero: "))
numero_usuario_original= numero_usuario #guarda el valor original del nimero ingresado
numero_invertido= 0

while numero_usuario > 0:
    ultimo_digito = numero_usuario % 10                      #obtiene el ultimo digito del numero ingresado
    numero_invertido = numero_invertido*10 + ultimo_digito   #mueve el valor un espacio agregandole un 0 y luego ingresa el ultimo digito obtenido
    numero_usuario //= 10                                    #elimina el ultimo digito del numero ingresado para continuar con el siguiente en la siguiente iteracion

print(f"el numero{numero_usuario_original} invertido se escribe {numero_invertido}")
