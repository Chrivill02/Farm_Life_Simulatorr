#Espacio para Angie(Calendario y Planificación)







#Espacio para Rodrigo (Economía y mercado)







#Espacio para Karen(Animales)
class Animal:
    def __init__(self):
        self.salud=100
        self.hambre=0
        self.felicidad=100
        self.cantidad_animales=2
        self.enfermo=False

    def MostrarDatos(self):
        print(f'Datos:\nSalud: {self.salud}\nHambre: {self.hambre}\nFelicidad: {self.felicidad}\nRecursos: {self.produccion}\nCantidad de animales: {cantidad_animales}')
    def AlimentarAnimal(self, cantidad):
        self.hambre -= cantidad
        self.felicidad += cantidad

    def Acariciar(self):
        self.felicidad +=10

    def Limpiar(self):
        self.salud +=10

    def Enfermar(self):
        self.salud-=20

    def Curar(self):
        self.salud +=30

class Oveja(Animal):
        def __init__(self, salud, hambre, felicidad):
            super().__init__(salud, hambre, felicidad)
            self.tipo = "oveja"
            self.lana=0

        def ProducirLana(self):
            self.lana +=15
        def VenderLana(self):
            self.lana -=15

        def AgregarOveja(self, cantidad):
            self.cantidad_animales+=cantidad

        def EliminarOveja(self, cantidad):
            self.cantidad_animales -= cantidad

        def MostrarCantidadVaca(self):
            return self.cantidad_animales

        def MostrarProduccion(self):
            print(f'La producción de LANA es de: {self.lana}')
class Gallina(Animal):
        def __init__(self, salud, hambre, felicidad):
            super().__init__(salud, hambre, felicidad)
            self.tipo = "gallina"
            self.huevos=0

        def ProducirHuevos(self):
            self.huevos+=5

        def VenderHuevos(self):
            self.huevos-=5

        def AgregarGallina(self, cantidad):
            self.cantidad_animales+=cantidad

        def EliminarGallina(self, cantidad):
            self.cantidad_animales-=cantidad

        def MostrarCantidadGallina(self):
            return self.cantidad_animales
        def MostrarProduccion(self):
            print(f'La producción de HUEVOS es de: {self.huevos}')
class Vaca(Animal):
        def __init__(self, salud, hambre, felicidad):
            super().__init__(salud, hambre, felicidad)
            self.tipo = "vaca"
            self.leche=0

        def ProducirLeche(self):
            self.leche += 15

        def VenderLeche(self):
            self.leche -=15

        def AgregarVaca(self, cantidad):
            self.cantidad_animales+=cantidad

        def EliminarVaca(self, cantidad):
            self.cantidad_animales -= cantidad

        def MostrarCantidadVaca(self):
            return self.cantidad_animales
        def MostrarProduccion(self):
            print(f'La producción de LECHE es de: {self.leche}')


class Enfermedades:
    def __init__(self, ListaEnfermos):
        self.ListaEnfermos=ListaEnfermos

class Granja(Oveja, Gallina, Vaca):
    def __init__(self, tipo, salud, hambre, felicidad):
        Oveja.__init__(self, tipo, salud, hambre, felicidad)
        Gallina.__init__(self, tipo, salud, hambre, felicidad)
        Vaca.__init__(self, tipo, salud, hambre, felicidad)

    def Mostrar_Granja_Animales(self):
        print(f'ANIMALES:\nVacas: {Vaca.MostrarCantidadVaca()}\nGallinas: {Gallina.MostrarCantidadGallina()}\nOvejas: {Oveja.MostrarCantidadOveja()}')
        print(f'RECURSOS:\nLeche: {self.leche}\nHuevos: {self.huevos}\nLana: {self.lana}')





while opcion != 0:
    print("Bienvenido a Farm Simulator! ")
    print("Selecciona el número de la opción que deseas: ")
    print("1. Cultivos y cosechas")
    print("2. Cuidado de animales")
    print("3. Economía y comercio")
    print("4. Ver inventario")
    print("0. Salir")
    opcion = int(input())

    if opcion == 1:
        Actualizar()
        calendario.avanzar_tiempo(60)
        calendario.mostrar_fecha_hora()
        Animal.MostrarDatos()
        print("Seleccione el número de la opción que desea consultar")
        print("1. ")







