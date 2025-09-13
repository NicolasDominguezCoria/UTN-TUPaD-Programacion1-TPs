# TECNICATURA UNIVERSITARIA EN PROGRAMACION A DISTANCIA
# UNIVERSIDAD TECNOLOGICA NACIONAL

# ALUMNO: Daniel Nicolas Dominguez Coria, DNI: 35085946
# MATERIA: Programación 1
#Trabajo Practico Unidad 5, listas

# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

notas= [10,9,8,7,8,5,7,6,4,9]
print(f"lista de notas: {notas}")

notas= [10,9,8,7,8,5,7,6,4,9]
print(f"lista de notas: {notas}")

# CALCULO DE PROMEDIO
cantidad_notas= 10
suma_notas=0
for nota in notas:
    suma_notas += nota

promedio1= suma_notas/cantidad_notas
print(f"el promedio de las notas es {promedio1}")

# CALCULO NOTA MAS ALTA
nota_mayor1 =notas[0]
for nota in notas[1:]:
    if nota > nota_mayor1:
        nota_mayor1= nota
print(f"la notas mas alta es {nota_mayor1}")

# CALCULO NOTA MAS BAJA
nota_menor1= notas[0]
for nota in notas[1:]:
    if nota < nota_menor1:
        nota_menor1 = nota
print(f"la notas mas alta es {nota_menor1}")


#-------------------------------------------------------------------------------------------------
# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

lista_productos= []

for i in range(1,6):
    producto= input(f"ingrese el producto {i} de 5: ")
    lista_productos.append(producto)
    i += 1
print(f"lista de productos: {lista_productos}")

 # ORDENAR PRODUCTOS ALFABETICAMENTE
lista_productos_ordenada= sorted(lista_productos)
print(f"lista de productos ordenada alfabeticamente: {lista_productos_ordenada}")

 # PRODUCTO A ELIMINAR
x=0 #variable utilizada para el bucle
while x != 1:
    producto_eliminar= input("que producto deseas eliminar de la lista? ")
    if producto_eliminar in lista_productos_ordenada:
        lista_productos_ordenada.remove(producto_eliminar)
        print(f"se ha eliminado el producto {producto_eliminar}")
        print(f"lista actualizada: {lista_productos_ordenada}")
        x= 1
    else:
        print(f"no se encontró el producto {producto_eliminar} en la lista, intente nuevamente")


#-------------------------------------------------------------------------------------------------
#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

#GENERAR LISTADO DE NUMEROS
import random
numeros_aleatorios= [random.randint(1,100) for i in range(15)]
print(f"lista de numeros: {numeros_aleatorios}")

 #SEPARACION DEL LISTADO EN NUMEROS PARES E IMPARES
numeros_pares=[]
numeros_impares=[]

for numero in numeros_aleatorios:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

 #CALCULO DE CANTIDAD DE NUMEROS EN CADA LISTA
cantidad_pares= 0
for pares in numeros_pares:
    cantidad_pares += 1

cantidad_impares= 0
for impares in numeros_impares:
    cantidad_impares += 1

print(f"los numeros pares de la lista son {cantidad_pares}: {numeros_pares}")
print(f"los numeros impares de la lista son {cantidad_impares}: {numeros_impares}")


#-------------------------------------------------------------------------------------------------
#4) Dada una lista con valores repetidos: datos= [1,3,5,3,7,1,9,5,3]
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

datos= [1,3,5,3,7,1,9,5,3]
 #CREACION DE NUEVA LISTA ELIMINANDO REPETICIONES
datos_sin_repetir= []
for dato in datos:
    if dato not in datos_sin_repetir:
        datos_sin_repetir.append(dato)

print(f"listado con datos repetidos: {datos}")
print(f"listado eliminando repeticiones de datos: {datos_sin_repetir}")


#-------------------------------------------------------------------------------------------------
#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

lista_estudiantes= ["Juan", "Pedro", "Luis", "Carlos", "Daniel", "Jose", "Nicolas", "Pablo"]
print(f"lista estudiantes presentes: {lista_estudiantes}")

 #AGREGAR ESTUDIANTES
agregar_estudiante= input("Desea agregar un nuevo estudiante a la lista? (si/no):")

while agregar_estudiante == "si":
    nuevo_estudiante= input("ingrese el nombre del estudiante: ")
    lista_estudiantes.append(nuevo_estudiante)
    print(f"{nuevo_estudiante} a sido agregado a la lista")
    print((f"lista estudiantes actualizada: {lista_estudiantes}"))
    agregar_estudiante= input("Desea agregar otro estudiante a la lista? (si/no):")

 #ELIMINAR ESTUDIANTES
eliminar_estudiante= input("Desea eliminar un estudiante de la lista? (si/no):")

while eliminar_estudiante == "si":
    eliminar= input("ingrese el nombre del estudiante: ")
    if eliminar in lista_estudiantes:
        lista_estudiantes.remove(eliminar)
        print(f"{eliminar} a sido eliminado de la lista")
        print((f"lista estudiantes actualizada: {lista_estudiantes}"))
    else:
        print(f"{eliminar} no se encontró en la lista")
    eliminar_estudiante= input("Desea eliminar otro estudiante de la lista? (si/no):")

 #MENSAJE FINAL
print((f"lista estudiantes final: {lista_estudiantes}"))


#-------------------------------------------------------------------------------------------------
#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

lista= [1,2,3,4,5,6,7]
print(f"lista de numeros: {lista}")
rotar= input("desea rotar la lista un lugar a la derecha? (si/no)")

while rotar == "si":
    ultimo_elemento= lista[-1] #obtiene el último elemento
    resto_elementos= lista[:-1] #obtiene todos los elementos excepto el ultimo
    lista= [ultimo_elemento] + resto_elementos #rearma la lista con el ultimo elemento como primero
    print(f"lista rotada: {lista}")
    rotar= input("desea volver a rotar la lista un lugar a la derecha? (si/no)")

print(f"lista final: {lista}")


#-------------------------------------------------------------------------------------------------
#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
temperaturas= [[10,20],[11,22],[14,27],[12,23],[9,17],[7,20],[8,21]]
print("temperaturas minimas y máximas de la semana:")

#CONCATENA LOS DIAS CON SUS TEMPERATURAS
for i in range(len(dias_semana)):
    dia= dias_semana[i]
    temp= temperaturas[i]
    print(dia,temp)

#CALCULO DE LOS PROMEDIOS DE MAXIMA Y MINIMA
suma_min=0
suma_max=0
for dia in temperaturas:
    suma_min +=dia[0] #obtiene la suma de las temperaturas minimas
    suma_max +=dia[1] #obtiene la suma de las temperaturas maximas

num_dias=len(temperaturas) #obtiene el total de elementos de la lista
promedio_min=suma_min/num_dias #promedio te temperaturas minimas
promedio_max=suma_max/num_dias #promedio te temperaturas maximas

 #se imprime el resultado con dos decimales usando round para simplificarlo
print(f"el promedio de las temperaturas mínimas es {round(promedio_min,2)}") 
print(f"el promedio de las temperaturas máximas es {round(promedio_max,2)}")

#CALCULO DE AMPLITUD TERMICA (diferencia entre temp min y max)
maxima_amplitud= 0 #valor colocado a modo de iniciar la variable
dia_mayor_amplitud= ""

for i in range(len(temperaturas)):
    temp_dia= temperaturas[i]  #accede a las listas anidadas usando el indice i
    amplitud= temp_dia[1] - temp_dia[0]  #calcula la amplitud en cada lista anidada

    if amplitud > maxima_amplitud:
        maxima_amplitud = amplitud #compara las amplitudes y obtiene la amplitud maxima
        dia_mayor_amplitud = dias_semana[i] #obtiene el dia de las semana con el indice i

print(f"el día de mayor amplitud térmica ({maxima_amplitud}°) fué el día {dia_mayor_amplitud}")


#-------------------------------------------------------------------------------------------------
#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

notas_estudiantes= [[10,8,9],[7,7,8],[9,8,9],[7,10,5],[6,7,10]]
estudiantes= ["Juan", "Pedro", "Pablo", "Luis","Carlos"]
materias= ["Lengua", "Matemática", "Historia"]

 #PRESENTACION DE LA MATRIZ
print("MATRIZ CON NOTAS DE ESTUDIANTES EN LENGUA, MATEMÁTICA E HISTORIA:")
for i in range(len(estudiantes)): #concatenacion de listas
    estudiante= estudiantes[i] #obtiene los nombres de cada
    notas= notas_estudiantes[i] #obtiene las notas de cada estudiante
    print(estudiante, notas) #imprime cada estudiante con sus notas

 #CALCULO DE PROMEDIO GENERAL DE CADA ESTUDIANTE
print("\nPROMEDIO DE CADA ESTUDIANTE:")
for i in range(len(notas_estudiantes)):
    nota_estudiante= notas_estudiantes[i] #obtiene las notas de cada estudiante
    estudiante= estudiantes[i]

    suma_notas= 0 #variable para sumar las notas, se inicializa en 0 en cada iteracion para cada estudiante
    for nota in nota_estudiante:
        suma_notas += nota #suma las notas de cada estudiante

    promedio_estudiante = suma_notas / len(nota_estudiante) #calcula el promedio de cada estudiante
    print(f"Promedio de {estudiante}: {round(promedio_estudiante,2)}") #se usa round para mostrar solo dos decimales del promedio obtenido

 #CALCULO DE PROMEDIO POR MATERIA
numero_materias=len(notas_estudiantes[0]) #obtiene el numero de materias leyendo los elementos de la primer sublista (en todas son la misma cantidad)
numero_estudiantes= len(notas_estudiantes) #obtiene el numero de estudiantes 

print("\nPROMEDIO DE CADA MATERIA:")
for j in range(numero_materias): 
    materia= materias[j] #obtiene el nombre de cada materia de la lista materias
    suma_materia= 0 #variable para sumar las notas de cada materia, se inicializa en 0 en cada iteracion para cada materia
    for i in range(numero_estudiantes): 
        suma_materia += notas_estudiantes[i][j] #realiza la suma extrayendo en cada iteracion la nota de la materia de cada estudiante
    
    promedio_asignatura= suma_materia/numero_estudiantes #calculo del promedio
    print(f"promedio de {materia}: {round(promedio_asignatura,2)}") #se usa round para mostrar solo dos decimales del promedio obtenido


#-------------------------------------------------------------------------------------------------
# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

# ACLARACION IMPORTANTE: este ejercicio me resultó particularmente dificil, miré muchos tutoriales en youtube, explicaciones en diferentes foros y 
#                        documentacion de python para guiarme. Si bien todavia no hemos estudiado la definicion de funciones en la cursada me encontré
#                        en la necesidad de usar este recurso ya que resultó una forma eficiente de abordar la resolucion del ejercicio. Para el resto del código
#                        intenté amoldarme a lo estudiado hasta ahora. Por cualquier correccion, duda o consulta estoy a disposición del tutor. 

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

print("BIENVENIDO AL JUEGO DE TaTeTi")
print("En este juego hay dos jugadores: 'X' y 'O' (inicia el jugador X)")
print("para ingresar una jugada en el tablero tenés que escribir la fila (0, 1, 2) y luego la columna (0, 1, 2)")
print()

filas= len(tablero)
columnas= len(tablero[0])
jugador_actual = "X" #que guarda el simbolo del juegador que tiene el turno
jugadas = 0 #contador de jugadas

def verificar_ganador(tablero,jugador_actual): #verifica todas las posibles combinaciones para ganar el juego
    # Verificacion horizontal
    if tablero[0][0] == tablero[0][1] == tablero[0][2] == jugador_actual or tablero[1][0] == tablero[1][1] == tablero[1][2] == jugador_actual or tablero[2][0] == tablero[2][1] == tablero[2][2] == jugador_actual:
        return True
    # Verificacion vertical
    if tablero[0][0] == tablero[1][0] == tablero[2][0] == jugador_actual or tablero[0][1] == tablero[1][1] == tablero[2][1] == jugador_actual or tablero[0][2] == tablero[1][2] == tablero[2][2] == jugador_actual:
        return True
    # Verificar en diagonal
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador_actual:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador_actual:
        return True
    return False

while jugadas < 9: #el tablero posee nueve "casilleros" es decir nueve posibles 
    for fila in range(filas): #imprime el tablero en cada iteracion
        for columna in range(columnas):
            print(tablero[fila][columna], end=" ")
        print()
    
    print(f"\nJugador'{jugador_actual}' ingresa tu jugada") # pide su jugada al jugador actual
    
    fila = int(input("Ingresa la fila del casillero (0, 1, 2): "))
    columna = int(input("Ahora Ingresa la columna del casillero (0, 1, 2): "))
    
    # verifica si el casillero está vacío y es válido
    if 0 <= fila <= 2 and 0 <= columna <= 2 and tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador_actual
        jugadas += 1 # Coloca la marca del jugador en el tablero

        if verificar_ganador(tablero,jugador_actual): #verifica si hay alguna combinacion ganadora
            for fila in range(filas):
                for columna in range(columnas): 
                    print(tablero[fila][columna], end=" ") #muestra el tablero por ultima vez
                print() #espacio en blanco
            print(f"Felicidades jugador '{jugador_actual}', haz ganado el TaTeTi!")
            break #finaliza el bucle en caso de haya una combinacion ganadora (no es una buena practica pero para este caso es aplicable)

        # Cambiar al siguiente jugador
        if jugador_actual == "X":
            jugador_actual = "O"
        else:
            jugador_actual = "X"
    else:
        print("¡Error! La posición no es válida o ya está ocupada. Intenta de nuevo.")
            
print("¡Juego terminado!") #mensaje final


#-------------------------------------------------------------------------------------------------
#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.

#ACLARACION: al igual que el ejercicio anterior

lista_productos= ["arroz", "fideos", "leche", "queso"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
lista_ventas = [
    [5, 6, 7, 10, 9, 8, 5], # arroz
    [6, 6, 5, 3, 10, 8, 7],   # fideos
    [5, 2, 1, 8, 2, 9, 8],  # leche
    [7, 4, 6, 1, 9, 3, 2]  # queso
]

#PRESENTACION DE LA MATRIZ
print("MATRIZ DE PRODUCTOS Y SUS VENTAS DE LUNES A DOMINGO:")
for i in range(len(lista_productos)):
    producto= lista_productos[i]
    ventas= lista_ventas[i]
    print(producto, ventas)

#CALCULO DEL TOTAL DE VENTAS DE CADA PRODUCTO
print("\nTOTAL DE VENTAS DE CADA PRODUCTO:")
for i in range(len(lista_ventas)):
    producto= lista_productos[i]
    ventas= lista_ventas[i]
    suma_venta=0
    for venta in ventas:
        suma_venta += venta
    print(f"total vendido de {producto}: {suma_venta}")

#CALCULO DIA CON MAYORES VENTAS
print("\nDIA DE MAYORES VENTAS:")

ventas_por_dia = [] #creamos una nueva lista donde se acumulará el total de ventas de cada dia

for j in range(len(lista_ventas[0])): # recorre los días (columnas)
    suma_dia = 0
    for i in range(len(lista_ventas)): #recorre los productos (filas) para sumar las ventas del día 'j'
        suma_dia += lista_ventas[i][j] #suma cada elemento dentro de cada sublista
    ventas_por_dia.append(suma_dia) #guarda el valor obtenido en la nueva lista creada

#a modo de agregar informacion mostramos la matriz con el total de ventas de cada dia
for i in range(len(dias)): 
    dia= dias[i]
    total_venta= ventas_por_dia[i]
    print(f"{dia}: {total_venta}") #muestra el total de ventas de cada dia

#calculamos el dia con mas vantas a partir de la lista anterior
dia_con_mas_ventas= ventas_por_dia[0] # tomamos como referencia el primer elemento de la lista
indice_dia_con_mas_ventas= 0 # indice del primer elemento

for f in range(1, len(ventas_por_dia)): #recorre la lista en busca del mayor valor, iniciando por el segundo elemento
    elemento_actual= ventas_por_dia[f]
    if elemento_actual > dia_con_mas_ventas:
        dia_con_mas_ventas= elemento_actual  #compara y actualiza en caso de que encuentre un mayor valor
        indice_dia_con_mas_ventas= f #actualiza el indice

print(f"El día con mas ventas es {dias[indice_dia_con_mas_ventas]} con {dia_con_mas_ventas} ventas")


#CALCULO DE PRODUCTO MAS VENDIDO
print("\nPRODUCTO MAS VENDIDO DE LA SEMANA:")

ventas_por_producto= [] #creamos una nueva lista donde se guardaran los totales de venta por producto

for fila in lista_ventas: #sumamos las ventas de cada producto
    suma_total_producto= 0 #se inicializa la variable que acumula la suma de ventas
    for total in fila:
        suma_total_producto += total #se realiza la suma
    ventas_por_producto.append(suma_total_producto) #se guarda el valor obtenido en la lista creada para ello

for i in range(len(lista_productos)): 
    prod= lista_productos[i]
    total_venta_producto= ventas_por_producto[i]
    print(f"{prod}: {total_venta_producto}")

producto_mas_vendido= ventas_por_producto[0] #tomamos con referencia el primer producto
indice_producto_mas_vendido = 0 #indice del primer producto

for f in range(1, len(ventas_por_producto)): #recorre la lista en busca del mayor valor, iniciando por el segundo elemento
    if ventas_por_producto[f] > producto_mas_vendido:
        producto_mas_vendido = ventas_por_producto[f] #compara y actualiza en caso de que encuentre un mayor valor
        indice_producto_mas_vendido = f #actualiza el indice 

print(f"El producto con mas ventas es {lista_productos[indice_producto_mas_vendido]} con {producto_mas_vendido} ventas")

