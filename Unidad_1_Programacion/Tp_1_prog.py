# TECNICATURA UNIVERSITARIA EN PROGRAMACION A DISTANCIA
# UNIVERSIDAD TECNOLOGICA NACIONAL

# ALUMNO: Daniel Nicolas Dominguez Coria, DNI: 35085946

#Trabajo Practico N°1, Unidad 1, programacion 1

# 1- Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print ("Hola Mundo!")

# 2- Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
# Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”.
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
nombre= input("Escribe tu nombre: " )
print(f"Hola {nombre}!")

# 3- Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima porpantalla una oración con los datos ingresados.
# Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”,el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”.
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
nombre= input("Ingresa tu nombre: " )
apellido= input("Ingresa tu apellido: ")
edad= input("Ingresa tu edad:")
residencia= input("Ingresa tu pais de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4- Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
radio= int(input("Ingresa el radio del circulo: "))
pi= 3.141592
area= (pi * radio)**2
perimetro= (2*pi*radio)
print (f"El area del circulo es {area} y su perímetro es {perimetro}")

# 5- Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
# (1 hora = 3600 segundos)
segundos= int(input("Ingrese la cantidad de segundos:"))
hora= segundos / 3600
print(f"los {segundos} segundos ingresados equivalen a {hora} horas")

# 6- Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numero= int(input("Ingrese un numero para mostrar su tabla de multiplicar:"))
print(f"la tabla de multiplicar del {numero} es")
print(f"{numero} x 1 = ", numero*1)
print(f"{numero} x 2 = ", numero*2)
print(f"{numero} x 3 = ", numero*3)
print(f"{numero} x 4 = ", numero*4)
print(f"{numero} x 5 = ", numero*5)
print(f"{numero} x 6 = ", numero*6)
print(f"{numero} x 7 = ", numero*7)
print(f"{numero} x 8 = ", numero*8)
print(f"{numero} x 9 = ", numero*9)
print(f"{numero} x 10 = ", numero*10)

# 7- Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1= int(input("Ingrese un primer numero distinto de cero: "))
num2= int(input("Ingrese un segundo numero distinto de cero: "))
suma= num1+num2
resta= num1-num2
multiplicacion= num1*num2
division= num1/num2
print(f"la suma de {num1} y {num2} es: {suma}")
print(f"la resta de {num1} y {num2} es: {resta}")
print(f"la multiplicación de {num1} y {num2} es: {multiplicacion}")
print(f"la división de {num1} y {num2} es: {division}")

# 8- Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
# Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: IMC= peso en Kg /(altura en metros)^2
altura= float(input("Ingrese su altura expresada en metros: "))
peso= float(input("Ingrese su peso expresado en kg: "))
imc= peso/altura**2
print(f"Su indice de masa corporal es {imc}")

# 9- Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
# Tener en cuenta la siguiente equivalencia: temp en F° = (9/5) * temp en C° + 32
celsius= float(input("Ingrese una temperatura en grados Celsius: "))
fahrenheit= (9/5) * celsius + 32
print( f"la temperatura expresada en grados fahrenheit es {fahrenheit}" )

# 10- Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
num1= int(input("Ingrese un primer numero: "))
num2= int(input("Ingrese un segundo numero: "))
num3= int(input("Ingrese un tercer numero: "))
promedio= (num1+num2+num3)/3
print( f"el promedio de{num1}, {num2} y {num3} es: {promedio}" )