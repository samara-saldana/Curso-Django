from poo_test import Guerrero, Mago, Clerigo, Asesino

def simular_combate():
    print("Bienvenido al coliseo")
    mago = Mago("Harry",120, 60)
    clerigo = Clerigo("Sirio", 150, 87)

    guerrero = Guerrero("Amadeus", 200, 130)

    espartano = Guerrero.crear_espartano_elite()

    asesino = Asesino("Scar", 150)

    tiempo_pelea = 2
    while tiempo_pelea > 0:
        print("Turno del mago")
        mago.lanzar_hechizo(guerrero)

        print("Turno del asesino")
        asesino * 3
        guerrero.salud -=45

        dano_jefe=60

        print("turno del jefe")
        print("el espartano golpea al mago")
        mago.salud -= dano_jefe

        print("Turno del clerigo")
        clerigo >> mago

        print(mago)
        print(clerigo)
        print(guerrero)
        print(espartano)
        print(asesino)


        tiempo_pelea -=1


if __name__ == '__main__':
    simular_combate()