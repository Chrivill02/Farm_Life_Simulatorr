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
        self.cantidad_enfermos=0
        self.comida_disponible=5

    def MostrarDatos(self):
        print(f'Datos:\nSalud: {self.salud}\nHambre: '
              f'{self.hambre}\nFelicidad: {self.felicidad}\nRecursos: '
              f'{self.produccion}\nCantidad de animales: {self.cantidad_animales}\nCantidad de '
              f'animales enfermos: {self.cantidad_enfermos}')
    def AlimentarAnimal(self, comida_a_utilizar):
        self.hambre -= comida_a_utilizar
        self.felicidad += comida_a_utilizar
        self.comida_disponible -= comida_a_utilizar

    def Acariciar(self):
        self.felicidad +=10

    def Limpiar(self):
        self.salud +=10

    def Enfermar(self):
        if self.salud<7:
            self.enfermo=True
            self.cantidad_enfermos +=1
            print("Tienes un animal enfermo")

    def MostrarEnfermos(self):
        print(f'Tienes un total de {self.cantidad_enfermos} animales enfermos')
    def Curar(self):
        self.salud +=30
        print('Animal curado exitosamente')

    def AgregarComida(self, cantidad):
        self.comida_disponible += cantidad


class Oveja(Animal):
        def __init__(self):
            super().__init__()
            self.tipo = "oveja"
            self.lana=0

        def ProducirLana(self):
            self.lana +=15
            print("Ahora tienes 15 metros de lana más")
        def VenderLana(self):
            self.lana -=15
            print("Vendiste 15 metros de lana")

        def AgregarOveja(self, cantidad):
            self.cantidad_animales += cantidad
            print(f"Acabas de agregar {cantidad} ovejas a tu granja")

        def EliminarOveja(self, cantidad):
            self.cantidad_animales -= cantidad

        def MostrarCantidadOveja(self):
            print(f'Tienes un total de {self.cantidad_animales} ovejas')

        def MostrarProduccion(self):
            print(f'La producción actual disponible de LANA es de: {self.lana}')
class Gallina(Animal):
        def __init__(self):
            super().__init__()
            self.tipo = "gallina"
            self.huevos=0

        def ProducirHuevos(self):
            self.huevos+=3
            print("Ahora tienes 3 huevos más")

        def VenderHuevos(self):
            self.huevos -= 3
            print("Vendiste 3 huevos exitosamente")

        def AgregarGallina(self, cantidad):
            self.cantidad_animales += cantidad

        def EliminarGallina(self, cantidad):
            self.cantidad_animales -= cantidad

        def MostrarCantidadGallina(self):
            print(f'Ahora tienes un total de {self.cantidad_animales} gallinas')
        def MostrarProduccion(self):
            print(f'La producción actual disponible de HUEVOS es de: {self.huevos}')
class Vaca(Animal):
        def __init__(self):
            super().__init__()
            self.tipo = "vaca"
            self.leche = 0

        def ProducirLeche(self):
            self.leche += 15
            print("Ahora tienes 15litros de leche más")

        def VenderLeche(self):
            self.leche -=15
            print("Vendiste 15 litros de leche exitosamente")

        def AgregarVaca(self, cantidad):
            self.cantidad_animales += cantidad
            print(f"Agregaste {cantidad} vacas a tu granja")

        def EliminarVaca(self, cantidad):
            self.cantidad_animales -= cantidad

        def MostrarCantidadVaca(self):
            print(f'Ahora tienes un total de {self.cantidad_animales} vacas en tu granaja')
        def MostrarProduccion(self):
            print(f'La producción actual disponible de LECHE es de: {self.leche}')





class Granja(Oveja, Gallina, Vaca):
    def __init__(self):
        Oveja.__init__(self)
        Gallina.__init__(self)
        Vaca.__init__(self)

    def Mostrar_Granja_Animales(self):
        print(f'ANIMALES:\nVacas: {self.MostrarCantidadVaca()}\nGallinas: {self.MostrarCantidadGallina()}\nOvejas: {self.MostrarCantidadOveja()}')
        print(f'RECURSOS:\nLeche: {self.leche}\nHuevos: {self.huevos}\nLana: {self.lana}')

Mi_granja= Granja()

Mi_Oveja = Oveja()
Mi_Vaca= Vaca()
Mi_Gallina= Gallina()

opcion = int(input())
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

    if opcion == 2:
        Actualizar()
        calendario.avanzar_tiempo(60)
        calendario.mostrar_fecha_hora()

        opcion_animales = int(input()) #opción para elegir la acción (alimentar, acariciar, limpiar, etc.)
        while opcion_animales != 0:
            print("¡Bienvenido al espacio de Cuidado de animales! ¿Que deseas hacer?")
            print("1. Alimentar")
            print("2. Acariciar")
            print("3. Limpiar")
            print("4. Ver animales enfermos")
            print("5. Curar")
            print("6. Ver inventario de animales")
            print("0. Salir")
            if opcion_animales == 1:
                Actualizar()
                calendario.avanzar_tiempo(60)
                calendario.mostrar_fecha_hora()
                opcion_alimentar=1 #opción para elegir que animal alimentar
                print("¿Que animal deseas alimentar? ")
                print("1.Ovejas\n2.Vacas\n3.Gallinas")
                if opcion_alimentar==1 and Mi_Oveja.comida_disponible==0:
                    print("Ya no tienes más comida para alimentar a tus ovejas")
                    print("Consigue más comida para alimentarlas")
                elif opcion_alimentar==1 and Mi_Oveja.comida_disponible!=0:
                    Mi_Oveja.AlimentarAnimal(1)
                    print(f'Ya solo tienes {Mi_Oveja.comida_disponible} porciones de comida para oveja disponibles')
                elif opcion_alimentar== 2 and Mi_Vaca.comida_disponible==0:
                    print("Ya no tienes más comida para alimentar a tus vacas")
                    print("Consigue más comida para alimentarlas")
                elif opcion_alimentar == 2 and Mi_Vaca.comida_disponible != 0:
                    Mi_Vaca.AlimentarAnimal(1)
                    print(f'Ya solo tienes {Mi_Vaca.comida_disponible} porciones de comida para vaca disponibles')
                elif opcion_alimentar == 3 and Mi_Gallina.comida_disponible == 0:
                    print("Ya no tienes más comida para alimentar a tus Gallinas")
                    print("Consigue más comida para alimentarlas")
                elif opcion_alimentar == 3 and Mi_Gallina.comida_disponible != 0:
                    Mi_Gallina.AlimentarAnimal(1)
                    print(f'Ya solo tienes {Mi_Gallina.comida_disponible} porciones de comida para gallina disponibles')

            elif opcion_animales == 2:
                Actualizar()
                calendario.avanzar_tiempo(60)
                calendario.mostrar_fecha_hora()
                opcion_acariciar=int(input()) #opcion para elegir que animal acariciar
                print("¿Que animal deseas acariciar? ")
                print("1.Ovejas\n2.Vacas\n3.Gallinas")
                if opcion_acariciar==1:
                    Mi_Oveja.Acariciar()
                    print("Oveja acariciada exitosamente")
                elif opcion_acariciar==2:
                    Mi_Vaca.Acariciar()
                    print("Vaca acariciada exitosamente")
                elif opcion_acariciar==3:
                    Mi_Gallina.Acariciar()
                    print("Gallina acariciada exitosamente")

            elif opcion_animales==3:
                opcion_limpiar = int(input()) #opcion para elegir que animal limpiar
                print("¿Que animal deseas limpiar? ")
                print("1.Ovejas\n2.Vacas\n3.Gallinas")
                if opcion_limpiar==1:
                    Mi_Oveja.Limpiar()
                    print("Oveja limpiada exitosamente")
                elif opcion_limpiar==2:
                    Mi_Vaca.Limpiar()
                    print("Vaca limpiada exitosamente")
                elif opcion_limpiar==3:
                    Mi_Gallina.Limpiar()
                    print("Gallina limpiada exitosamente")

            elif opcion_animales==4:
                opcion_enfermar=int(input())
                print("¿Que animal deseas enfermar? ")
                print("1.Ovejas\n2.Vacas\n3.Gallinas")
                if opcion_enfermar==1:
                    Mi_Oveja.Enfermar()
                    Mi_Oveja.MostrarEnfermos()
                elif opcion ==2:
                    Mi_Vaca.Enfermar()
                    Mi_Vaca.MostrarEnfermos()
                elif opcion_enfermar==3:
                    Mi_Gallina.Enfermar()
                    Mi_Gallina.MostrarEnfermos()

            elif opcion_animales==5:
                opcion_curar= int(input())
                print("¿Que animal deseas curar? ")
                print("1.Ovejas\n2.Vacas\n3.Gallinas")
                if opcion_curar==1:
                    Mi_Oveja.Curar()
                elif opcion_curar==2:
                    Mi_Vaca.Curar()
                elif opcion_curar==3:
                    Mi_Gallina.Curar()

            elif opcion_animales==6:
                Mi_granja.Mostrar_Granja_Animales()










