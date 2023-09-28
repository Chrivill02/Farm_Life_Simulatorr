#Espacio para Angie(Calendario y Planificación)







#Espacio para Rodrigo (Economía y mercado)







#Espacio para Karen(Animales)
class Animal:
    def __init__(self, tipo):
        self.tipo=tipo
        self.salud=100
        self.hambre=0
        self.felicidad=100
        self.produccion=0

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

    def Producir(self):
        recursos={}
        if self.tipo=="vaca":
            recursos["leche"]= 5
        elif self.tipo=="lana":
            recursos["lana"] = 5
        elif self.tipo=="gallina":
            recursos["pollo"]=5
        return recursos



class Oveja(Animal):
    def __init__(self, tipo, salud, hambre, felicidad, produccion, ):
        super().__init__(tipo,salud, hambre, felicidad, produccion)
        sel

class Jugador:
    def __init__(self, nombre, granja):
        self.nombre=nombre
        self.granja=granja

class Granja:
    def __init__(self, animales, recursos, enfermeria):
        self.animales=animales
        self.recursos=recursos
        self.enfermeria=enfermeria

class Recursos:
    def __init__(self, leche, huevos, lana, alimentacion_animales):
        self.leche=leche
        self.huevos=huevos
        self.lana=lana
        self.alimentacion_animales=alimentacion_animales

class Enfermedades:
    def __init__(self, ListaEnfermos):
        self.ListaEnfermos=ListaEnfermos






#Espacio para Chris (Cultivos)