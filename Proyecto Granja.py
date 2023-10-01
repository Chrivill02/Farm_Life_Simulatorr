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
        if comida_a_utilizar==1:
            print(f"Acabas de utilizar {comida_a_utilizar} porción de comida para alimentar a tus animales")
        elif comida_a_utilizar==0:
            print("No cuentas con porciones de comida disponibles para alimentar a tus animales")
        else:
            print(f"Acabas de utilizar {comida_a_utilizar} porciones de comida para alimentar a tus animales")

    def Acariciar(self):
        self.felicidad +=10
        print("Animal acariciado exitosamente")

    def Limpiar(self):
        self.salud +=10
        print("Animal limpiado exitosamente")

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
        if cantidad==1:
            print(f'Se ha agregado {cantidad} porción de comida para tus animales')
        else:
            print(f'Se han agregado {cantidad} porciones de comida para tus animales')


class Oveja(Animal):
        def __init__(self):
            super().__init__()
            self.tipo = "oveja"
            self.lana=0

        def ProducirLana(self):
            self.lana +=5
            print("Ahora tienes 5 kilogramos de lana más")
        def VenderLana(self):
            if self.lana==0:
                print("No tienes lana disponible para vender")
            elif self.lana>0 and self.lana<5:
                print(f'No tienes suficiente lana para poder venderla')
            elif self.lana>4:
                self.lana -=5
                print("Vendiste 5 kilogramos de lana")

        def AgregarOveja(self, cantidad):
            self.cantidad_animales += cantidad
            if cantidad==1:
                print(f'Se ha agregado una oveja a tu granja')
            elif cantidad==0 or cantidad<0:
                print("No se ha agregado ninguna oveja a tu granja")
            else:
                print(f"Acabas de agregar {cantidad} ovejas a tu granja")

        def EliminarOveja(self, cantidad):
            if self.cantidad_animales==0 or cantidad>self.cantidad_animales:
                self.cantidad_animales=0
                print(f"No tienes ovejas disponibles")
            else:
                self.cantidad_animales -= cantidad
                print(f"Acabas de eliminar {cantidad} ovejas de tu granja")

        def MostrarCantidadAnimal(self):
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
            if self.huevos == 0:
                print("No tienes huevos disponibles para vender")
            elif self.huevos > 0 and self.huevos < 3:
                print(f'No tienes suficientes huevos para poder venderlos')
            elif self.huevos > 2:
                self.huevos -= 3
                print("Vendiste 3 huevos")

        def AgregarGallina(self, cantidad):
            self.cantidad_animales += cantidad
            if cantidad==1:
                print(f'Se ha agregado una gallina a tu granja')
            elif cantidad==0 or cantidad<0:
                print("No se ha agregado ninguna gallina a tu granja")
            else:
                print(f"Acabas de agregar {cantidad} gallinas a tu granja")

        def EliminarGallina(self, cantidad):
            if self.cantidad_animales == 0 or cantidad > self.cantidad_animales:
                self.cantidad_animales = 0
                print(f"No tienes gallinas disponibles")
            else:
                self.cantidad_animales -= cantidad
                print(f"Acabas de eliminar {cantidad} gallinas de tu granja")

        def MostrarCantidadAnimal(self):
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
            if self.leche == 0:
                print("No tienes leche disponible para vender")
            elif self.leche > 0 and self.leche < 15:
                print(f'No tienes suficiente leche para poder venderla')
            elif self.leche > 14:
                self.leche -= 15
                print("Vendiste 15 litros de leche")

        def AgregarVaca(self, cantidad):
            self.cantidad_animales += cantidad
            if cantidad == 1:
                print(f'Se ha agregado una vaca a tu granja')
            elif cantidad == 0 or cantidad < 0:
                print("No se ha agregado ninguna vaca a tu granja")
            else:
                print(f"Acabas de agregar {cantidad} vacas a tu granja")

        def EliminarVaca(self, cantidad):
            if self.cantidad_animales == 0 or cantidad > self.cantidad_animales:
                self.cantidad_animales = 0
                print(f"No tienes vacas disponibles")
            else:
                self.cantidad_animales -= cantidad
                print(f"Acabas de eliminar {cantidad} vacas de tu granja")

        def MostrarCantidadAnimal(self):
            print(f'Ahora tienes un total de {self.cantidad_animales} vacas en tu granaja')

        def MostrarProduccion(self):
            print(f'La producción actual disponible de LECHE es de: {self.leche}')





class Granja(Oveja, Gallina, Vaca):
    def __init__(self):
        super().__init__()
        self.animales=[] #Lista para mantener un registro de los animales

    def AgregarAnimal(self, animal):
        self.animales.append(animal)
        print("Animal agregado exitosamente")
    def Mostrar_Granja_Animales(self):
        print("ANIMALES")
        for animal in (self.animales):
            animal.MostrarCantidadAnimal()
            animal.MostrarProduccion()



Mi_granja= Granja()

Mi_Oveja = Oveja()
Mi_Vaca= Vaca()
Mi_Gallina= Gallina()


    elif opcion == 2:
        Actualizar()
        calendario.avanzar_tiempo(60)
        calendario.mostrar_fecha_hora()

        opcion_animales = int(input()) #opción para elegir la acción (alimentar, acariciar, limpiar, etc.)
        while opcion_animales != 0:
            Actualizar()
            calendario.avanzar_tiempo(60)
            calendario.mostrar_fecha_hora()
            print("¡Bienvenido al espacio de Cuidado de animales! ¿Que deseas hacer?")
            print("1. Alimentar")
            print("2. Acariciar")
            print("3. Limpiar")
            print("4. Ver animales enfermos")
            print("5. Curar")
            print("6. Ver inventario de animales")
            print("7. Agregar animal a mi granja")
            print("0. Salir")
            if opcion_animales == 1:
                Actualizar()
                calendario.avanzar_tiempo(60)
                calendario.mostrar_fecha_hora()
                opcion_alimentar=1 #opción para elegir que animal alimentar
                print("¿Que animal deseas alimentar? ")
                print("1.Ovejas\n2.Vacas\n3.Gallinas")
                if opcion_alimentar==1:
                    Mi_Oveja.AlimentarAnimal(1)

                elif opcion_alimentar == 2:
                    Mi_Vaca.AlimentarAnimal(1)

                elif opcion_alimentar == 3:
                    Mi_Gallina.AlimentarAnimal(1)

            elif opcion_animales == 2:
                Actualizar()
                calendario.avanzar_tiempo(60)
                calendario.mostrar_fecha_hora()
                opcion_acariciar=int(input()) #opcion para elegir que animal acariciar
                print("¿Que animal deseas acariciar? ")
                print("1.Ovejas\n2.Vacas\n3.Gallinas")
                if opcion_acariciar==1:
                    Mi_Oveja.Acariciar()
                elif opcion_acariciar==2:
                    Mi_Vaca.Acariciar()
                elif opcion_acariciar==3:
                    Mi_Gallina.Acariciar()

            elif opcion_animales==3:
                Actualizar()
                calendario.avanzar_tiempo(60)
                calendario.mostrar_fecha_hora()
                opcion_limpiar = int(input()) #opcion para elegir que animal limpiar
                print("¿Que animal deseas limpiar? ")
                print("1.Ovejas\n2.Vacas\n3.Gallinas")
                if opcion_limpiar==1:
                    Mi_Oveja.Limpiar()

                elif opcion_limpiar==2:
                    Mi_Vaca.Limpiar()

                elif opcion_limpiar==3:
                    Mi_Gallina.Limpiar()


            elif opcion_animales==4:
                Actualizar()
                calendario.avanzar_tiempo(60)
                calendario.mostrar_fecha_hora()
                opcion_enfermar=int(input()) #opcion para elegir ver que tipo de animal está enfermo
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
                Actualizar()
                calendario.avanzar_tiempo(60)
                calendario.mostrar_fecha_hora()
                opcion_curar= int(input()) #opcion para elegir que animal curar
                print("¿Que animal deseas curar? ")
                print("1.Ovejas\n2.Vacas\n3.Gallinas")
                if opcion_curar==1:
                    Mi_Oveja.Curar()
                elif opcion_curar==2:
                    Mi_Vaca.Curar()
                elif opcion_curar==3:
                    Mi_Gallina.Curar()

            elif opcion_animales==6:
                Actualizar()
                calendario.avanzar_tiempo(60)
                calendario.mostrar_fecha_hora()
                Mi_granja.Mostrar_Granja_Animales()

            elif opcion_animales==7:
                Actualizar()
                calendario.avanzar_tiempo(60)
                calendario.mostrar_fecha_hora()
                print("¿Que animal deseas curar? ")
                print("1.Ovejas\n2.Vacas\n3.Gallinas")
                opcion_agregar = int(input())  # opcion para elegir que animal agregar
                if opcion_agregar == 1:
                    Mi_granja.AgregarAnimal(Mi_Oveja)
                elif opcion_agregar == 2:
                    Mi_granja.AgregarAnimal(Mi_Vaca)
                elif opcion_agregar == 3:
                    Mi_granja.AgregarAnimal(Mi_Gallina)














