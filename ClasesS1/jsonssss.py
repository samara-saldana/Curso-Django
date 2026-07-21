import json

with open('users.json', 'r') as archivo:
    usuarios = json.load(archivo)

print(type(usuarios))
nuevo = []

for usuario in usuarios:
    nombre = usuario["name"]
    latitud = usuario['address']['geo']['lat']
    longitud = usuario['address']['geo']['lng']
    ciudad = usuario['address']['city']
    telefono = usuario['phone']
    pagina_web = usuario['website']

    nuevo.append({"nombre": nombre, "latitud":latitud, "longitud":longitud, "ciudad":ciudad, "telefono":telefono, "pagina_web":pagina_web})

print(nuevo)


with open('datos.json', 'w',encoding ='utf-8') as archivon:
    json.dump(nuevo,archivon,indent=4, ensure_ascii=False)