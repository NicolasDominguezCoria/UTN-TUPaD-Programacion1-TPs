# TECNICATURA UNIVERSITARIA EN PROGRAMACION A DISTANCIA
# UNIVERSIDAD TECNOLOGICA NACIONAL

# ALUMNO: Daniel Nicolas Dominguez Coria, DNI: 35085946
# MATERIA: Programación 1
# Trabajo Practico Unidad 6, funciones

#1. Crear una función llamada imprimir_hola_mundo que imprima por 
#   pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo(): #funcion
    print("Hola Mundo!")   #cuerpo de la funcion

imprimir_hola_mundo() #llamado a la funcion

#2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
#   Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”.
# Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre): #funcion 
    print(f"Hola {nombre}!.") #mensaje de salida

nombre= input("Ingresa tu nombre: ") # variable que recibe la informacion del usuario
saludar_usuario(nombre) # llamada a la funcion con mensaje de salida 


#3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia)
#   que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
#   Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia): # funcion
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}") #mensaje de salida

nombre = input("Ingresa tu nombre: ") #variable para ingresar nombre
apellido = input("Ingresa tu apellido: ") #variable para ingresar apellido
edad = input("Ingresa tu edad: ") #variable para ingresar edad
residencia = input("Ingresa tu pais de residencia: ") #variable para ingresar pais de residencia

informacion_personal(nombre, apellido, edad, residencia) #llamada a la funcion con mensaje de salida


#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
#   calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
#   Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

from math import pi #se importa la pi(3,14159....) desde la librerpia math 

def calcular_area_circulo(radio): #funcion para calcular el area
    area_circulo = pi * (radio ** 2) #variable donde se realiza el cálculo del area
    print(f"el area del circulos es: {round(area_circulo,2)}") # mensaje de salida con el resultado (se usa la funcion round para mostrar solo dos decimales)

def calcular_perimetro_circulo(radio): #funcion para calcular el perimetro
    perimetro_circulo = 2 * pi * radio #variable donde se realiza el calculo del perímetro
    print(f"el perimetro del circulos es: {round(perimetro_circulo,2)}") # mensaje de salida con el resultado (se usa la funcion round para mostrar solo dos decimales)

radio = float(input("ingrese el radio del círculo: ")) #variable donde se solicita al usuario el radio, se utiliza la funcio float para poder ingresar numeros con decimal
calcular_area_circulo(radio) #llamada a la funcion que calcula e imprime el area
calcular_perimetro_circulo(radio) #llamada a la funcion que calcula e imprime el perimetro


#5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y
#   devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos): #funcion
    horas= segundos / 3600 #variable que calcula el valor de segundos a horas
    print(f"{segundos} segundos equivalen a {round(horas,2)} hora/s") #mensaje de salida con valor de segundos en horas, se utilizó "round" para mostrar solo dos decimales.

segundos = int(input("Ingrese los segundos para transformarlos en horas: ")) #variable que solicita al usuario el valor en segundos
segundos_a_horas(segundos) #llamada a la funcion que transforma de segundos a horas


#6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro e imprima
#   la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero): #funcion
    print (f"tabla de multiplicar del 1 al 10 de {numero}:") #mensaje encabezado de la tabla creada
    for i in range(1, 11):  #funcion for para realizar la tabla e imprimirla en pantalla
        resultado = numero * i #variable que guarda el resultado de la multiplicacion en cada iteracion
        print(f"  {numero} x {i} = {resultado}") #mensaje de salida con resultado en cada iteracion


numero = int(input("Ingrese un numero entero: ")) #variable que recibe el numero cargado por el usuario
tabla_multiplicar(numero) #llamada a la funcion que muestra la tabla del numero ingresado


#7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con
# el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b): #funcion
    suma = a + b #variable que calcula la suma
    resta = a - b #variable que calcula la resta
    multiplicacion = a * b #variable que calcula la multiplicacion
    
    if b != 0: #condicional que veridica si el segundo numero es distinto de cero
        division = a / b #si es distinto de cero
    else: #si es cero solo se imprimer un mensaje, ya que si se hiciera el calculo python nos marcaría un error
        division = "indefinido"

    return (suma, resta, multiplicacion, division) #empaquetado de las variables para que sea una tupla

num1= float(input("Ingrese el primer número: ")) # variable que recibe el primer numero, al ser un float puede contener coma
num2= float(input("Ingrese el segundo número: ")) # variable que recibe el segundo numero, al ser un float puede contener coma
suma, resta, multiplicacion, division= operaciones_basicas(num1,num2) #llamada a la funcion y desempaquetado de las variables de la tupla

print(f"\nOperaciones básicas de {num1} y {num2}: ") #mensaje encabezado de la operacion realizada
# Impresion de resultados de todas las operaciones de forma clara
print(f" Suma → {num1} + {num2} = {suma}\n Resta → {num1} - {num2} = {resta}\n Multiplicacion → {num1} x {num2} = {multiplicacion}\n Division → {num1} : {num2} = {division}")


#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros,
#   y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura): #funcion
    imc= peso / (altura**2) #variable que realiza el cálculo de indice de masa corporal
    #condicional (adicional) que verifica el diagnóstico segun el resultado del imc.(datos extraidos de internet)
    diagnostico= ""
    
    if imc <= 18.5: 
        diagnostico = "Debajo de lo normal"
    elif imc <= 24.9:
        diagnostico = "Normal"
    elif imc <= 29.9:
        diagnostico = "Sobrepeso"
    elif imc  <= 34.9:
        diagnostico = "Obesidad I"
    elif imc <= 39.9:
        diagnostico = "Obesidad II"
    elif imc >= 40:
        diagnostico = "Obesidad III"
    
    print(f"Su indice de masa corporal es: {round(imc,2)} kg/m2, su diagnóstico es: '{diagnostico}'.") #mensaje de salida con valor de imc y diagnóstico

peso = float(input("Ingresa tu peso en Kg: ")) #variable que acumula el valor del peso en kg
altura = float(input("Ingresa tu altura en metros: ")) #variable que acumula el valor del peso en metros
calcular_imc(peso,altura) #llamada a la funcion



#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
#   Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius): #funcion
    fahrenheit = 1.8 * celsius + 32 #variable que realiza el pasaje de celsius a fahrenheit
    print(f"la tempertura {celsius} en grados celsius equivale a {fahrenheit} grados farhenheit") #mensaje de salida con conversion de temperaturas

celsius= float(input("Iingresa una temperatura en grados celsius: ")) #variable que acumula el valor ingresado por el ususario en celsius
celsius_a_fahrenheit(celsius) #llamado a la funcion con impresion del resultado


#10. Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
#    Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c): #funcion
    promedio = (a + b + c)/3 #variable que realiza el calculo del promedio
    print(f"El promedio de {a}, {b} y {c} es: {round(promedio,2)}") #mensaje de salida con el resultado

num1= float(input("ingrese el primer numero: ")) #acumula el valor del primer numero
num2= float(input("ingrese el segundo numero: ")) #acumula el valor del segundo numero
num3= float(input("ingrese el tercer numero: ")) #acumula el valor del tercer numero
calcular_promedio(num1,num2,num3) #llamada a la funcion que realiza el calculo del primedio y lo imprime en pantalla