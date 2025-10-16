# TECNICATURA UNIVERSITARIA EN PROGRAMACION A DISTANCIA
# UNIVERSIDAD TECNOLOGICA NACIONAL

# ALUMNO: Daniel Nicolas Dominguez Coria, DNI: 35085946
# MATERIA: Programación 1
# Trabajo Practico Unidad 8, Manejo de Archivos



#1. Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos.
#   Cada línea debe tener: nombre,precio,cantidad

#mansaje de presentacion:
print("\n¡BIENVENIDO AL GESTOR DE PRODUCTOS CON MANEJO DE ARCHIVOS DEL T.P.8!\n  A continuacion iremos mostrando paso a paso cada ejercicio.")

print("\n1. Creación de archivo 'productos.txt'") #encabezado ejercicio 1 
with open("productos.txt", "w") as archivo: #genera el archivo donde se guardará la informacion, si ya existe los sobre escribe
    archivo.write("Remera, 2000, 10\n")       # registra el producto 1 en el archivo
    archivo.write("Pantalon, 3000, 20\n")     # resgistra el producto 2 en el archivo
    archivo.write("Buzo, 3500, 15\n")         # registra el producto 3 en el archivo
    print("  'productos.txt' creado exitosamente!.")   #mensaje de confirmacion




#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea,
#   la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
#   Ej: Producto: Lapicera | Precio: $120.5 | Cantidad: 30

print("\n2. Lectura del archivo productos.txt:")  #encabezado ejercicio 2
with open("productos.txt", "r") as archivo:  #abre y lee el archivo donde se registraron los tres primeros productos.
    for linea in archivo:                    #bucle que extrae linea por linea cada registro
        linea= linea.strip()                 #strip elimina los espacios vacios al principio y final de cada linea
        producto, precio, cantidad = linea.split(",")  #strip desempaqueta cada item teniendo en cuenta las "," en la frase y lo organiza en su variable correspondiente
    
        print(f"  Producto: {producto} | Precio: ${precio} | Cantidad: {cantidad}" ) # toma los items desempaquetados y los imprime ordenados para formar la lista de productos 




#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos,
#   le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad) y lo agregue al archivo
#   sin borrar el contenido existente.

print("\n3. Ingreso de nuevo producto a productos.txt:")  #encabezado ejercicio 3
nuevo_producto = input("  Ingrese un nuevo producto: ")                 #recibe el nombre del nuevo producto
nuevo_precio = input(f"  Ingrese el precio de {nuevo_producto}: ")      #recibe el predio del nuevo producto
nuevo_cantidad = input(f"  Ingrese la cantidad de {nuevo_producto}: ")  # recibe la cantidad de unidades del nuevo producto

with open("productos.txt", "a") as archivo: #escribe al final del archivo pero sin sobreescribirlo
    archivo.write(f"{nuevo_producto}, {nuevo_precio}, {nuevo_cantidad}\n") #la informacion que se registra ordenada




#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en una lista llamada productos,
#   donde cada elemento sea un diccionario con claves: nombre, precio, cantidad.

print("\n4. Carga de los productos en una lista de diccionarios:")  #encabezado ejercicio 4
productos = [] #lista donde se acumularan los diccionarios de productos

with open("productos.txt", "r") as archivo: #abre y lee el archivo donde se registraron los tres primeros productos.
    for linea in archivo:                                  #bucle que extrae linea por linea cada registro
        linea = linea.strip()                              #strip elimina los espacios vacios al principio y final de cada linea
        nombre, precio, cantidad = linea.split(",")        #strip desempaqueta cada item teniendo en cuenta las "," en la frase y lo organiza en su variable correspondiente
    
        producto = {              #crea el diccionario con los datos extraidos  en cada iteración como valores de cada clave correspondiente
            "nombre": nombre,         #crea la clave nombre y le asigna el valor del mismmo nombre extraido del archivo.
            "precio": precio,         #crea la clave precio y le asigna el valor del mismmo nombre extraido del archivo.    
            "cantidad": cantidad      #crea la clave cantidad y le asigna el valor del mismmo nombre extraido del archivo.
        }

        productos.append(producto) #agrega cada diccionario al final de la lista 

for prod in productos: #bucle que extrae en cada iteracion un indice de la lista y lo imprime por pantalla
    print(f"  Producto: {prod['nombre']} | Precio: ${prod['precio']} | Cantidad: {prod['cantidad']}") #orden que toma cada linea de la lista vertical al imprimirse
    #Aclaracion: se usó el nombre "prod" ya que "producto" fue asignada anteriormente, si bien la variable "producto" solo existe dentro del with esto
    # evita posibles errores o confuciones, sobre todo en el ejercicio 5 donde usamos otro for para busqueda de producto en la lista. La variable "prod" del bucle acumula, en cada iteracion, uno de los diccionarios añadidos anteriormente a la lista.
    # luego con print mostramos el valor dentro de cada una de sus claves. (nombre precio, cantidad).
    # Vale aclarar que el nombre "producto" se dejará reservada para uso exclusivo dentro de los bloques with, esto facilita el entendimiento y orden del código. 




#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto.
#   Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si no existe, mostrar un mensaje de error.

print("\n5. Busqueda de producto en la lista:") #encabezado ejercicio 5
busqueda_producto = input(" Ingresa el nombre del producto a buscar: ") #recibe el nombre del producto ingresado por el usuario para realizar la busqueda

en_lista = False #Esta variable booleana sirve como bandera en caso de coincidencia para la busqueda del producto ingresado

for p in productos: #bucle for que busca en la lista, la coincidencia con el valor ingresado 
    if p["nombre"].lower().strip() == busqueda_producto.lower().strip() : #la condicional toma el un diccionario en cada iteracion, busca la clave "nombre" y compara su valor con el ingresado 
        print(f" Producto encontrado:")    #si hay coincidencia se imprime por pantalla el producto con cada uno de sus items
        print(f"  - Nombre: {p['nombre']}\n  - Precio: ${p['precio']}\n  - Cantidad: {p['cantidad']}")
        en_lista = True                #Vuelve verdadero la variable booleana (bandera) para que la proxima condicional no se ejecute
        break                          #Corta automáticamente el bucle for ya que la coincidencia fue exitosa.
        #Aclaracion: Nuevamente se debió asignar un nombre a la variable del bucle for que extrae de la lista un diccionario en cada iteracion, al estar ocupara "producto" y "prod" se decicdió asignarle como nombre "p"
        #            en la condicional se agregó como extra las funciones .lower() y .strip() que convierte los valores a comparar en minuscula y quieta los espacios al principio y final. Esto mejora la posibilidad de coincidencia.

if not en_lista: #si en la condicional anterior no hubo coincidencia de valores comparados la bandera (booleano) sigue siendo False y se ejecuta esta.
    print(f"\n El producto '{busqueda_producto}' no existe en la lista.") #imprime por pantalla que no hubo coincidencia.




#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado productos,
#   sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista.

print("\n6. Actualizar los productos en productos.txt:") #encabezado ejercicio 6
with open("productos.txt", "w") as archivo: # llama y reescribe el archivo con los valores obtenido de la lista "productos" en cada iteracion
    for producto in productos: #bucle for que extrae cada diccionario de la lista en cada iteracion
        linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n" # extrae el contenido del diccionario y lo ordena para que se guarde en el archivo
        archivo.write(linea)   #escribe la informacion dentro del archivo linea por linea

print("  Archivo 'productos.txt' actualizado correctamente:") #avisa que la actualizacion se realizó correctamente

with open("productos.txt", "r") as archivo: #hacemos un ultimo llamado al archivo para leer e imprimir su contenido actualizado
    contenido = archivo.read()
    print(contenido)
