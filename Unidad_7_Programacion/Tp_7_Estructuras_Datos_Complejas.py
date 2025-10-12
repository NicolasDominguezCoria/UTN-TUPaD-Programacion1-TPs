# TECNICATURA UNIVERSITARIA EN PROGRAMACION A DISTANCIA
# UNIVERSIDAD TECNOLOGICA NACIONAL

# ALUMNO: Daniel Nicolas Dominguez Coria, DNI: 35085946
# MATERIA: Programación 1
# Trabajo Practico Unidad 7, Estructuras de datos complejas

#ACLARACION: El trabajo desarrollado en los ejercicios de este TP no se enfocó tanto el prestar atención a agregar
#            validaciones en los inputs o la modularizacion de las funcionaes que podrian robustecer y mejorar el código, sino que se enfocó especialmente
#            en lograr que las funcionalidades solicitadas en cada ejercicio (en el trabajo con tuplas, listas, sets y diccionarios) se ejecuten correctamente.
#            


#1) Dado el diccionario precios_frutas
#   precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#   Añadir las siguientes frutas con sus respectivos precios: Naranja= 1200 ; Manzana= 1500 ; pera= 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} #diccionario inicial
print(f'Diccionario de precios original: {precios_frutas}') #Imprime el diccionario con su informacion interna inicial

#carga de nuevas pareja solicitadas
precios_frutas['Naranja'] = 1200 
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

   #Puede hacerse tambien con la función .update() creando una nueva diccionario con los nuevos key-value a y agregandolos al diccionario existente 
#nuevas_frutas = {'Naranja': 1200 , 'Manzana': 1500 , 'Pera': 2300}
#precios_frutas.update(nuevas_frutas)

print(f'1. Diccionario de precios con nuevas frutas:{precios_frutas}') #Imprime el diccionario con la nueva informacion agregada



#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado
#   en el punto anterior, actualizar los precios de las siguientes frutas:  Banana = 1330 ; Manzana = 1700 ; Melón = 2800

#Actualiza los values de las keys mencionadas
precios_frutas['Banana'] = 1330 
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

   #Puede hacerse tambien con la función .update() creando una nuevo diccionario con los valores a actualizar y agregandolos al diccionario existente 
#nuevos_valores = {'Banana': 1330 , 'Manzana': 1700 , 'Melón': 2800}
#precios_frutas.update(nuevos_valores)

print(f'2. Diccionario de precios con valores actualizados:{precios_frutas}')



#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior,
#   crear una lista que contenga únicamente las frutas sin los precios.

#extrae las keys utilizando la funcion integrada .keys()
frutas = precios_frutas.keys()

    #Tambien puede hacerse con la funcion 'list' de python y se obtiene un resultado mas limpio (sin "dict_keys..")
#frutas = list(precios_frutas)

print(f'3. Lista de frutas disponibles: {frutas}')



# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
#    • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#    • Luego, pedí un nombre y mostrale el número asociado, si existe.

numeros_telefonicos= {} #diccionario vacio donde se guardarán los contactos
print("Bienvenido a tu agenda de contactos!.\n Por favor a continuación cargá los cinco primeros contactos:") #mensaje de bienvenida

for i in range(5): #Para ingresar los cinco contacto usamos un bucle for con 5 iteraciones definidas
    nombre= input(f' Ingresa el nombre del contacto {i+1}: ') #recibe el nombre del contacto (Key)
    numero= int(input(f' Ingresa el numero telefónico de {nombre}: ')) #recibe el número del contacto como un entero (value)
    numeros_telefonicos[nombre] = numero #agrega al diccionario el nuevo contacto
    print() #simula un espacio en blanco para una interfaz mas limpia

print(f'\n Los cinco contactos iniciales han sido cargados correctamente:\n  {numeros_telefonicos}') #mensaje al finalizar el bucle e impresion del diccionario


buscar_contacto= input('\nIngresa el nombre del contacto que quieres buscar: ') #recibe el nombre (key) del contacto a buscar en el diccionario

if buscar_contacto in numeros_telefonicos: #condicional que comprueba si el nombre (key) existe en el diccionario
    print(f'  El número de {buscar_contacto} es {numeros_telefonicos[buscar_contacto]}')  # mensaje de salida si existe
else:
    print('  Ese contacto no existe en la agenda.')  #mensaje de salida si no existe



#5) Solicita al usuario una frase e imprime:
#   • Las palabras únicas (usando un set).
#   • Un diccionario con la cantidad de veces que aparece cada palabra.

frase_usuario = input("Bienvenido!. Por favor ingresá una frase: ") #contiene la frase ingresada por el usuario

palabras_frase = frase_usuario.lower().split() #con .lower() convertimos todas las palabras a minuscula y con .split() descartamos los espacios en blanco 

palabras_individual = set(palabras_frase) #con set creamos el conjunto de palabras individualizadas en la frase (como vimos en la teoria un set no permite repeticiones)

palabras_repeticiones = {} #en este diccionario vacio introduciremos las palabras (keys) generados en el conjunto(set) anterior y luego sus repeticiones (values)

#el bucle for nos permite separar cada palabra dentro de la frase (ya en minuscula y descartando los espacios) 
for repeticion in palabras_frase: #busca una palabra en cada iteracion dentro de la frase
    if repeticion in palabras_repeticiones: # si esa palabra (key) está ya esta en el diccionario
        palabras_repeticiones[repeticion] += 1 #suma 1 al valor(value) de esa palabra
    else:                                    #si esa palabra (key) no está en el diccionario
        palabras_repeticiones[repeticion] = 1 #la agrega con el valor (value) 1

print(f'Palabras en la frase sin repetir:\n  {palabras_individual}') #Muestra en conjunto de las palabras sin repetir en la frase

print(f'Palabras y las veces que se repiten en la frase:\n  {palabras_repeticiones}') #Muestra el diccionario con las palabras y las veces que se repiten




#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

alumnos_promedios= {} #diccionario donde se acumularan los nombres de los alumnos(keys) y sus 3 notas (values) en torma de tuplas

for i in range(3): #bucle for con tres iteraciones, cada una para cargar los alumnos y sus notas
    nombre_alumno= input(f'Ingresá el nombre del alumno {i+1}: ') #toma el nombre del alumno
    print(f'  A continuación ingresá las notas de {nombre_alumno} ')
    #tomamos las notas individualmente para luego poder convertirlas en una tupla
    nota1 = float(input("    Nota 1: ")) #toma el valor de la 1er nota como una numero flotante
    nota2 = float(input("    Nota 2: ")) #toma el valor de la 2da nota como una numero flotante
    nota3 = float(input("    Nota 3: "))  #toma el valor de la 3er nota como una numero flotante
    print() #simula un espacio en blanco para mayor orden
    notas_tupla = (nota1, nota2, nota3) #convierte las tres notas en una tupla
    alumnos_promedios[nombre_alumno]= notas_tupla #agrega al diccionario el nombre ingresado como key la tupla como value 

print('Los Promedios de los alumnos son:') #encabezado para los promedio

#el bucle for nos permite ordenar en forma de columna la informacion para una ejecucion mas limpia
for nombre, notas, in alumnos_promedios.items(): #extrae el nombre (key) y notas(value en forma de tupla) en cada iteracion hasta leerlos a todos.
    promedio= sum(notas) / len(notas) #toma las notas (value), las suma y luego la divide por la cantidad para obtener el promedio 
    print(f" El promedio de {nombre} es {promedio:.2f}") #imprime el nombre del alumnos y su promedio con solo dos decimales por si el calculo del promedio da un número con muchos decimales 




#  7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#   • Mostrá los que aprobaron ambos parciales.
#   • Mostrá los que aprobaron solo uno de los dos.
#   • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

aprobados_parcial1 = {'Juan','Pedro','Luis','Carlos','José','Daniel','Miguel','Nicolas','Martin','Elias'} #conjunto1
aprobados_parcial2 = {'Elias','Nicolas','Daniel','Carlos','Pedro','Mauricio','Alberto','Joaquin',} #conjunto2

print('Alumnos que aprobaron ambos parciales:') #encabezado lista aprobados ambos

aprobados_ambos = aprobados_parcial1 & aprobados_parcial2 #utilizamos "interseccion" para generar un nuevo conjunto con los nombres que aparecen en ambos conjuntos 
for nombre in aprobados_ambos: #usamos un ciclo for para imprimir cada nombre en forma vertical para una lectura mas limpia
    print(f' -{nombre}')
        
print('\nAlumnos que aprobaron solo uno de los dos:') #encabezado lista aprobados solo uno de ambos
print("Solo primer parcial:") #encabezado del listado de quienes solo aprobaron el 1er parcial
aprobados_solo_1ro = aprobados_parcial1 - aprobados_parcial2 #utilizamos "diferencia" para generar un nuevo conjunto con quienes solo figuran en el primer conjunto
for nombre in aprobados_solo_1ro: #usamos un ciclo for para imprimir cada nombre en forma vertical para una lectura mas limpia
    print(f' -{nombre}')
    

print("Solo segundo parcial:") #encabezado del listado de quienes solo aprobaron el 1er parcial
aprobados_solo_2do = aprobados_parcial2 - aprobados_parcial1 #utilizamos "diferencia" para generar un nuevo conjunto con quienes solo figuran en el segundo conjunto
for nombre in aprobados_solo_2do: #usamos un ciclo for para imprimir cada nombre en forma vertical para una lectura mas limpia
    print(f' -{nombre}')
    

print('\nAlumnos que aprobaron al menos un parcial:') #encabezado lista aprobados al menos un parcial
aprobados_al_menos_uno = aprobados_parcial1.union(aprobados_parcial2) #utilizamos "union" para generar un nuevo conjunto con los nombres de ambos conjuntos sin que se repitan. 
for nombre in aprobados_al_menos_uno: #usamos un ciclo for para imprimir cada nombre en forma vertical para una lectura mas limpia
    print(f' -{nombre}')




#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
#   • Consultar el stock de un producto ingresado.
#   • Agregar unidades al stock si el producto ya existe.
#   • Agregar un nuevo producto si no existe.

productos_stock = {'Leche': 30 , 'Queso': 20 , 'Ricota': 15, 'Crema': 25 , 'Manteca': 10, 'Mermelada': 40, 'Yerba': 50} #diccionario con productos en stock

print('Bienvenido al sistema de stock de la tienda!\nPor favor seleccione que operacion desea realizar:') #encabezado 
menu_opciones = ['1. Consultar el stock de un producto', '2. Agregar unidades a un producto existente', '3. Agregar un nuevo producto al stock'] #lista menú de opciones
for opcion in menu_opciones: #este bucle for imprime el menu de opciones en forma vertical
    print(opcion)

opcion_usuario = int(input(" Su selección:")) #recibe la opcion seleccionada por el usuario

if opcion_usuario == 1: #si selecciona 1
    #consultar el stock de un producto en la lista
    producto= input('Ingrese el producto para consultar su stock: ') #recibe el nombre del producto ingresado por el usuario

    if producto in productos_stock: #condicional que verifica si el producto existe en el diccionario
        print(f'El producto {producto} tiene {productos_stock[producto]} undades en existencia') #si existe
    else:
        print('El producto ingresado no existe en el stock') #si no existe
elif opcion_usuario == 2: #si selecciona 2
    #agregar unidades a un producto en stock
    producto_ingresar_unidades = input('Ingrese el producto para agregar unidades: ') #recibe el nombre del producto ingresado por el usuario
    if producto_ingresar_unidades in productos_stock: #condicional que verifica si el producto existe en el diccionario
        unidades = int(input(f'Ingrese las unidades de {producto_ingresar_unidades} para su stock:')) #si existe solicita al usuario la cantidad de unidades
        productos_stock[producto_ingresar_unidades] += unidades #suma las unidades ingresadas a las ya existentes
        print(f'Unidades ingresadas correctamente, {producto_ingresar_unidades} ahora posee {productos_stock[producto_ingresar_unidades]} unidades en existencia') #mensaje de confirmacion
        print(productos_stock) #imprime la lista para mostrar que efectivamente se actualizaron las unidades del producto
    else:
        print('El producto ingresado no existe en el stock') #si el producto no existe en el stock
elif opcion_usuario == 3: #si selecciona 3
    #agregar producto que no existente en el stock
    ingresar_producto = input('Ingrese un producto para ingresar a la lista: ') #recibe el nombre del producto ingresado por el usuario
    if ingresar_producto not in productos_stock: #condicional que verifica si el producto no existe en el diccionario
        unidades_producto = int(input(f'Ingrese la cantidad de unidades de {ingresar_producto}: ')) #si no existe solicita la cantidad de unidades del producto
        productos_stock[ingresar_producto]= unidades_producto #agrega al diccionario el nuevo producto y sus unidades
        print(f'Producto ingresado correctamente, {ingresar_producto} ahora existe y posee {productos_stock[ingresar_producto]} unidades en existencia') #mensaje de confirmacion
        print(productos_stock) #imprime la lista para mostrar que efectivamente se ingresó en nuevo producto
    else:
        print('El producto ingresado ya existe en el stock') #si el producto ya existe en el stock

   # Aclaración: a modo de hacer mas entretenido este ejercicio se utilizó, a modo de ejemplo, frases de un personaje de película infantil llamado "el grinch"
   #             Bajo ninguna circunstancia es mi intención ofender o faltar el respeto ni tomar a la lijera los solicitado. Simplemente darle
   #             un giro divertido y humoristico pero también útil y funcional al desarrollo del ejercicio.


#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#   Permití consultar qué actividad hay en cierto día y hora.

#diccionario con agenda
agenda_grinch = {('Lunes', '4:00'): 'Sumerjirme en mi propia miseria', ('Martes', '4:30'): 'Contemplar el avismo', ('Miercoles', '5:00'): 'Solucionar la hambruna mundial sin decirselo a nadie', ('Jueves','5:30'): 'Danza y Ejercicio',('Viernes','6:00'): 'Cena Conmigo, esa no la cambiaré',('Sabado', '6:30'): 'Luchar con el odio que me tengo'}

print("Bienvenido a la agenda del Grinch!") #Encabezado mensaje de bienvenida

repetir_bucle = True # variable booleana que permite mantener activo o terminar el bucle

while repetir_bucle: #Bucle while que permite volver a realizar la accion 
    dia_buscar = input('Ingresá el día que querés consultar: ') #recibe el valor del dia ingresado por el usuario
    hora_buscar = input('Ingresá la hora: ') #recibe el valor de la hora ingresado por el usuario

    clave_buscar = (dia_buscar, hora_buscar) #transforma los valores ingresados en tupla para poder realizar la busqueda en el diccionario

    if clave_buscar in agenda_grinch: #condicional que comprueba si la informacion ingresada existe en el diccionario
        print(f'{dia_buscar} a las {hora_buscar}: {agenda_grinch[clave_buscar]}') #si existe...
    else:
        print('Rayos! No hay eventos en ese día y horario') #si no existe...

    repetir= input("\n¿Querés hacer otra búsqueda en la agenda del grinch?\n'S' para repetir, 'N' para finalizar: ") #consulta al usuario si quiere repetir la accion
    if repetir == 'N' or repetir == 'n': #condicional de verifica si repite o no el bucle
        repetir_bucle = False #cambio del estado de la variable booleana
        print('Recordá: Si no querés tener barriga mejor pintate el ombligo en la espalda. Hasta luego!\n     Atte. El grinch') #mensaje de despedida




#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
#    • Las capitales sean las claves.
#    • Los países sean los valores.

#diccionario con paises (key) y sus capitales (value)
original= {'Argentina': 'Buenos Aires', 'Chile': 'Santiago', 'Uruguay': 'Montevideo', 'Paraguay': 'Asunción', 'Brasil': 'Brasilia'}

invertido= {} #nuevo diccionario donde se mostrarán los datos invertidos

#bucle for que permite hacer la inversión en cada key-value
for pais, capital in original.items(): #extrae key-value explorando cada pareja con la funcion items() en cada iteración
    invertido[capital] = pais #carga en el nuevo diccionario los datos extraidos de forma invertida (el value como key y el key como value)

print("Diccionario original:") #encabezado del diccionario original
print(original) #imprime en pantalla el diccionario original

print("\nDiccionario invertido:") #encabezado del diccionario invertido
print(invertido) #imprime en pantalla el diccionario con las parejas invertidas