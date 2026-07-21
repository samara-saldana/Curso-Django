from core_engine.database import inicializar_db, obtener_conexion
from core_engine.models import Vendedor, Lead, Empresa

#from core_engine.database import *
#import core-engine.database as database

def registro_empresa(nombre):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("INSERT INTO empresas (nombre_empresa) VALUES (?)", (nombre,))
        conexion.commit()
        print(f"La empresa {nombre} ha sido registrada correctamente")
    except Exception as e:
        print(f"Error al registrar empresa: {e}")
    finally:
        conexion.close()

def registro_prospecto(lead:Lead,empresa:str):
    conexion =obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre_empresa FROM empresas")
    empresas = cursor.fetchall()

    try:
        for emp in empresas:
            if emp[1] == empresa:
                try:
                    nuevo_pr =  Lead(lead.nombre, lead.apellido, lead.email,lead.presupuesto_estimado)
                    cursor.execute('''
                    INSERT INTO prospectos (correo, nombre, apellido, presupuesto_estimado, estado, clasificacion, prioridad, empresa_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (nuevo_pr.email, nuevo_pr.nombre, nuevo_pr.apellido, nuevo_pr.presupuesto_estimado, nuevo_pr.estado, nuevo_pr.clasificacion, nuevo_pr.prioridad, empresa[0]))
                except Exception as e:
                    print(f"Error al registrar empresa: {e}")
            else:
                print("Hace falta registrar empresa")
    except Exception as e:
        print(f"Error al registrar empresa: {e}")
    
    


if __name__ == "__main__":
    inicializar_db()

    emp = "Patito"
    registro_empresa(emp)

    lead_1 = Lead("Maria", "Perez", "maria@patito.com", 3000)
    lead_2 = Lead("Pedro", "Gomez", "pedro@patito.com", 6000)
    lead_3 = Lead("Juan", "Lopez", "juan@patito.com", 11000)

    registro_prospecto(lead_1, emp)
    registro_prospecto(lead_2, emp)
    registro_prospecto(lead_3, emp)





def main():
    inicializar_db()

    lead_1 = Lead("Maria", "Perez", "maria@patito.com", 3000)
    lead_2 = Lead("Pedro", "Gomez", "pedro@patito.com", 6000)
    lead_3 = Lead("Juan", "Lopez", "juan@patito.com", 11000)

    registro_prospecto(lead_1)
    registro_prospecto(lead_2)
    registro_prospecto(lead_3)

    #duplicado
    registro_prospecto(lead_1)

if __name__ == "__main__":
    main()