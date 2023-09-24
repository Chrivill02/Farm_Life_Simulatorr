#Espacio para Angie(Calendario y Planificación)







#Espacio para Rodrigo (Economía y mercado)







#Espacio para Karen(Animales)







#Espacio para Chris (Cultivos)
#Borrar esto
#Corregir errores

class Hortaliza:
    def __init__(self,nombre, precio, aspecto, puntos_salud,semillas ):
        self.nombre = nombre
        self.precio = precio
        self.aspecto = aspecto
        self.puntos_salud = puntos_salud
        self.semillas = semillas

    def mostrar_datos(self):
        print("Precio: ", self.precio)
        print("Aspecto: ", self.aspecto)
        print("Puntos de salud: ", self.puntos_salud)
        print("Semillas: ", self.semillas)

class Semilla:
    def __init__(self, es_brote = False, es_crecimiento = False, es_madura = False, tiene_agua = False
                 , tiene_fertilizante = False, tiene_plaga = False, hora_semilla = False):

        self.precio = 0
        self.es_brote = es_brote
        self.es_crecimiento = es_crecimiento
        self.es_madura = es_madura
        self.tiene_agua = tiene_agua
        self.tiene_fertilizante = tiene_fertilizante
        self.tiene_plaga = tiene_plaga
        self.hora_semilla = hora_semilla

    def Mostrar_Datos(self):
        print("Nombre: ", "")
        print("Precio: ", self.precio)
        print("Tiene agua: ", self.tiene_agua)

    def Crecer(self):
        if self.es_brote == True:
            self.es_crecimiento = True
            self.es_brote = False
            print("Su semilla está en floracion")
        elif self.es_crecimiento == True:
            self.es_madura = True
            self.es_crecimiento = False
            print("Su semilla está madura, lista para cosechar ")

    def Madurar(self):
        self.es_madura = True
        self.es_crecimiento = False




class Semilla_Manzana(Semilla):
    def __init__(self,  es_brote = False, es_crecimiento = False, es_madura = False, tiene_agua = False
                 , tiene_fertilizante = False, tiene_plaga = False, hora_semilla = 0):
        super().__init__(  es_brote, es_crecimiento, es_madura, tiene_agua, tiene_fertilizante, tiene_plaga, hora_semilla)
        self.nombre_backend = "Semilla_Manzana"
        self.nombre_informal = "Semilla de Manzana"
        self.precio = 10

    def Mostrar_Datos(self):
        print("Nombre: ", "Semilla de Manzana")
        print("Precio: ", self.precio)
        print("Tiene agua: ", self.tiene_agua)



class Semilla_Pera(Semilla):
    def __init__(self,  es_brote = False, es_crecimiento = False, es_madura = False, tiene_agua = False,
                 tiene_fertilizante = False, tiene_plaga = False, hora_semilla = 0):
        super().__init__( es_brote, es_crecimiento, es_madura,tiene_agua, tiene_fertilizante, tiene_plaga , hora_semilla)
        self.nombre_backend = "Semilla_Pera"
        self.nombre_informal = "Semilla de Pera"
        self.precio = 8


    def Mostrar_Datos(self):
        print("Nombre: ", "Semilla de Pera")
        print("Precio: ", self.precio)
        print("Tiene agua: ", self.tiene_agua)

class Semilla_Tomate(Semilla):
    def __init__(self, es_brote = False, es_crecimiento = False, es_madura = False, tiene_agua = False,
                 tiene_fertilizante = False, tiene_plaga = False, hora_semilla = 0):
        super().__init__(  es_brote, es_crecimiento, es_madura, tiene_agua, tiene_fertilizante, tiene_plaga, hora_semilla)
        self.nombre_backend = "Semilla_Tomate"
        self.nombre_informal = "Semilla de Tomate"
        self.precio = 5

    def Mostrar_Datos(self):
        print("Nombre: ", "Semilla de Tomate")
        print("Precio: ", self.precio)
        print("Tiene agua: ", self.tiene_agua)


class Semilla_Pimiento(Semilla):
    def __init__(self,  es_brote = False, es_crecimiento = False, es_madura = False, tiene_agua = False,
                 tiene_fertilizante = False, tiene_plaga = False, hora_semilla = 0):
        super().__init__(  es_brote, es_crecimiento, es_madura, tiene_agua, tiene_fertilizante, tiene_plaga , hora_semilla)
        self.nombre_backend = "Semilla_Pimiento"
        self.nombre_informal = "Semilla de Pimiento"
        self.precio = 4

    def Mostrar_Datos(self):
        print("Nombre: ", "Semilla de Pimiento")
        print("Precio: ", self.precio)
        print("Tiene agua: ", self.tiene_agua)

class Semilla_Uva(Semilla):
    def __init__(self ,es_brote = False, es_crecimiento = False, es_madura = False,  tiene_agua = False,
                 tiene_fertilizante = False, tiene_plaga = False, hora_semilla = 0):
        super().__init__(  es_brote, es_crecimiento, es_madura,  tiene_agua, tiene_fertilizante, tiene_plaga, hora_semilla)
        self.nombre_backend = "Semilla_Uva"
        self.nombre_informal = "Semilla de Uva"
        self.precio = 10

    def Mostrar_Datos(self):
        print("Nombre: ", "Semilla de Uva")
        print("Precio: ", self.precio)
        print("Tiene agua: ", self.tiene_agua)
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
            if  listaSuelos[i].tiene_semilla == True:
                contador_espacios = contador_espacios - 1
            else:
                continue
        self.espacio_siembra = contador_espacios
class Inventario:
    def __init__(self, semillas_manzana, semillas_pera, semillas_uva, semillas_pimiento, semmillas_tomate):
        self.semillas_manzana = semillas_manzana
        self.semillas_pera = semillas_pera
        self.semillas_uva = semillas_uva
        self.semillas_pimiento = semillas_pimiento
        self.semmillas_tomate = semmillas_tomate

    def Agregar_Semilla(self,Nombre_Semilla):
        if Nombre_Semilla == "Semilla_Manzana":
            self.semillas_manzana = self.semillas_manzana + 1
        elif Nombre_Semilla == "Semilla_Pera":
            self.semillas_pera = self.semillas_pera + 1
        elif Nombre_Semilla == "Semilla_Uva":
            self.semillas_uva = self.semillas_uva + 1
        elif Nombre_Semilla == "Semilla_Pimiento":
            self.semillas_pimiento = self.semillas_pimiento + 1
        elif Nombre_Semilla == "Semilla_Tomate":
            self.semmillas_tomate = self.semmillas_tomate + 1

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
            self.semmillas_tomate = self.semmillas_tomate - 1

    def Mostrar_Semillas(self):
        print(self.semillas_manzana, " Semillas de Manzana")
        print(self.semillas_pera, " Semillas de Pera")
        print(self.semillas_uva, " Semilas de Uva")
        print(self.semmillas_tomate, " Semillas de Tomate")
        print(self.semillas_pimiento, " Semillas de Pimiento")



class Suelo:
    def __init__(self, tiene_semilla, _numero, semilla = "No tiene semilla", numero_semilla = 10, tiene_agua = False, hora_semilla = 0):
        self.tiene_semilla = tiene_semilla
        self._numero = _numero
        self.semilla = semilla
        self.numero_semilla = numero_semilla
        self.tiene_agua = tiene_agua
        self.hora_semilla = hora_semilla
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

    def Get_Numero(self):
        return self._numero

    #Esto es como una actualizacion del tiempo









#def actualizarTiempo():
#Borrar
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
                if self.dia > 30:  # Puedes ajustar esto según el número de días en tu juego
                    self.dia = 1
                    self.cambiar_estacion()
                    if self.mes == 12:
                        self.mes = 0

    def cambiar_estacion(self):
        estaciones = ["Primavera", "Verano", "Otoño", "Invierno"]  # Personaliza según las estaciones de tu juego
        estacion_actual = estaciones.index(self.estacion)
        self.estacion = estaciones[(estacion_actual + 1) % len(estaciones)]

    def mostrar_fecha_hora(self):
        print(f"Día {self.dia} de {self.estacion}, {self.hora:02d}:{self.minutos:02d}")

    def Tiempo_En_Formato(self):
        return (f" {self.dia:02d}:{self.hora:02d}:{self.minutos:02d}")



def Sembrar(Nombre_Semilla, Nombre_Informal_Semilla, index_Semilla):
    print("¿En que suelo deseas sembrarlo? ")
    terreno.Verificar_Suelos_Disponibles()
    opcion_suelo = int(input("Ingrese el numero del suelo que deseas: "))
    listaSuelos[opcion_suelo].tiene_semilla = True
    listaSuelos[opcion_suelo].Agregar_Semilla(Nombre_Informal_Semilla)
    listaSuelos[opcion_suelo].numero_semilla = index_Semilla
    listaSemillas[index_Semilla].nombre_informal = ""
    inventario.Eliminar_Semilla(Nombre_Semilla)
    terreno.Actualizar()

    print(Nombre_Informal_Semilla, " sembrada en suelo ", listaSuelos[opcion_suelo].Get_Numero())

#Por aca voy, ya muestra el tiempo, solo falta el if para usar el metodo Crecer
def Actualizar():
     for i in range(0, len(listaSuelos)):
        if listaSuelos[i].tiene_agua == True:
            print(listaSemillas[listaSuelos[i].numero_semilla].hora_semilla)


# Uso de ejemplo
calendario = Calendario()


opcion = 1
listaSemillas = []
listaSuelos = []
listaSemillas.append(Semilla_Tomate())
listaSemillas.append(Semilla_Uva())
listaSemillas.append(Semilla_Pimiento())
listaSemillas.append(Semilla_Pera())
listaSemillas.append(Semilla_Manzana())
inventario = Inventario(1,1,1,1,1)
listaSuelos.append(Suelo(False, 0))
listaSuelos.append(Suelo(False, 1))
listaSuelos.append(Suelo(False, 2))
listaSuelos.append(Suelo(False, 3))
listaSuelos.append(Suelo(False, 4))
terreno = Terreno(5, 1, 1000)


while opcion != 0:
    Actualizar()
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
        Actualizar()
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
                Actualizar()
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
                    Sembrar(listaSemillas[opcion_siembra].nombre_backend,listaSemillas[opcion_siembra].nombre_informal
                            , opcion_siembra)

                    """if opcion_siembra == 1:
                        calendario.avanzar_tiempo(10)
                        calendario.mostrar_fecha_hora()
                        if inventario.semillas_manzana == 0:
                            print("No tienes semillas de manzana")
                        else:
                            Sembrar("Semilla_Manzana", "Semilla de Manzana", 1)
                    elif opcion_siembra == 2:
                        calendario.avanzar_tiempo(10)
                        calendario.mostrar_fecha_hora()
                        if inventario.semillas_pera == 0:
                            print("No tienes semillas de pera")
                        else:
                            Sembrar("Semilla_Pera", "Semilla de Pera",2 )
                    elif opcion_siembra == 3:
                        calendario.avanzar_tiempo(10)
                        calendario.mostrar_fecha_hora()
                        if inventario.semillas_uva == 0:
                            print("No tienes semillas de uva")
                        else:
                            Sembrar("Semilla_Uva", "Semilla de Uva", 3)
                    elif opcion_siembra == 4:
                        calendario.avanzar_tiempo(10)
                        calendario.mostrar_fecha_hora()
                        if inventario.semillas_pimiento == 0:
                            print("No tienes semillas de pimiento")
                        else:
                            Sembrar("Semilla_Pimiento", "Semilla de pimiento", 4)
                    elif opcion_siembra == 5:
                        calendario.avanzar_tiempo(10)
                        calendario.mostrar_fecha_hora()
                        if inventario.semmillas_tomate == 0:
                            print("No tienes semillas de tomate")
                        else:
                            Sembrar("Semilla_Tomate", "Semilla de Tomate", 5)"""
            elif opcion_cosechas == 2:
                Actualizar()
                calendario.avanzar_tiempo(60)
                calendario.mostrar_fecha_hora()
                decision = "S"
                while decision == "S" or decision == "s":
                    for i in range(0 , len(listaSuelos)):
                        print("Suelo: ", listaSuelos[i].Get_Numero() ," , ", listaSuelos[i].semilla)
                    opcion_suelo = int(input("Ingrese el numero del suelo que desea regar: "))
                    if listaSuelos[opcion_suelo].tiene_semilla == False:
                        print("No hay semillas en este suelo")
                    else:
                        listaSemillas[listaSuelos[opcion_suelo].numero_semilla].tiene_agua = True
                        listaSemillas[listaSuelos[opcion_suelo].numero_semilla].Mostrar_Datos()
                        listaSemillas[listaSuelos[opcion_suelo].numero_semilla].hora_semilla = calendario.hora
                        listaSuelos[opcion_suelo].hora_semilla = calendario.hora
                        listaSuelos[opcion_suelo].tiene_agua = True
                        decision = input("¿Desea regar otra semilla? (S/N): ")




            elif opcion_cosechas == 4:
                Actualizar()
                calendario.avanzar_tiempo(60)
                calendario.mostrar_fecha_hora()
                print("Bienvenido al inventario")
                inventario.Mostrar_Semillas()
            elif opcion_cosechas == 5:
                Actualizar()
                calendario.avanzar_tiempo(60)
                calendario.mostrar_fecha_hora()

    elif opcion == 2:
        Actualizar()
        calendario.avanzar_tiempo(60)
        calendario.mostrar_fecha_hora()
        print("Bienvenido al espacio de cuidado de animales")
    elif opcion==3:
        Actualizar()
        calendario.avanzar_tiempo(60)
        calendario.mostrar_fecha_hora()
        print("Bienvenido al espacio de economía y comercio")
    elif opcion == 4:
        Actualizar()
        calendario.avanzar_tiempo(60)
        calendario.mostrar_fecha_hora()
        print("Bienvenido al inventario")
        inventario.Mostrar_Semillas()
    elif opcion == 5:
        Actualizar()
        calendario.avanzar_tiempo(60)
        calendario.mostrar_fecha_hora()



