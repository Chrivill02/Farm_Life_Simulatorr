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


opcion = 1
listaSemillas = []

listaSemillas.append(Semilla_Tomate(False, False, False))
listaSemillas.append(Semilla_Uva(False, False, False))
listaSemillas.append(Semilla_Pimiento(False, False, False))
listaSemillas.append(Semilla_Pera(False, False, False))
listaSemillas.append(Semilla_Manzana(False, False, False))
inventario = Inventario(1,1,1,1,1)

while opcion != 0:
    print("Bienvenido a Farm Simulator, presione cualquier tecla y enter para continuar: ")
    terreno = Terreno(5, 1, 1000)
    input()
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
                    print("Tienes: ", terreno.espacio_siembra, " espacios para sembrar.")
                    print("¿Que deseas sembrar? ")
                    print("1. Semillas de Manzana")
                    print("2. Semillas de Pera")
                    print("3. Semillas de Uva")
                    print("4. Semillas de Pimiento")
                    print("5. Semillas de Tomate")




    elif opcion == 2:
        print("Bienvenido al espacio de cuidado de animales")
    elif opcion==3:
        print("Bienvenido al espacio de economía y comercio")
    elif opcion == 4:
        print("Bienvenido al inventario")


