"""
records.py - Versión 2 (Habla Correcto)
Gestión del historial y guardado persistente en formato JSON.
"""
import json
import os
from datetime import datetime

ARCHIVO_JSON = "records.json"

def cargar_historial():
    """Lee el archivo JSON. Si no existe, devuelve una estructura vacía."""
    if not os.path.exists(ARCHIVO_JSON):
        return {"historial_partidas": []}
    try:
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"historial_partidas": []}

def guardar_partida(jugador, stats, ganador_equipo):
    """
    Guarda los resultados de un jugador individual al final de la partida.
    Recibe: objeto Jugador, objeto Estadisticas, string con el equipo ganador.
    """
    historial = cargar_historial()
    r = stats.resumen()

    entrada = {
        "fecha":       datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "nombre":      jugador.nombre,
        "aciertos":    r["aciertos"],
        "errores":     r["errores"],
        "racha_max":   r["racha_max"],
        "porcentaje":  r["porcentaje"],
        "tiempo_prom": r["tiempo_prom"],
        "resultado":   "Victoria" if jugador.nombre in [j for j in [ganador_equipo]] else "Derrota",
    }

    historial["historial_partidas"].append(entrada)

    try:
        with open(ARCHIVO_JSON, "w", encoding="utf-8") as f:
            json.dump(historial, f, indent=4, ensure_ascii=False)
        print("💾 Resultados guardados en records.json")
    except Exception as e:
        print(f"⚠️ No se pudo guardar: {e}")

def mostrar_historial():
    """Imprime el historial de partidas guardadas."""
    historial = cargar_historial()
    partidas  = historial.get("historial_partidas", [])

    print("\n🏆 ===== HISTORIAL DE PARTIDAS =====")
    if not partidas:
        print("  Aún no hay partidas guardadas.")
    else:
        for i, p in enumerate(partidas[-10:], 1):   # últimas 10
            print(f"\n  {i}. {p['nombre']} — {p['fecha']}")
            print(f"     ✔ {p['aciertos']} aciertos  ❌ {p['errores']} errores")
            print(f"     🔥 Mejor racha: {p['racha_max']}  |  📈 {p['porcentaje']}%")
    print("====================================")