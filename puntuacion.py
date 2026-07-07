"""
puntuacion.py - Versión 2 (Habla Correcto)
Sistema de cálculo de puntos dinámico por dificultad y tipo de reto.
"""

def calcular_puntos(nivel, tipo_reto, racha=0):
    """
    Calcula los puntos basándose en la dificultad y añade un bonus por racha.
    """
    # Puntos base por nivel
    base_puntos = {
        "facil": 10,
        "medio": 20,
        "dificil": 35
    }
    
    puntos = base_puntos.get(nivel, 10)
    
    # Multiplicador si es una oración completa (requiere más esfuerzo)
    if tipo_reto == "oraciones":
        puntos = int(puntos * 1.5)
        
    # Bonus por racha de aciertos continua
    if racha >= 3:
        puntos += 5
    if racha >= 5:
        puntos += 10
        
    return puntos