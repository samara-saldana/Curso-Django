#L funcion lambdda no se uede debuggear al ser una funcion anonima

calcular_comision = lambda venta: venta *0.5

# print(f"Comisión por venta de $1000: ${calcular_comision(1000)}")

leads = [
    {"nombre" : "Empresa A", "presupuesto":2000, "estado": "Nuevo"},
    {"nombre" : "Empresa B", "presupuesto":3000, "estado": "Contactado"},
    {"nombre" : "Empresa C", "presupuesto":1500, "estado": "Nuevo"},
    {"nombre" : "Empresa D", "presupuesto":2000, "estado": "Cerrado"}
]
leads_ordenados = sorted(leads, key= lambda lead: lead['presupuesto'], reverse=True)

# [print(c) for c in leads_ordenados]

presupuesto = lambda lead : lead['presupuesto']*2
# [print(f"Presupuesto duplicad para {lead['nombre']}: ${presupuesto(lead)}") for lead in leads_ordenados]




maximo =lambda x,y: x if x>y else y
# print(f"Maximo entre 10 y 20: {maximo(10,20)}")

reverso = lambda s: s[::-1]
# print(f"Reverso de 'Python': {reverso('Python')}")


#args -> Argumento variable sposicinales, trabaja con valores solamente

suma = lambda *args : sum(args)

# print(f"Suma de 1,2,3,4,5: {suma(1,2,3,4,5)}")


#kwargs -> Argumentos variables por clave, trabaja con clave y valor

mostrar_info = lambda **kwargs: print (f"información recibida: {kwargs}")
# mostrar_info (nombre="juan", edad=30, ciudad= "Madrid")
# mostrar_info (producto="juan", precio=1200, stock= 50)
# mostrar_info (usurio="admin", permisos= ["lectura", "escrtura", "ejecucion"])

evaluar = lambda x: "Positivo" if x >0 else ("Negativo" if x<0 else "Cero")
# print(f"Evaluar 10: {evaluar(10)}")
# print(f"Evaluar -5: {evaluar(-5)}")
# print(f"Evaluar 0: {evaluar(0)}")


leads_nuevos = filter(lambda lead: lead['estado'] == 'Nuevo', leads)
print(f"Leads nuevos: {leads_nuevos}") #filter es un tipo de dato no legible para python
# print(f"Leads nuevos: {list(leads_nuevos)}")
# print(f"Leads nuevos: {tuple(leads_nuevos)}")
#por que despues de que transformo en uno la siguiente me sale vacia?
print(f"Tipo de dato de leads nuevos: {type(leads_nuevos)}")
[print(f"- Lead: {lead['nombre']}, Presupuesto: ${lead['presupuesto']}") for lead in leads_nuevos]  #y por que ya no funciona la lista de copresion sidejo esa tranformacion?



nombres_mayusculas = list(map(lambda lead: lead['nombre'].upper(),leads))
print(f"nombres de leads en mayúsculas:{nombres_mayusculas}")

inventario_crudo = [
    {"sku":"A1", "producto":"LAPTOP gamer","precio_str":"$1200.50", "moneda":"USD"},
    {"sku":"B2", "producto":"ratón Inalambrico","precio_str":"€45.00", "moneda":"EUR"},
    {"sku":"C3", "producto":"TECLADO MECANICO","precio_str":"$85.99", "moneda":"USD"}
]

TASA_EURO_A_USD = 1.08

def normalizar_producto(item:dict) -> dict:
    """Limpia el texto, convierte monedas y formata a un estandar"""
    precio_limpio = float(item['precio_str'].replace("$","").replace("€",""))

    if item['moneda'] == 'EUR':
        precio_limpio = round(precio_limpio*TASA_EURO_A_USD,2)
    
    return {
        "sku":item["sku"], 
        "producto":item["producto"].title(),
        "precio_usd":precio_limpio
    }

inventario_limpio = list(map(normalizar_producto,inventario_crudo))


for prod in inventario_limpio:
    print(f" -{prod['sku']} | {prod['producto']} -> $ {prod['precio_usd']} USD")

logs_servidor = [
    {"ip": "192.168.1.10", "endpoint": "/home", "status": 200, "user_agent": "Chrome"},
    {"ip": "45.33.22.11", "endpoint": "/wp-admin.php", "status": 403, "user_agent": "Python-urllib"},
    {"ip": "10.0.0.5", "endpoint": "/api/v1/users", "status": 200, "user_agent": "Safari"},
    {"ip": "88.15.44.3", "endpoint": "/.env", "status": 404, "user_agent": "Curl/7.68.0"},
    {"ip": "192.168.1.12", "endpoint": "/dashboard", "status": 200, "user_agent": "Firefox"}
]

def es_amenaza(log: dict) -> bool:
    """
    devuelve true si la particion parece maliciosa.
    evalua errores de permisos (403), archivos sensibles o bots automátos
    """
    endpoints_peligrosos = [".env","wp-admin","config.php"]

    
    if any(peligro in log['endpoin'] for peligro in endpoints_peligrosos):
        return True
    if log["status"] == 403 and log['user_agent'] not in ["Crhome", "Firefox", "safari"]:
        return True
    return False
    
ataques_detectados = list(filter(es_amenaza,logs_servidor))

for ataque in ataques_detectados:
    print(f"Bloqes la ip:{ataque['ip']} -> intento aceer a '{ataque['endpoint']}")