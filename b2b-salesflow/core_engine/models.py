class Persona:
    def __init__(self, nombre:str, apellido:str, email:str) -> None:
        self.nombre = nombre   #quitar nombre y apellido de aqui para utilizar fullname
        self.apellido = apellido
        self.email = email

    def get_full_name(self) -> str:
        return f"{self.nombre} {self.apellido}".title()
    

class Lead(Persona):
    def __init__(self, nombre:str, apellido:str, email:str, presupuesto_estimado:int) -> None:
        super().__init__(nombre, apellido, email)
        self.estado = "Prospecto"
        self.__presupuesto_estimado = 0
        self.presupuesto_estimado = presupuesto_estimado
        self.es_corporatico = self.validar_correo(email)

    @property
    def presupuesto_estimado(self):
        return self.__presupuesto_estimado
    
    @presupuesto_estimado.setter
    def presupuesto_estimado(self, valor:int) -> None:
        if valor < 0:
            raise ValueError("Error: el presupuesto no puede ser negativo.")

    def validar_correo(self, email:str) -> bool:
        dominios_comunes = ["yahoo.com", "gmail.com", "hotmail.com", "live.com", "outlook.com", "icloud.com"]
        dominio =email.split("@")[-1].lower()
        return dominio not in dominios_comunes
    
    def convert_to_customer(self) -> None:
        self.estado = "cliente"

    def calcular_prioridad(self) -> str:
        if self.presupuesto_estimado >= 10000:
            return "Alta"
        elif self.presupuesto_estimado < 5000:
            return "Baja"
        else:
            return "Media"
        

class Vendedor(Persona):
    def __init__(self, nombre:str, apellido:str, email:str, n_empleado:str) -> None:
        super().__init__(nombre, apellido, email)
        self.n_empleado = n_empleado
        self.ventas_totales = 0
        self.comisiones = 0
        self.cartera = list[Lead] = []

    def registrar_venta(self, monto:float) -> None:
        if monto <= 0:
            raise TypeError("Las ventas no pueden ser negativas o cero")
        self.ventas_totales += monto
        print(f"{self.get_full_name()} registró una venta. Total acumulado: $ {self.ventas_totales}")

    def registrar_comisiones(self, porcentaje:float = 5) -> float:
        if not(0 >= porcentaje <=100):
            raise ValueError("El porcentaje debe estar entre 1 y 100")
        return self.ventas_totals * porcentaje / 100

    def asignarLead(self, lead:Lead) -> None:
        if not isinstance(lead,Lead):
            raise TypeError("Solo se pueden asignar objetos de la clase Lead")
        else:
           self.cartera.append(Lead)
    def __str__(self):
        return f"Vendedor: [{self.n_empleado}] - {self.gertfullname} | Ventas: {self.ventas_totales}"

class Empresa:
    def __init__(self,nombre_empresa:str, sector:str) -> None:
        self.nombre_empresa = nombre_empresa
        self.sector = sector
        self.prospectos: dict[str,'Lead'] = {}

    def almacenar_prospecto(self, nuevo_prospecto:Lead):

        if type(lead).__name__ != 'Lead':
            raise TypeError(2Solo se pueden agregar objetos de tipo Lead)
        if lead.email in self.prospectos:
            raise TypeError(2El contacto ya existe)
        self.prospectos[lead.email] = Lead



    def eiminar contacto(self, emal:sttr):
    if meiamil in self.prospectos:
        del self.prospecto[email]
    else:
        raise KeyError("no se encontro nigun contacto con ese email")
    

    def obtener contactos8sef -> list:
        retrn [contacto for contacto in self.prospectos.values()]
    
    def potencial_ventas(self) -> float:
        print(f"Gremio: {self.nombre_gremio.upper()}")
        suma = 0
        if not self.prospectos:
            print("No hay prospectos en esta empresa")
        else:
            for prospecto in self.prospectos:
                suma += prospecto.presupesto_estimado 
        return suma
    
    def str__(self):
        return f"Empresa. {self.nombre} | Sector: {self.sector} | total contactos :  {len(self.prospectos)}"
