# jugadores.py - Sistema de jugadores V2

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vidas = 3
        self.racha = 0
        self.aciertos = 0
        self.errores = 0

    def registrar_acierto(self, tiempo=0, tipo="palabra"):
        self.aciertos += 1
        self.racha += 1

    def registrar_error(self, tiempo=0):
        self.errores += 1
        self.racha = 0
        self.vidas -= 1


def crear_jugador():
    nombre = input("👤 Nombre del jugador: ")
    return Jugador(nombre)


def crear_equipos():
    print("\n⚔️ CONFIGURACIÓN DE EQUIPOS")

    num = int(input("¿Cuántos jugadores? (2-10): "))

    jugadores = []
    for i in range(num):
        print(f"\nJugador {i+1}")
        jugadores.append(crear_jugador())

    equipos = {"Azul": [], "Rojo": []}

    for i, j in enumerate(jugadores):
        if i % 2 == 0:
            equipos["Azul"].append(j)
        else:
            equipos["Rojo"].append(j)

    print("\n🏆 Equipos creados:")
    print("🔵 Azul:", [j.nombre for j in equipos["Azul"]])
    print("🔴 Rojo:", [j.nombre for j in equipos["Rojo"]])

    return equipos