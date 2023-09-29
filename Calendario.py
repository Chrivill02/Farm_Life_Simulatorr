import time

class Calendario:
    def __init__(self, hora_inicial=6, minutos_iniciales=0, dia_inicial=1, estacion_inicial="Primavera"):
        self.hora = hora_inicial
        self.minutos = minutos_iniciales
        self.dia = dia_inicial
        self.estacion = estacion_inicial

    def avanzar_tiempo(self, minutos):
        self.minutos += minutos
        while self.minutos >= 60:
            self.minutos -= 60
            self.hora += 1
            if self.hora >= 24:
                self.hora = 0
                self.dia += 1
                if self.dia > 30:
                    self.dia = 1
                    self.cambiar_estacion()

    def cambiar_estacion(self):
        estaciones = ["Primavera", "Verano", "Otoño", "Invierno"]
        estacion_actual = estaciones.index(self.estacion)
        self.estacion = estaciones[(estacion_actual + 1) % len(estaciones)]

    def mostrar_fecha_hora(self):
        print(f"Día {self.dia} de {self.estacion}, {self.hora:02d}:{self.minutos:02d}")

calendario = Calendario()

while True:
    calendario.mostrar_fecha_hora()
    time.sleep(1)
    calendario.avanzar_tiempo(10)  