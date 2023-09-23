#Espacio para Angie(Calendario y Planificación)







#Espacio para Rodrigo (Economía y mercado)







#Espacio para Karen(Animales)







#Espacio para Chris (Cultivos)
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
    def __init__(self, es_brote, es_crecimiento, es_madura):
        self.nombre = ""
        self.precio = 0
        self.es_brote = es_brote
        self.es_crecimiento = es_crecimiento
        self.es_madura = es_madura


    def mostrar_datos(self):
        print("Nombre: ", self.nombre)
        print("Precio: ", self.precio)


class Semilla_Manzana(Semilla):
    def __init__(self,  es_brote, es_crecimiento, es_madura):
        super().__init__(  es_brote, es_crecimiento, es_madura)
        self.nombre = "Semilla de Manzana"
        self.precio = 10

    def mostrar_datos(self):
        print("Nombre: ", self.nombre)
        print("Precio: ", self.precio)

class Semilla_Pera(Semilla):
    def __init__(self,  es_brote, es_crecimiento, es_madura):
        super().__init__( es_brote, es_crecimiento, es_madura)
        self.nombre = "Semilla de Pera"
        self.precio = 8

    def mostrar_datos(self):
        print("Nombre: ", self.nombre)
        print("Precio: ", self.precio)

class Semilla_Tomate(Semilla):
    def __init__(self, es_brote, es_crecimiento, es_madura):
        super().__init__(  es_brote, es_crecimiento, es_madura)
        self.nombre = "Semilla de Tomate"
        self.precio = 5

    def mostrar_datos(self):
        print("Nombre: ", self.nombre)
        print("Precio: ", self.precio)

class Semilla_Pimiento(Semilla):
    def __init__(self,  es_brote, es_crecimiento, es_madura):
        super().__init__(  es_brote, es_crecimiento, es_madura)

        self.nombre = "Semilla de Pimiento"
        self.precio = 4
    def mostrar_datos(self):
        print("Nombre: ", self.nombre)
        print("Precio: ", self.precio)

class Semilla_Uva(Semilla):
    def __init__(self ,es_brote, es_crecimiento, es_madura):
        super().__init__(  es_brote, es_crecimiento, es_madura)
        self.nombre = "Semilla de Uva"
        self.precio = 10

    def mostrar_datos(self):
        print("Nombre: ", self.nombre)
        print("Precio: ", self.precio)
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
    def __init__(self, tiene_agua, tiene_fertilizante, tiene_plaga, tiene_semilla, _numero, semilla):
        self.tiene_agua = tiene_agua
        self.tiene_fertilizante = tiene_fertilizante
        self.tiene_plaga = tiene_plaga
        self.tiene_semilla = tiene_semilla
        self._numero = _numero
        self.semilla = semilla

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

    def Get_Numero(self):
        return self._numero
    def Agregar_Semilla(self, Nombre_de_semilla):
        self.semilla = Nombre_de_semilla

def Sembrar(Nombre_Semilla, Nombre_Informal_Semilla):
    print("¿En que suelo deseas sembrarlo? ")
    terreno.Verificar_Suelos_Disponibles()
    opcion_suelo = int(input("Ingrese el numero del suelo que deseas: "))
    listaSuelos[opcion_suelo].tiene_semilla = True
    listaSuelos[opcion_suelo].Agregar_Semilla(Nombre_Informal_Semilla)
    inventario.Eliminar_Semilla(Nombre_Semilla)
    terreno.Actualizar()

    print(Nombre_Semilla, " sembrada en suelo ", listaSuelos[opcion_suelo].Get_Numero())
    print(inventario.Mostrar_Semillas())

opcion = 1
listaSemillas = []
listaSuelos = []
listaSemillas.append(Semilla_Tomate(False, False, False))
listaSemillas.append(Semilla_Uva(False, False, False))
listaSemillas.append(Semilla_Pimiento(False, False, False))
listaSemillas.append(Semilla_Pera(False, False, False))
listaSemillas.append(Semilla_Manzana(False, False, False))
inventario = Inventario(1,1,1,1,1)
listaSuelos.append(Suelo(False, False, False, False, 0, "No tiene semilla"))
listaSuelos.append(Suelo(False, False, False, False, 1, "No tiene semilla"))
listaSuelos.append(Suelo(False, False, False, False, 2 , "No tiene semilla"))
listaSuelos.append(Suelo(False, False, False, False, 3, "No tiene semilla"))
listaSuelos.append(Suelo(False, False, False, False, 4, "No tiene semilla"))
terreno = Terreno(5, 1, 1000)
while opcion != 0:
    print("Bienvenido a Farm Simulator! ")
    print("Selecciona la opción que deseas: ")
    print("1. Cultivos y cosechas")
    print("2. Cuidado de animales")
    print("3. Economía y comercio")
    print("4. Ver inventario")
    print("0. Salir")
    opcion = int(input(""))
    if opcion == 1:
        opcion_cosechas = 1
        while opcion_cosechas != 0:
            print("Bienvenido al espacio de cultivos y cosechas! ¿Que deseas hacer?")
            print("1. Sembrar")
            print("2. Regar")
            print("3. Cosechar")
            print("4. Ver inventario")
            print("0. Salir")
            opcion_cosechas = int(input(""))
            if opcion_cosechas == 1:
                opcion_siembra = 1
                while opcion_siembra != 0:
                    if terreno.espacio_siembra == 0:
                        print("Ya no tienes más espacios para sembrar")
                        print("Cultiva o mejora el terreno para sembrar más")
                    else:
                        print("Tienes: ", terreno.espacio_siembra, " espacios para sembrar.")
                        print("¿Que deseas sembrar? ")
                        print("1. Semillas de Manzana")
                        print("2. Semillas de Pera")
                        print("3. Semillas de Uva")
                        print("4. Semillas de Pimiento")
                        print("5. Semillas de Tomate")
                        print("0. Salir")
                        opcion_siembra = int(input(""))
                        if opcion_siembra == 1:
                            if inventario.semillas_manzana == 0:
                                print("No tienes semillas de manzana")
                            else:
                                Sembrar("Semilla_Manzana", "Semilla de Manzana")
                        elif opcion_siembra == 2:
                            if inventario.semillas_pera == 0:
                                print("No tienes semillas de pera")
                            else:
                                Sembrar("Semilla_Pera", "Semilla de Pera")
                        elif opcion_siembra == 3:
                            if inventario.semillas_uva == 0:
                                print("No tienes semillas de uva")
                            else:
                                Sembrar("Semilla_Uva", "Semilla de Uva")
                        elif opcion_siembra == 4:
                            if inventario.semillas_pimiento == 0:
                                print("No tienes semillas de pimiento")
                            else:
                                Sembrar("Semilla_Pimiento", "Semilla de pimiento")
                        elif opcion_siembra == 5:
                            if inventario.semmillas_tomate == 0:
                                print("No tienes semillas de tomate")
                            else:
                                Sembrar("Semilla_Tomate", "Semilla de Tomate")
            elif opcion_cosechas == 2:
                
                decision = "S"
                while decision == "S" or decision == "s":
                    for i in range(0 , len(listaSuelos)):
                        print("Suelo: ", listaSuelos[i].Get_Numero() ," , ", listaSuelos[i].semilla)
                    opcion_suelo = int(input("Ingrese el numero del suelo que desea regar: "))
                    listaSuelos[opcion_suelo].tiene_agua = True
                    decision = input("¿Desea regar otra semilla? (S/N): ")



            elif opcion_cosechas == 4:
                print("Bienvenido al inventario")
                inventario.Mostrar_Semillas()


    elif opcion == 2:
        print("Bienvenido al espacio de cuidado de animales")
    elif opcion==3:
        print("Bienvenido al espacio de economía y comercio")
    elif opcion == 4:
        print("Bienvenido al inventario")
        inventario.Mostrar_Semillas()



