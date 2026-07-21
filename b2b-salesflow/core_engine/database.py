import sqlite3
from core_engine.models import Lead


def inicializar_db():

    conexion = sqlite3.connect("emprYpros.db")
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prospectos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            correo TEXT UNIQUE NOT NULL,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            presupuesto_estimado INTEGER DEFAULT 0,
            estado TEXT NOT NULL,
            clasificacion TEXT NOT NULL,
            prioridad TEXT NOT NULL,

            empresa_id INTERGER,
            FOREIGN KEY (empresa_id) REFERENCES empresas (id)  
        )
    ''')

    conexion.commit()
    conexion.close()

def guardar_lead(lead:Lead):
    conexion = sqlite3.connect("emprYpros.db")
    cursor = conexion.cursor()

    try:   #se onene los signos de interrogacion por seguridad
        cursor.execute('''
                    INSERT INTO prospectos (correo, nombre, apellido, presupuesto_estimado, estado, clasificacion, prioridad)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (lead.email, lead.nombre, lead.apellido, lead.presupuesto_estimado, lead.estado, lead.clasificacion, lead.calcular_prioridad()))
        conexion.commit()
        print("Exito al registrar el lead")
    except sqlite3.IntegrityError:
        print(f"Aviso, el lead con email {lead.email} ya existe en la DB")
        conexion.rollback()
    finally:
        conexion.close()