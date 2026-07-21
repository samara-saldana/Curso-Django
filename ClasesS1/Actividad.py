import json

print("--- ⚙️ Iniciando Pipeline de Transformación de Datos ---")

# DATOS CRUDOS: Una tupla inmutable que contiene otras tuplas.
# Formato: (ID_Cliente, Nombre_Empresa, Venta_Cerrada, Monto_USD)
datos_backend = (
    ("C001", "TechCorp", True, 15000),
    ("C002", "GamerStore", False, 0),
    ("C003", "EduGlobal", True, 8500),
    ("C004", "BioHealth", True, 22000),
    ("C005", "AutoFix", False, 0)
)

# ==========================================
# 🛑 ZONA DE RETO: TU CÓDIGO EMPIEZA AQUÍ
# ==========================================

# 1. Usa filter() y una lambda para obtener solo las tuplas donde Venta_Cerrada sea True.
ventas_exitosas = list(filter(lambda tupla: tupla[2] == True, datos_backend))


# 2. Usa map() y una lambda para transformar 'ventas_exitosas' en una lista de diccionarios.
# Cada diccionario debe verse así: {"empresa": Nombre_Empresa, "comision": Monto_USD * 0.10}
lista_comisiones = list(map(lambda venta: {"empresa": venta[1], "comision": venta[3] * 0.10},ventas_exitosas))

# 3. Construye el Diccionario Maestro.
# Debe tener dos claves principales: 
# - "metadata": Un diccionario con la clave "total_ventas_exitosas" (usa len() sobre tu lista).
# - "desglose": La lista de diccionarios que creaste en el paso 2.
diccionario_dashboard = {
    "metadata": {
        "total_ventas_exitosas": len(ventas_exitosas)
        },
    "desglose" : lista_comisiones
}
# 4. Convierte el 'diccionario_dashboard' a un JSON string con indentación de 4.
json_final = json.dumps(diccionario_dashboard,indent=4)

# ==========================================
# ✅ ZONA DE PRUEBA: NO MODIFICAR
# ==========================================
print("\n📦 JSON LISTO PARA EL FRONTEND:")
print(json_final)




