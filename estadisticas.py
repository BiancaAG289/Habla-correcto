# estadisticas.py - Versión 2 (Habla Correcto)

class Estadisticas:
    def __init__(self):
        self.aciertos = 0
        self.errores = 0
        self.racha = 0
        self.racha_max = 0
        self.tiempos = []

    def registrar_acierto(self, tiempo):
        self.aciertos += 1
        self.racha += 1
        if self.racha > self.racha_max:
            self.racha_max = self.racha
        self.tiempos.append(tiempo)

    def registrar_error(self, tiempo=0):
        self.errores += 1
        self.racha = 0
        self.tiempos.append(tiempo)

    def promedio_tiempo(self):
        if not self.tiempos:
            return 0
        return round(sum(self.tiempos) / len(self.tiempos), 2)

    def resumen(self):
        total = self.aciertos + self.errores
        porcentaje = round((self.aciertos / total) * 100, 1) if total > 0 else 0
        return {
            "aciertos":    self.aciertos,
            "errores":     self.errores,
            "racha_max":   self.racha_max,
            "porcentaje":  porcentaje,
            "tiempo_prom": self.promedio_tiempo(),
        }