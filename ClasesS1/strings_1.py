texto_sucio = "          Hola, a todos         "

'''
print(f"Texto original: {texto_sucio}")
print(f"Uso de lstrip(): {texto_sucio.lstrip()}") #corta espacios de la izquierda
print(f"Uso de rstrip(): {texto_sucio.rstrip()}") #corta los esacio de la derecha
print(f"Uso de strip(): {texto_sucio.strip()}")  #corta los esacios de la derecha y la izquierda
'''


saludo = "Hola gatos, adios gatos"
'''
print(f"texto original: {saludo}")
print(f"Uso de replace(): {saludo.replace('gatos', 'perros')}")   #reemplaza todas las coincidencias
print(f"Uso de replace() con count:{saludo.replace('gatos', 'perros',1)}")   #reemplaza la primera coincidencia que encuentre
'''

csv = "manzana,pera, platano, uva"

lista_frutas = csv.split(",")
#print(f"Lista de frutas:{lista_frutas}")

conector ="-"
texto_unido = conector.join(lista_frutas)
#print(f"Texto unido: {texto_unido}")

texto_lineas = "Linea 1\nLinea 2\nLinea 3"
#print(f"Texto original: \n{texto_lineas}")
#print(f"Uso de splitlines(): {texto_lineas.splitlines()}")


frase = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme ..."
# print(f"Texto original {frase}")
# print(f"Uso de find(): {frase.find('lugar')}")
# print(f"Uso de count(): {frase.count('de')}")
# print(f"Uso de index() {frase.index('Mancha')}")
# print(f"Uso de startwith() {frase.startswith('En un lugar')}")
# print(f"Uso de endswith() {frase.endswith('acordarme ...')}")

# print("'12345'.isdigit(): ", '12345'.isdigit())
# print("'Hola'.isdigit(): ", 'Hola'.isalpha())
# print("'Hola12345'.isalnum(): ", 'Hola12345'.isalnum())
# print("'Hola mundo'.isspace(): " ,'Hola mundo'.isspace())
# print("'Hola mundo'.istitle(): ", 'Hola mundo'.istitle())
# print("'Hola mundo'.isupper(): ", 'Hola mundo'.isupper())
# print("'Hola mundo'.islower(): " ,'Hola mundo'.islower())


#atributo docs
#Me sirve para documentar mi función

def procesar_datos(tabla:dict) -> list:
    """
    Esta función recibe na tabla de datos crudos y estandariza los formatos

    Parámetros:
    tabla (list): Lista de diccionarios con los datos crudos

    Retorna.
    list: Lisra de diccionarios con los datos estandar
    """
    pass

# print(f"documentacion de la función prcesar datos(): {procesar_datos.__doc__}")

STATUS = "activo"
query_sql = f"""
SELECT id_usuario,nombre,fecha_registro
FROM usuarios
WHERE estado = '{STATUS}'
ORDER BY fecha_egstro DESC;
"""


#Aqui python si lo reconoce, pero otro framework no siempre, entonces hay que utilizar doble comilla en bloques de comentarios
# query_sql = f'''
# SELECT id_usuario,nombre,fecha_registro
# FROM usuarios
# WHERE estado = '{STATUS}'
# ORDER BY fecha_egstro DESC;
# '''

# print(f"Consulta SQL: \n{query_sql}")

#raw strings #Dos formas de escribir rutas de archivo porque python tiene conflicto con las \
ruta_archivo = "C:\\Users\\Carpeta\\archivo.csv"
ruta_archivo_raw = r"C:\Users\Carpeta\archivo.csv"
# print(f"Ruta del archivo:{ruta_archivo}")

id_usuario = "45"
id_producto = "1642"
# print(f"ID original{id_usuario} -> ID formateado: {id_usuario.zfill(7)}")
# print(f"ID original{id_producto} -> ID formateado: {id_producto.zfill(7)}")

for i in range (1,11):
    # print(f"ID original{i} -> ID formateado: {str(i).zfill(3)}")
    pass


correo = "usuario@dominio.com"
usuario,arroba, dominio = correo.partition("@")
# print(f"Correo original : {correo}")
# print(f"udsuario : {usuario}")
# print(f"arroba : {arroba}")
# print(f"dominio : {dominio}")

correo = "usuario.dominio.com"
usuario,arroba, dominio = correo.partition("@")
# print(f"Correo original : {correo}")
# print(f"udsuario : {usuario}")
# print(f"arroba : {arroba}")
# print(f"dominio : {dominio}")



