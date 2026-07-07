# combate.py - Motor final V2

import os
import time
from estadisticas import Estadisticas
import puntuacion
import records


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def iniciar_combate(equipos, callback):
    jugadores = equipos["Azul"] + equipos["Rojo"]

    stats = {j.nombre: Estadisticas() for j in jugadores}
    puntajes = {j.nombre: 0 for j in jugadores}

    print("⚔️ COMBATE INICIADO")

    while True:

        for jugador in jugadores:

            if jugador.vidas <= 0:
                continue

            limpiar_pantalla()

            print(f"🎮 Turno de {jugador.nombre}")
            input("🎤 ENTER para hablar...")

            inicio = time.time()
            resultado = callback(jugador)
            tiempo = round(time.time() - inicio, 2)

            if resultado:
                jugador.registrar_acierto()
                stats[jugador.nombre].registrar_acierto(tiempo)
                puntos = puntuacion.calcular_puntos("medio", "palabras")
                puntajes[jugador.nombre] += puntos
                print(f"✅ +{puntos} puntos")

            else:
                jugador.registrar_error()
                stats[jugador.nombre].registrar_error()
                print("❌ Fallo")

            time.sleep(1)

            # CONDICIÓN DE FIN
            if all(j.vidas <= 0 for j in equipos["Azul"]):
                ganador = "Rojo"
                return finalizar(equipos, stats, puntajes, ganador)

            if all(j.vidas <= 0 for j in equipos["Rojo"]):
                ganador = "Azul"
                return finalizar(equipos, stats, puntajes, ganador)


def finalizar(equipos, stats, puntajes, ganador):

    limpiar_pantalla()

    print("\n🏆 FIN DEL JUEGO")
    print("=" * 40)
    print(f"🥇 Ganador: Equipo {ganador}")
    print("\n📊 ESTADÍSTICAS FINALES\n")

    for nombre, s in stats.items():
        r = s.resumen()
        print(f"👤 {nombre}")
        print(f"✔ Aciertos: {r['aciertos']}")
        print(f"❌ Errores: {r['errores']}")
        print(f"🔥 Mejor racha: {r['racha_max']}")
        print(f"📈 % éxito: {r['porcentaje']}%")
        print(f"⏱ Tiempo prom: {r['tiempo_prom']}s")
        print(f"⭐ Puntos: {puntajes[nombre]}")
        print("-" * 30)

    # Guardar records
    for jugador in equipos["Azul"] + equipos["Rojo"]:
        records.guardar_partida(jugador, stats[jugador.nombre], ganador)

    input("\nENTER para salir...")