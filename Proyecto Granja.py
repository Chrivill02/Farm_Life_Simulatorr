#Espacio para Angie(Calendario y Planificación)
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






#Espacio para Rodrigo (Economía y mercado)







#Espacio para Karen(Animales)







#Espacio para Chris (Cultivos)
#Borrar esto
#Corregir errores
import random


class Hortaliza:
    def __init__(self, nombre, precio, puntos_salud, semillas):
        self.nombre = nombre
        self.precio = precio
        self.puntos_salud = puntos_salud
        self.semillas = semillas

    def mostrar_datos(self):
        print("Precio: ", self.precio)
        print("Puntos de salud: ", self.puntos_salud)
        print("Semillas: ", self.semillas)

    def Dar_Semillas(self):
        return self.semillas


class Manzana(Hortaliza):
    def __init__(self, nombre="Manzana", precio=25, puntos_salud=10, semillas=3):
        super().__init__(nombre, precio, puntos_salud, semillas)


class Pera(Hortaliza):
    def __init__(self, nombre="Pera", precio=30, puntos_salud=15, semillas=3):
        super().__init__(nombre, precio, puntos_salud, semillas)


class Uva(Hortaliza):
    def __init__(self, nombre="Uva", precio=50, puntos_salud=25, semillas=2):
        super().__init__(nombre, precio, puntos_salud, semillas)


class Pimiento(Hortaliza):
    def __init__(self, nombre="Pimiento", precio=15, puntos_salud=5, semillas=5):
        super().__init__(nombre, precio, puntos_salud, semillas)


class Tomate(Hortaliza):
    def __init__(self, nombre="Tomate", precio=10, puntos_salud=5, semillas=4):
        super().__init__(nombre, precio, puntos_salud, semillas)


class Semilla:
    def __init__(self, es_brote=False, es_crecimiento=False, es_madura=False, tiene_agua=False
                 , tiene_fertilizante=False, tiene_plaga=False, dia_semilla=0, agua=0):
        self.precio = 0
        self.es_brote = es_brote
        self.es_crecimiento = es_crecimiento
        self.es_madura = es_madura
        self.tiene_agua = tiene_agua
        self.tiene_fertilizante = tiene_fertilizante
        self.tiene_plaga = tiene_plaga
        self.dia_semilla = dia_semilla
        self.agua = agua

    def Mostrar_Datos(self):
        print("Nombre: ", "")
        print("Precio: ", self.precio)
        print("Agua: ", self.agua)
        if self.tiene_plaga == True:
            print("Tiene plaga: Si")
        else:
            print("Tiene plaga: No")
        if self.tiene_fertilizante == True:
            print("Tiene fertilizante: Si")
        else:
            print("Tiene fertilizante: No")

    def Random_Plaga(self):
        if random.randrange(15) == 10:
            self.Recibir_Plaga()

    def Recibir_Agua(self):
        if self.agua == 30:
            self.Crecer()
        elif self.agua == 50:
            self.Madurar()
        self.agua = self.agua + 10

    def Relentizar_Crecimiento(self):
        self.agua = self.agua - 15

    def Recibir_Plaga(self):
        self.tiene_plaga = True

    def Morir(self, no_suelo):
        if self.agua < 0:
            listaSuelos[no_suelo].tiene_semilla = False
            listaSuelos[no_suelo].hortaliza = "No hay hortaliza"
            listaSemillas[listaSuelos[no_suelo].numero_semilla].es_madura = False
            listaSuelos[no_suelo].semilla = "No tiene semilla"
            print(listaSemillas[listaSuelos[no_suelo].numero_semilla].nombre_madura, " Podrido y desechado :(")

    def Recibir_Fertilizante(self):
        self.tiene_fertilizante = True
        inventario.fertilizantes = inventario.fertilizantes - 1

    def Acelerar_Crecimiento(self):
        if self.tiene_fertilizante == True:
            self.agua = self.agua + 10

    def Crecer(self):
        self.es_crecimiento = True
        self.es_brote = False
        print("Su semilla está en floracion")

    def Madurar(self):
        self.es_madura = True
        self.es_crecimiento = False
        print("Su semilla está madura, lista para cosechar")

    def Actualizar_Crecimiento(self, no_suelo):
        if self.tiene_plaga:
            self.Relentizar_Crecimiento()
        self.Morir(no_suelo)
        if self.tiene_fertilizante == True:
            self.agua = self.agua + 10


class Semilla_Manzana(Semilla):
    def __init__(self, es_brote=False, es_crecimiento=False, es_madura=False, tiene_agua=False
                 , tiene_fertilizante=False, tiene_plaga=False, dia_semilla=0):
        super().__init__(es_brote, es_crecimiento, es_madura, tiene_agua, tiene_fertilizante, tiene_plaga, dia_semilla)
        self.nombre_backend = "Semilla_Manzana"
        self.nombre_informal = "Semilla de Manzana"
        self.nombre_madura = "Manzana"
        self.precio = 10

    def Mostrar_Datos(self):
        print("Nombre: ", "Semilla de Manzana")
        print("Precio: ", self.precio)
        print("Agua: ", self.agua)
        if self.tiene_plaga == True:
            print("Tiene plaga: Si")
        else:
            print("Tiene plaga: No")
        if self.tiene_fertilizante == True:
            print("Tiene fertilizante: Si")
        else:
            print("Tiene fertilizante: No")


class Semilla_Pera(Semilla):
    def __init__(self, es_brote=False, es_crecimiento=False, es_madura=False, tiene_agua=False,
                 tiene_fertilizante=False, tiene_plaga=False, dia_semilla=0):
        super().__init__(es_brote, es_crecimiento, es_madura, tiene_agua, tiene_fertilizante, tiene_plaga, dia_semilla)
        self.nombre_backend = "Semilla_Pera"
        self.nombre_informal = "Semilla de Pera"
        self.nombre_madura = "Pera"
        self.precio = 8

    def Mostrar_Datos(self):
        print("Nombre: ", "Semilla de Pera")
        print("Precio: ", self.precio)
        print("Agua: ", self.agua)
        if self.tiene_plaga == True:
            print("Tiene plaga: Si")
        else:
            print("Tiene plaga: No")
        if self.tiene_fertilizante == True:
            print("Tiene fertilizante: Si")
        else:
            print("Tiene fertilizante: No")


class Semilla_Tomate(Semilla):
    def __init__(self, es_brote=False, es_crecimiento=False, es_madura=False, tiene_agua=False,
                 tiene_fertilizante=False, tiene_plaga=False, dia_semilla=0):
        super().__init__(es_brote, es_crecimiento, es_madura, tiene_agua, tiene_fertilizante, tiene_plaga, dia_semilla)
        self.nombre_backend = "Semilla_Tomate"
        self.nombre_informal = "Semilla de Tomate"
        self.nombre_madura = "Tomate"
        self.precio = 5

    def Mostrar_Datos(self):
        print("Nombre: ", "Semilla de Tomate")
        print("Precio: ", self.precio)
        print("Agua: ", self.agua)
        if self.tiene_plaga == True:
            print("Tiene plaga: Si")
        else:
            print("Tiene plaga: No")
        if self.tiene_fertilizante == True:
            print("Tiene fertilizante: Si")
        else:
            print("Tiene fertilizante: No")


class Semilla_Pimiento(Semilla):
    def __init__(self, es_brote=False, es_crecimiento=False, es_madura=False, tiene_agua=False,
                 tiene_fertilizante=False, tiene_plaga=False, dia_semilla=0):
        super().__init__(es_brote, es_crecimiento, es_madura, tiene_agua, tiene_fertilizante, tiene_plaga, dia_semilla)
        self.nombre_backend = "Semilla_Pimiento"
        self.nombre_informal = "Semilla de Pimiento"
        self.nombre_madura = "Pimiento"
        self.precio = 4

    def Mostrar_Datos(self):
        print("Nombre: ", "Semilla de Pimiento")
        print("Precio: ", self.precio)
        print("Agua: ", self.agua)
        if self.tiene_plaga == True:
            print("Tiene plaga: Si")
        else:
            print("Tiene plaga: No")
        if self.tiene_fertilizante == True:
            print("Tiene fertilizante: Si")
        else:
            print("Tiene fertilizante: No")


class Semilla_Uva(Semilla):
    def __init__(self, es_brote=False, es_crecimiento=False, es_madura=False, tiene_agua=False,
                 tiene_fertilizante=False, tiene_plaga=False, dia_semilla=0):
        super().__init__(es_brote, es_crecimiento, es_madura, tiene_agua, tiene_fertilizante, tiene_plaga, dia_semilla)
        self.nombre_backend = "Semilla_Uva"
        self.nombre_informal = "Semilla de Uva"
        self.nombre_madura = "Uva"
        self.precio = 10

    def Mostrar_Datos(self):
        print("Nombre: ", "Semilla de Uva")
        print("Precio: ", self.precio)
        print("Agua: ", self.agua)
        if self.tiene_plaga == True:
            print("Tiene plaga: Si")
        else:
            print("Tiene plaga: No")
        if self.tiene_fertilizante == True:
            print("Tiene fertilizante: Si")
        else:
            print("Tiene fertilizante: No")


class Terreno:
    def __init__(self, espacio_siembra, nivel, precio):
        self.espacio_siembra = espacio_siembra
        self.nivel = nivel
        self.precio = precio

    def Verificar_Suelos_Disponibles(self):
        for i in range(0, len(listaSuelos)):
            if listaSuelos[i].tiene_semilla == True:
                print("Suelo: ", listaSuelos[i].Get_Numero(), " no disponible")
            else:
                print("Suelo: ", listaSuelos[i].Get_Numero(), " disponible")

    def Actualizar(self):
        contador_espacios = 5
        for i in range(0, len(listaSuelos)):
            if listaSuelos[i].tiene_semilla == True:
                contador_espacios = contador_espacios - 1
            else:
                continue
        self.espacio_siembra = contador_espacios


class Inventario:
    def __init__(self, semillas_manzana, semillas_pera, semillas_uva, semillas_pimiento, semillas_tomate,
                 manzanas=0, peras=0, uvas=0, pimientos=0, tomates=0, fertilizantes=3):
        self.semillas_manzana = semillas_manzana
        self.semillas_pera = semillas_pera
        self.semillas_uva = semillas_uva
        self.semillas_pimiento = semillas_pimiento
        self.semillas_tomate = semillas_tomate
        self.manzanas = manzanas
        self.peras = peras
        self.uvas = uvas
        self.pimientos = pimientos
        self.tomates = tomates
        self.fertilizantes = fertilizantes

    def Agregar_Semilla(self, Nombre_Semilla, numero_semillas):
        if Nombre_Semilla == "Semilla_Manzana":
            self.semillas_manzana = self.semillas_manzana + numero_semillas
        elif Nombre_Semilla == "Semilla_Pera":
            self.semillas_pera = self.semillas_pera + numero_semillas
        elif Nombre_Semilla == "Semilla_Uva":
            self.semillas_uva = self.semillas_uva + numero_semillas
        elif Nombre_Semilla == "Semilla_Pimiento":
            self.semillas_pimiento = self.semillas_pimiento + numero_semillas
        elif Nombre_Semilla == "Semilla_Tomate":
            self.semillas_tomate = self.semillas_tomate + numero_semillas

    def Eliminar_Semilla(self, Nombre_Semilla):
        if Nombre_Semilla == "Semilla_Manzana":
            self.semillas_manzana = self.semillas_manzana - 1
        elif Nombre_Semilla == "Semilla_Pera":
            self.semillas_pera = self.semillas_pera - 1
        elif Nombre_Semilla == "Semilla_Uva":
            self.semillas_uva = self.semillas_uva - 1
        elif Nombre_Semilla == "Semilla_Pimiento":
            self.semillas_pimiento = self.semillas_pimiento - 1
        elif Nombre_Semilla == "Semilla_Tomate":
            self.semillas_tomate = self.semillas_tomate - 1

    def Agregar_Hortalizas(self, Hortaliza):
        if Hortaliza == "Manzana":
            self.manzanas = self.manzanas + 1
        elif Hortaliza == "Pera":
            self.peras = self.peras + 1
        elif Hortaliza == "Uva":
            self.uvas = self.uvas + 1
        elif Hortaliza == "Pimiento":
            self.pimientos = self.pimientos + 1
        elif Hortaliza == "Tomate":
            self.tomates = self.tomates + 1

    def Eliminar_Hortaliza(self, Hortaliza):
        if Hortaliza == "Manzana":
            self.manzanas = self.manzanas - 1
        elif Hortaliza == "Pera":
            self.peras = self.peras - 1
        elif Hortaliza == "Uva":
            self.uvas = self.uvas - 1
        elif Hortaliza == "Pimiento":
            self.pimientos = self.pimientos - 1
        elif Hortaliza == "Tomate":
            self.tomates = self.tomates - 1

    def Mostrar(self):
        print(self.semillas_manzana, " Semillas de Manzana")
        print(self.semillas_pera, " Semillas de Pera")
        print(self.semillas_uva, " Semilas de Uva")
        print(self.semillas_tomate, " Semillas de Tomate")
        print(self.semillas_pimiento, " Semillas de Pimiento")
        print(self.manzanas, " Manzanas")
        print(self.peras, " Peras")
        print(self.uvas, " Uvas")
        print(self.tomates, " Tomates")
        print(self.pimientos, " Pimientos")
        print(self.fertilizantes, " Fertilizantes")


class Suelo:
    def __init__(self, tiene_semilla, _numero, semilla="No tiene semilla", numero_semilla=10, tiene_agua=False,
                 dia_semilla=0, hortaliza="No hay hortaliza"):
        self.tiene_semilla = tiene_semilla
        self._numero = _numero
        self.semilla = semilla
        self.numero_semilla = numero_semilla
        self.tiene_agua = tiene_agua
        self.dia_semilla = dia_semilla
        self.hortaliza = hortaliza

    def fertilizar(self):
        self.tiene_fertilizante = True

    def relentizar_proceso(self):
        self.tiene_plaga = True

    def Parar_Proceso(self):
        self.tiene_agua = False

    def Mostrar_Datos(self):
        print("¿Tiene agua el suelo? ", self.tiene_agua)
        print("¿Tiene fertilizante el suelo? ", self.tiene_fertilizante)
        print("¿Tiene plaga el suelo? ", self.tiene_plaga)
        print("¿Tiene semilla el suelo? ", self.tiene_semilla)

    def Agregar_Semilla(self, Nombre_de_semilla):
        self.semilla = Nombre_de_semilla

    def Agregar_Hortaliza(self, Hortaliza):
        self.hortaliza = Hortaliza

    def Get_Numero(self):
        return self._numero


# Esto es como una actualizacion del tiempo


def Sembrar(Nombre_Semilla, Nombre_Informal_Semilla, index_Semilla, hortaliza):
    print("¿En que suelo deseas sembrarlo? ")
    terreno.Verificar_Suelos_Disponibles()
    opcion_suelo = int(input("Ingrese el numero del suelo que deseas: "))
    if listaSuelos[opcion_suelo].tiene_semilla == True:
        print("Suelo ocupado")
    else:
        listaSuelos[opcion_suelo].tiene_semilla = True
        listaSuelos[opcion_suelo].Agregar_Semilla(Nombre_Informal_Semilla)
        listaSuelos[opcion_suelo].Agregar_Hortaliza(hortaliza)
        listaSuelos[opcion_suelo].numero_semilla = index_Semilla
        listaSemillas[index_Semilla].nombre_informal = ""
        listaSemillas[index_Semilla].es_brote = True
        listaSemillas[index_Semilla].dia_semilla = calendario.dia
        inventario.Eliminar_Semilla(Nombre_Semilla)
        terreno.Actualizar()
        print(Nombre_Informal_Semilla, " sembrada en suelo ", listaSuelos[opcion_suelo].Get_Numero())



# Aca voy
def Cosechar():
    opcion_suelo = int(input("Ingrese el numero del suelo para cosechar su hortaliza: "))
    if listaSuelos[opcion_suelo].tiene_semilla == False:
        print("No hay semilla")
    elif listaSemillas[listaSuelos[opcion_suelo].numero_semilla].es_madura == False:
        print("Hortaliza no madura")
    else:
        hortaliza = listaSemillas[listaSuelos[opcion_suelo].numero_semilla].nombre_madura
        if hortaliza == "Manzana":
            listaHortalizas.append(Manzana)
            inventario.Agregar_Semilla("Semilla_Manzana", manzana.Dar_Semillas())
            for i in range(0, manzana.Dar_Semillas()):
                listaSemillas.append(Semilla_Manzana())
        elif hortaliza == "Pera":
            listaHortalizas.append(Pera)
            inventario.Agregar_Semilla("Semilla_Pera", pera.Dar_Semillas())
            for i in range(0, pera.Dar_Semillas()):
                listaSemillas.append(Semilla_Pera())
        elif hortaliza == "Uva":
            listaHortalizas.append(Uva)
            inventario.Agregar_Semilla("Semilla_Uva", uva.Dar_Semillas())
            for i in range(0, uva.Dar_Semillas()):
                listaSemillas.append(Semilla_Uva())
        elif hortaliza == "Pimiento":
            listaHortalizas.append(Pimiento)
            inventario.Agregar_Semilla("Semilla_Pimiento", pimiento.Dar_Semillas())
            for i in range(0, pimiento.Dar_Semillas()):
                listaSemillas.append(Semilla_Pimiento())
        elif hortaliza == "Tomate":
            listaHortalizas.append(Tomate)
            inventario.Agregar_Semilla("Semilla_Tomate", tomate.Dar_Semillas())
            for i in range(0, tomate.Dar_Semillas()):
                listaSemillas.append(Semilla_Tomate())
        inventario.Agregar_Hortalizas(hortaliza)
        listaSuelos[opcion_suelo].tiene_semilla = False
        listaSuelos[opcion_suelo].hortaliza = "No hay hortaliza"
        listaSemillas[listaSuelos[opcion_suelo].numero_semilla].es_madura = False
        listaSuelos[opcion_suelo].semilla = "No tiene semilla"
        print(listaSemillas[listaSuelos[opcion_suelo].numero_semilla].nombre_madura, " cosechad(o)a")


def Regar():
    calendario.avanzar_tiempo(60)
    calendario.mostrar_fecha_hora()
    decision = "S"
    while decision == "S" or decision == "s":
        for i in range(0, len(listaSuelos)):
            print("Suelo: ", listaSuelos[i].Get_Numero(), " , ", listaSuelos[i].semilla)
        opcion_suelo = int(input("Ingrese el numero del suelo que desea regar: "))
        calendario.avanzar_tiempo(60)
        calendario.mostrar_fecha_hora()
        if listaSuelos[opcion_suelo].tiene_semilla == False:
            print("No hay semillas en este suelo")
            decision = input("¿Desea regar otra semilla? (S/N): ")
        else:
            listaSemillas[listaSuelos[opcion_suelo].numero_semilla].tiene_agua = True
            listaSemillas[listaSuelos[opcion_suelo].numero_semilla].Recibir_Agua()
            listaSemillas[listaSuelos[opcion_suelo].numero_semilla].Random_Plaga()
            listaSemillas[listaSuelos[opcion_suelo].numero_semilla].Actualizar_Crecimiento(opcion_suelo)
            listaSemillas[listaSuelos[opcion_suelo].numero_semilla].Mostrar_Datos()
            listaSemillas[listaSuelos[opcion_suelo].numero_semilla].dia_semilla = calendario.dia
            listaSuelos[opcion_suelo].dia_semilla = calendario.dia
            listaSuelos[opcion_suelo].tiene_agua = True
            decision = input("¿Desea regar otra semilla? (S/N): ")


# Uso de ejemplo
calendario = Calendario()

opcion = 1
listaSemillas = []
listaSuelos = []
listaHortalizas = []
manzana = Manzana()
pera = Pera()
uva = Uva()
pimiento = Pimiento()
tomate = Tomate()
listaSemillas.append(Semilla_Tomate())
listaSemillas.append(Semilla_Uva())
listaSemillas.append(Semilla_Pimiento())
listaSemillas.append(Semilla_Pera())
listaSemillas.append(Semilla_Manzana())
inventario = Inventario(1, 1, 1, 1, 1)
listaSuelos.append(Suelo(False, 0))
listaSuelos.append(Suelo(False, 1))
listaSuelos.append(Suelo(False, 2))
listaSuelos.append(Suelo(False, 3))
listaSuelos.append(Suelo(False, 4))
terreno = Terreno(5, 1, 1000)

while opcion != 0:

    calendario.avanzar_tiempo(60)
    calendario.mostrar_fecha_hora()
    # Avanza el tiempo en minutos (ajusta según tus necesidades)while opcion != 0:
    print("Bienvenido a Farm Simulator! ")
    print("Selecciona la opción que deseas: ")
    print("1. Cultivos y cosechas")
    print("2. Cuidado de animales")
    print("3. Economía y comercio")
    print("4. Ver inventario")
    print("0. Salir")
    opcion = int(input(""))
    if opcion == 1:

        calendario.avanzar_tiempo(60)
        calendario.mostrar_fecha_hora()

        opcion_cosechas = 1
        while opcion_cosechas != 0:
            print("Bienvenido al espacio de cultivos y cosechas! ¿Que deseas hacer?")
            print("1. Sembrar")
            print("2. Regar")
            print("3. Cosechar")
            print("4. Ver inventario")
            print("5. Ver Hora")
            print("0. Salir")
            opcion_cosechas = int(input(""))
            if opcion_cosechas == 1:

                calendario.avanzar_tiempo(60)
                calendario.mostrar_fecha_hora()
                opcion_siembra = 1

                if terreno.espacio_siembra == 0:
                    print("Ya no tienes más espacios para sembrar")
                    print("Cultiva o mejora el terreno para sembrar más")
                else:
                    print("Tienes: ", terreno.espacio_siembra, " espacios para sembrar.")
                    print("¿Que deseas sembrar? ")

                    for i in range(0, len(listaSemillas)):
                        print(i, ". ", listaSemillas[i].nombre_informal)
                    opcion_siembra = int(input(""))
                    if listaSemillas[opcion_siembra].nombre_informal == "":
                        print("No hay semillas aqui ")
                    else:
                        Sembrar(listaSemillas[opcion_siembra].nombre_backend,
                                listaSemillas[opcion_siembra].nombre_informal
                                , opcion_siembra, listaSemillas[opcion_siembra].nombre_madura)

            elif opcion_cosechas == 2:
                Regar()

            elif opcion_cosechas == 3:
                for i in range(0, len(listaSuelos)):
                    print("Suelo: ", listaSuelos[i].Get_Numero(), " , ", listaSuelos[i].hortaliza)
                    if listaSuelos[i].tiene_semilla == True:
                        if listaSemillas[listaSuelos[i].numero_semilla].es_madura == True:
                            print("Madura")
                        else:
                            print("No madura")
                    else:
                        print("No hay semilla")
                Cosechar()
            elif opcion_cosechas == 4:
                calendario.avanzar_tiempo(60)
                calendario.mostrar_fecha_hora()
                print("Bienvenido al inventario")
                inventario.Mostrar()
                print("¿Deseas utilizar algo?")
                print("1. Fertilizante ")
                print("0. Salir")
                opcion_inventario = int(input())
                if opcion_inventario == 1 and inventario.fertilizantes > 0:
                    print("¿En que suelo deseas usar el fertilizante?")
                    for i in range(0, len(listaSuelos)):
                        print("Suelo: ", listaSuelos[i].Get_Numero(), " , ", listaSuelos[i].semilla)
                    opcion_suelo = int(input("Ingrese el numero del suelo que desea regar: "))
                    calendario.avanzar_tiempo(60)
                    calendario.mostrar_fecha_hora()
                    if listaSuelos[opcion_suelo].tiene_semilla == False:
                        print("No hay semillas en este suelo")
                    else:
                        listaSemillas[listaSuelos[opcion_suelo].numero_semilla].Recibir_Fertilizante()

            elif opcion_cosechas == 5:

                calendario.avanzar_tiempo(60)
                calendario.mostrar_fecha_hora()

            elif opcion_cosechas == 7:

                calendario.avanzar_tiempo(1440)
                calendario.mostrar_fecha_hora()

    elif opcion == 2:

        calendario.avanzar_tiempo(60)
        calendario.mostrar_fecha_hora()
        print("Bienvenido al espacio de cuidado de animales")
    elif opcion == 3:

        calendario.avanzar_tiempo(60)
        calendario.mostrar_fecha_hora()
        print("Bienvenido al espacio de economía y comercio")
    elif opcion == 4:

        calendario.avanzar_tiempo(60)
        calendario.mostrar_fecha_hora()
        print("Bienvenido al inventario")
        inventario.Mostrar()
    elif opcion == 5:

        calendario.avanzar_tiempo(60)
        calendario.mostrar_fecha_hora()
    elif opcion == 7:

        calendario.avanzar_tiempo(1440)
        calendario.mostrar_fecha_hora()



