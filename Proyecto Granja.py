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
    def AlimentarAnimal(self, comida_en_uso):
        self.hambre -= comida_en_uso
        self.felicidad += comida_en_uso
        self.comida_disponible -= comida_en_uso

    def Acariciar(self):
        self.felicidad +=10

    def Limpiar(self):
        self.salud +=10

    def Enfermar(self):
        if self.enfermo==True:
            self.salud -= 20*self.cantidad_enfermos

    def Curar(self):
        self.salud +=30

    def AgregarComida(self, cantidad):
        self.comida_disponible += cantidad

class Oveja(Animal):
        def __init__(self):
            super().__init__()
            self.tipo = "oveja"
            self.lana=0

        def ProducirLana(self):
            self.lana +=15
        def VenderLana(self):
            self.lana -=15

        def AgregarOveja(self, cantidad):
            self.cantidad_animales += cantidad

        def EliminarOveja(self, cantidad):
            self.cantidad_animales -= cantidad

        def MostrarCantidadOveja(self):
            print(self.cantidad_animales)

        def MostrarProduccion(self):
            print(f'La producción actual disponible de LANA es de: {self.lana}')
class Gallina(Animal):
        def __init__(self):
            super().__init__()
            self.tipo = "gallina"
            self.huevos=0

        def ProducirHuevos(self):
            self.huevos+=3

        def VenderHuevos(self):
            self.huevos -= 3

        def AgregarGallina(self, cantidad):
            self.cantidad_animales += cantidad

        def EliminarGallina(self, cantidad):
            self.cantidad_animales -= cantidad

        def MostrarCantidadGallina(self):
            print(self.cantidad_animales)
        def MostrarProduccion(self):
            print(f'La producción actual disponible de HUEVOS es de: {self.huevos}')
class Vaca(Animal):
        def __init__(self):
            super().__init__()
            self.tipo = "vaca"
            self.leche = 0

        def ProducirLeche(self):
            self.leche += 15

        def VenderLeche(self):
            self.leche -=15

        def AgregarVaca(self, cantidad):
            self.cantidad_animales += cantidad

        def EliminarVaca(self, cantidad):
            self.cantidad_animales -= cantidad

        def MostrarCantidadVaca(self):
            print(self.cantidad_animales)
        def MostrarProduccion(self):
            print(f'La producción actual disponible de LECHE es de: {self.leche}')


class Enfermos:
    def __init__(self):
        ListaEnfermos=[]
        self.ListaEnfermos = ListaEnfermos.append(Animal.Enfermar())

class Granja(Oveja, Gallina, Vaca):
    def __init__(self):
        Oveja.__init__(self)
        Gallina.__init__(self)
        Vaca.__init__(self)

    def Mostrar_Granja_Animales(self):
        print(f'ANIMALES:\nVacas: {Vaca.MostrarCantidadVaca()}\nGallinas: {Gallina.MostrarCantidadGallina()}\nOvejas: {Oveja.MostrarCantidadOveja()}')
        print(f'RECURSOS:\nLeche: {self.leche}\nHuevos: {self.huevos}\nLana: {self.lana}')


Mi_oveja = Oveja()
Mi_Vaca= Vaca()
Mi_Gallina= Gallina()

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
    if opcion == 2:
        Actualizar()
        calendario.avanzar_tiempo(60)
        calendario.mostrar_fecha_hora()

        opcion_animales = 1
        while opcion_animales != 0:
            print("¡Bienvenido al espacio de Cuidado de animales! ¿Que deseas hacer?")
            print("1. Alimentar")
            print("2. Acariciar")
            print("3. Limpiar")
            print("4. Enfermar")
            print("5. Curar")
            print("6. Ver inventario")
            print("7. Ver Hora")
            print("0. Salir")
            opcion_animales = int(input(""))
            if opcion_animales == 1:
                Actualizar()
                calendario.avanzar_tiempo(60)
                calendario.mostrar_fecha_hora()
                opcion_alimentar == 1

                if  Mi_animal.comida== 0:
                    print("Ya no tienes más comida para alimentar a los animales")
                    print("Consigue más comida para los animales")
                else:
                    print(f'Tienes {Mi_animal.comida} porciones de comida')
                    print("¿Que animal deseas alimentar? ")

                    for i in range(0,Mi_animal.cantidad_animales):
                        print(i, ". ", Mi_animal[i].nombre_informal)
                    opcion_siembra = int(input(""))
                    if listaSemillas[opcion_siembra].nombre_informal== "":
                        print("No hay semillas aqui ")
                    else:
                        Sembrar(listaSemillas[opcion_siembra].nombre_backend,
                                listaSemillas[opcion_siembra].nombre_informal
                                , opcion_siembra, listaSemillas[opcion_siembra].nombre_madura)

            elif opcion_cosechas == 2:
                Actualizar()
                calendario.avanzar_tiempo(60)
                calendario.mostrar_fecha_hora()
                decision = "S"
                while decision == "S" or decision == "s":
                    for i in range(0 , len(listaSuelos)):
                        print("Suelo: ", listaSuelos[i].Get_Numero() ," , ", listaSuelos[i].semilla)
                    opcion_suelo = int(input("Ingrese el numero del suelo que desea regar: "))
                    calendario.avanzar_tiempo(60)
                    calendario.mostrar_fecha_hora()
                    if listaSuelos[opcion_suelo].tiene_semilla == False:
                        print("No hay semillas en este suelo")
                        decision = input("¿Desea regar otra semilla? (S/N): ")
                    else:
                        listaSemillas[listaSuelos[opcion_suelo].numero_semilla].tiene_agua = True
                        listaSemillas[listaSuelos[opcion_suelo].numero_semilla].Mostrar_Datos()
                        listaSemillas[listaSuelos[opcion_suelo].numero_semilla].dia_semilla = calendario.dia
                        listaSuelos[opcion_suelo].dia_semilla = calendario.dia
                        listaSuelos[opcion_suelo].tiene_agua = True
                        decision = input("¿Desea regar otra semilla? (S/N): ")

            elif opcion_cosechas == 3:
                for i in range(0 , len(listaSuelos)):
                    print("Suelo: ", listaSuelos[i].Get_Numero() ," , ", listaSuelos[i].hortaliza)
                    if listaSuelos[i].tiene_semilla == True:
                        if listaSemillas[listaSuelos[i].numero_semilla].es_madura == True:
                            print("Madura")
                        else:
                            print("No madura")
                    else:
                        print("No hay semilla")
                Cosechar()





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










