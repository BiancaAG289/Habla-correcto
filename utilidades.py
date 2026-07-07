# utilidades.py - Funciones auxiliares V2

import os
import time

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def efecto_carga(texto="Cargando", segundos=3):
    print(texto, end="")
    for _ in range(segundos):
        time.sleep(0.5)
        print(".", end="")
    print()


def titulo():
    print("===================================")
    print("🎙️ HABLA CORRECTO - V2")
    print("===================================")


def pausa():
    input("\n⏸️ Presiona ENTER para continuar...")