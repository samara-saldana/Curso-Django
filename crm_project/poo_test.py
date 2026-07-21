class Personaje:
    def __init__(self, nombre, salud_maxima):
        self.nombre = nombre
        self._salud = salud_maxima
        self.salud_maxima = salud_maxima
        self.inventario = ['Poción chica', 'Pan seco']

    @property
    def salud(self):
        return self._salud
    
    @salud.setter
    def salud(self,nueva_salud):
        if nueva_salud <= 0 :
            self._salud = 0
            print(f"{self.nombre} ha caido en la batalla :(")
        elif nueva_salud > self.salud_maxima :
            self._salud = self.salud_maxima
            print(f"No se le puede subir mas de {self.salud_maxima}")
        else:
            self._salud = nueva_salud
            print(f"Salud de {self.nombre} actualizada a: {self.salud}/{self.salud_maxima}")
    
    @salud.deleter
    def salud(self):
        print(f"Alerta!, no se puede borrar la salud de: {self.nombre}")

    def _efecto_sonido_curacion(self):
        print("Efecto de sonido: glug glug")

    def tomar_pocion(self, cantidad_curacion):
        print(f"{self.nombre} intenta tomar una pocion de + {cantidad_curacion} HP")
        self._efecto_sonido_curacion()
        self.salud = self.salud + cantidad_curacion

#metodos magicos
    def __str__(self):
        #se utiliza po ejemplo en: print(Personaje)
        return f"Personaje: {self.nombre} | HP: {self.salud}/{self.salud_maxima}"
    
    def __repr__(self):
        #se utilizan por ejemplo en repr(Personaje)
        return f"Personaje('{self.nombre}'.{self.salud_maxima})"
    
    def __gt__(self, otro_personaje):
        """Se activa al usar (>)"""
        return self.salud_maxima > otro_personaje.salud_maxima
    
    def __add__(self, otro_personaje):
        """Se activa al usar (+)"""
        print(f"fusion iniciada: {self.nombre} + {otro_personaje.nombre}")

        nuevo_nombre = f"{self.nombre[:3]}{otro_personaje.nombre[3:]}"
        nueva_salud = self.salud_maxima + otro_personaje.salud_maxima

        return Personaje(nuevo_nombre,nueva_salud)
    
    def __len__(self):
        """Se activa al usar len(objeto)"""
        return len(self.inventario)
    
    @staticmethod
    def mostrar_manual_juego():
        print("Manual del juego")
        print("Ahi va un menu")

    @classmethod
    def crear_npc_basico(cls):
        print("[Sistema] Generando NPC basico sin pedir datos")
        return cls(nombre ="aldeano genérico", salud_maxima = 10) #simpre se va a crear un aldeano con estos atributos sin tener que pasar argumentos

#Nuevo metodo mágico
    def __lt__(self, otro_personaje):
        """Se activa al usar <)"""
        return self.salud > otro_personaje.salud



class Guerrero(Personaje):
    def __init__(self, nombre, salud_maxima, puntos_armadura):
        super().__init__(nombre,salud_maxima)
        self.puntos_armadura = puntos_armadura

    def recibir_dano(self, dano_enemigo):
        print(f"un enemigo ataca a {self.nombre} con {dano_enemigo} de daño")

        dano_real = dano_enemigo - self.puntos_armadura
        if dano_real<0:
            dano_real=0

        print(f"La armadura bloquea {self.puntos_armadura} puntos. daño real: {dano_real}")

        self.salud =self.salud - dano_real

    def __str__(self):
        ficha_base = super().__str__()
        return f"{ficha_base} | Armadura: {self.puntos_armadura}"
    
    @classmethod
    def crear_espartano_elite(cls):
        print(f"[Sistema] Creando Espartano de elite") 
        return cls(nombre="Espartano", salud_maxima=200, puntos_armadura =50)
    
    #Nuevo metodo magico
    def __pow__(self, veces):
        print(f"La armadura adquirió protección especial")
        self.puntos_armadura +=veces
        return self
        
    


class Mago(Personaje):
    def __init__(self, nombre, salud_maxima, poder_magico):
        super().__init__(nombre,salud_maxima)
        self.poder_magico = poder_magico
        self.mana = 90

    #metodo de lanzar ehechizo

    def lanzar_hechizo(self, objetivo: Personaje, costo_mana =15) -> None:
        print(f"{self.nombre} prepara un hechizo contra {objetivo.nombre}")
        if self.mana >= costo_mana:
            self.mana -= costo_mana
            dano = 25
            print(f"{objetivo.nombre} recibe {dano} de dano magico")
            print(f"Mana restante de {self.nombre}: {self.mana}")
            objetivo.salud -= dano 
        else:
            print(f"Fallo: {self.nombre} no tiene suficiente mana")
            print(f"Requiere: {costo_mana}, actual: {self.mana}")

    def __str__(self):
        ficha_base = super().__str__()
        return f"{ficha_base} | Poder mágico: {self.poder_magico} | mana: {self.mana}"
    
    @classmethod
    def crear_mago_aprendiz(cls):
        print(f"[Sistema] Creando Mago Aprendiz") 
        return cls(nombre="Aprendiz", salud_maxima=70, poder_magico =25)
    
    #nuevo metodo magico
    def __mul__(self, veces):
        self.poder_magico *= veces
        print(f"el poder mágico de {self.nombre} ahra es: {self.poder_magico}")
        return self

    def __call__(self):
        print(f"[__call__] {self.nombre} entra en modo mediacion")
        self.mana += 20
        print(f"mana restaurado. Mana actual: {self.mana}")

class Clerigo(Personaje):
    def __init__(self, nombre, salud_maxima, poder_curacion):
        super().__init__(nombre,salud_maxima)
        self.poder_curacion = poder_curacion

    def __str__(self):
        ficha_base = super().__str__()
        return f"{ficha_base} | Poder de curación: {self.poder_curacion}"
    
    def rezar(self):
        print(f"{self.nombre} se arrodilla y eleva su plegaria a Alá")
    
    @classmethod
    def crear_clerigo_sanador(cls):
        print(f"[Sistema] Creando Clerigo Sanador") 
        return cls(nombre = "sanador", salud_maxima = 50, poder_curacion = 30)

#nuevo metodo mágico
    def __truediv__(self, objetivo):
        print(f"{self.nombre} cura a {objetivo.nombre}")
        objetivo.salud += self.poder_curacion
        return objetivo
    
    def __rshift__(self,aliado):
        """Este metodo se activa cuando clerigo>>guerrero"""
        curacion=25
        print(f"{self.nombre} canaliza luz divina hacia {aliado.nombre}")
        aliado.salud += curacion


class Asesino(Personaje):
    def __init__(self, nombre, salud_maxima):
        super().__init__(nombre, salud_maxima)
        self.__nivel_sigilo = 100
        
    @property
    def sigilo(self):
        return self.__nivel_sigilo
        
    @sigilo.setter
    def sigilo(self, nuevo_valor):
        if nuevo_valor>100:
            self.__nivel_sigilo =100
        elif nuevo_valor <=0:
            self.__nivel_sigilo =0
            print(f"alerta: {self.nombre} ha pisado una rama")

    def ocultarse(self):
        print(f"{self.nombre} lanza una bombade humo")
        self.sigilo = 0
        self.sigilo +=40

        print(f"Nivel de sigilo restaurado a: {self.sigilo}")

    def __str__(self):
        ficha_base = super().__str__()
        return f"{ficha_base} 1 Sigilo: {self.sigilo}"
    
    def __mul__(self, multiplicador_critico: int):
        """"Se activa al usar el simbolo de asterisco"""

        costo_sigilo = 35

        print(f"{self.nombre} Intenta un taque furtivo")

        if self.sigilo >= costo_sigilo:
            dano_base =15
            dano_total = dano_base * multiplicador_critico

            self.sigilo -= costo_sigilo
            print(f"Se hace un ataque critico, daño total: {dano_total}")

        else:
            print("No hay suficiente sigilo")
            self.sigilo=0
    

def encapsulamiento():
    print(f"******Encapsulamiento******")
    personaje1 = Personaje("Furiosa", 120)    

    personaje1.salud = 500
    print(f"La salud actual del personaje es: {personaje1.salud}") #se accede a la propiedad privada
    personaje1.salud=120
    print(f"La salud actual del personaje es: {personaje1.salud}") #se accede a la propiedad privada
    personaje1.salud=-300
    print(f"La salud actual del personaje es: {personaje1.salud}") #se accede a la propiedad privada
    
    del(personaje1.salud)

    personaje1.tomar_pocion(60)

    print(f"El personaje es tiene más salud que el npc?: {personaje1 < Personaje.crear_npc_basico()} ")


def herencia():
    print(f"******Herencia******")
    guerrero1 = Guerrero("Goku",500,100)
    print(guerrero1)

    mago1 = Mago("Gandalf",200,85)
    print(mago1)

    clerigo1 = Clerigo("Amadeus",150,65)
    print(clerigo1)

    guerrero1.recibir_dano(25)
    print(guerrero1)

    nuevo_personaje = clerigo1+ mago1
    print(nuevo_personaje)


def polimorfismo():
    print(f"******Polimorfismo******")
    guerrero1 = Guerrero("Goku",500,100)
    print(guerrero1)

    mago1 = Mago("Gandalf",200,85)
    print(mago1)

    clerigo1 = Clerigo("Amadeus",150,65)
    print(clerigo1)
    mago1()
    """ el metodo call se llama por ejemplo asi clerigo1()"""

def demo_decoradores(self):

    Personaje.mostrar_manual_juego()

    npc= Personaje.crear_npc_basico()
    guerrero_nop = Guerrero.crear_espartano_elite


    

def abstraccion():
    print(f"******Abstracción******")
    npc_1 = Personaje.crear_npc_basico()

if __name__ == '__main__':  #esto solo se ejecuta cuando corra este archivo, no cuando lo mande llamar
    encapsulamiento()
    herencia()
    polimorfismo()
    abstraccion()






"""
enzo._Asesino__nivel_sigilo = 4000
print(enzo)

esto si te permite modificar los valores

"""