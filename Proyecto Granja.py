import os

def clear():
    os.system('cls')

def pause():
    os.system('pause')

# Espacio para Angie(Calendario y Planificación)


# Espacio para Rodrigo (Economía y mercado)
class Jugador:
    def _init_(self, nombre):
        self.nombre = nombre
        self.dinero = 200
        self.productos = {"Manzana": 0, "Pera": 0, "Uva": 0, "Pimiento": 0, "Tomate": 0,"Semilla de Manzanas": 0,
                        "Semilla de Pera": 0, "Semilla de Uva": 0, "Semilla de Pimiento": 0, "Semilla de Tomate": 0,
                        "Fertilizante": 0, "Insecticida": 0, "Medicamento": 0}
    def agregar_dinero(self, cantidad):
        self.dinero += cantidad

    def comprar(self, nombre_producto, cantidad):
        if self.dinero >= nombre_producto.precio * cantidad and nombre_producto.cantidad >= cantidad:
            self.dinero -= nombre_producto.precio * cantidad
            nombre_producto.cantidad -= cantidad
            if nombre_producto.nombre in self.productos:
                self.productos[nombre_producto.nombre] += cantidad
            else:
                self.productos[nombre_producto.nombre] = cantidad

            print("Ha comprado:", cantidad, "de", nombre_producto.nombre)
            return True
        else:
            print("No tiene dinero suficiente o no hay suficiente stock para comprar", cantidad, "de", nombre_producto.nombre)
            return False

    def vender(self, producto, cantidad):
        if producto.nombre in self.productos:
            if self.productos[producto.nombre] >= cantidad:
                self.dinero += producto.precio * cantidad
                self.productos[producto.nombre] -= cantidad
                print("Ha vendido:", cantidad, "de", producto.nombre)
                return True
            else:
                print("No tiene suficientes", producto.nombre, "para vender")
                return False
        else:
            print("No tiene", producto.nombre, "para vender")
            return False


class Producto:
    def _init_(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def _str_(self):
        return f"{self.nombre}: {self.cantidad}"


# EJEMPLO





Jugador1 = Jugador("Rodrigo")
Manzanas = Producto("Manzana", 15, 5)
Pera = Producto("Pera", 10, 5)
Uva = Producto("Uva", 20, 5)
Pimiento = Producto("Pimiento", 5, 5)
Tomate = Producto("Tomate", 5, 5)

Semilla_Manzanas = Producto("Semilla de Manzanas", 15, 5)
Semilla_Pera = Producto("Semilla de Pera", 10, 5)
Semilla_Uva = Producto("Semilla de Uva", 20, 5)
Semilla_Pimiento = Producto("Semilla de Pimiento", 5, 5)
Semilla_Tomate = Producto("Semilla de Tomate", 5, 5)

Fertilizante = Producto("Fertilizante", 5, 5)
Insecticida = Producto("Insecticida", 5, 5)
Medicamento = Producto("Medicamento", 5, 5)


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
    print("6. Mercado")
    print("0. Salir")
    opcion = int(input(""))




    elif opcion == 6:
        clear()
        print(f"Bienvenido al mercado {Jugador1.nombre}")
        print("Productos: ")
        i=0
        for nombre_producto, cantidad in Jugador1.productos.items():
            i += 1
            print(f"{i}. {nombre_producto}: {cantidad}")
        print(f"Dinero= ${Jugador1.dinero}")
        print("1. Comprar")
        print("2. Vender")
        opcion = int(input("Que desea hacer?"))
        if opcion == 1:
            clear()
            print("-----Comprar--------")
            print("1. Semillas")
            print("2. Frutas")
            print("3. Mejoras")
            print("4. Regresar al Menú")
            opcion = int(input("Que desea comprar?"))
            if opcion == 1:
                clear()
                print("-----Semillas--------")
                print("1. Semillas de Manzanas")
                print("2. Semillas de Pera")
                print("3. Semillas de Uva")
                print("4. Semillas de Pimiento")
                print("5. Semillas de Tomate")
                print("6. Regresar al Menú")
                opcion = int(input("Que desea comprar?"))
                if opcion == 1:
                    print(f"Semillas de Manzanas: Precio:{Semilla_Manzanas.precio}  Stock: {Semilla_Manzanas.cantidad}")
                    cantidad = int(input("Ingrese cuantas semillas de manzana quiere comprar: "))
                    Jugador1.comprar(Semilla_Manzanas, cantidad)
                    print(f"Jugador: {Jugador1.nombre}   Productos: {Jugador1.productos}  Dinero Restante: {Jugador1.dinero}")
                    pause()
                elif opcion == 2:
                    print(f"Semillas de Pera: Precio:{Semilla_Pera.precio}  Stock: {Semilla_Pera.cantidad}")
                    cantidad = int(input("Ingrese cuantas semillas de pera quiere comprar: "))
                    Jugador1.comprar(Semilla_Pera, cantidad)
                    print(f"Jugador: {Jugador1.nombre}   Productos: {Jugador1.productos}  Dinero Restante: {Jugador1.dinero}")
                    pause()
                elif opcion == 3:
                    print(f"Semillas de Uva: Precio:{Semilla_Uva.precio}  Stock: {Semilla_Uva.cantidad}")
                    cantidad = int(input("Ingrese cuantas semillas de Uva quiere comprar: "))
                    Jugador1.comprar(Semilla_Uva, cantidad)
                    print(f"Jugador: {Jugador1.nombre}   Productos: {Jugador1.productos}  Dinero Restante: {Jugador1.dinero}")
                    pause()
                elif opcion == 4:
                    print(f"Semillas de Pimiento: Precio:{Semilla_Pimiento.precio}  Stock: {Semilla_Pimiento.cantidad}")
                    cantidad = int(input("Ingrese cuantos semillas de Pimiento quiere comprar: "))
                    Jugador1.comprar(Semilla_Pimiento, cantidad)
                    print(f"Jugador: {Jugador1.nombre}   Productos: {Jugador1.productos}  Dinero Restante: {Jugador1.dinero}")
                    pause()
                elif opcion == 5:
                    print(f"Semillas de Tomate: Precio:{Semilla_Tomate.precio}  Stock: {Semilla_Tomate.cantidad}")
                    cantidad = int(input("Ingrese cuantos semillas de Tomate quiere comprar: "))
                    Jugador1.comprar(Semilla_Tomate, cantidad)
                    print(f"Jugador: {Jugador1.nombre}   Productos: {Jugador1.productos}  Dinero Restante: {Jugador1.dinero}")
                    pause()
                elif opcion == 6:
                    pass
                else:
                    print("Opción no valida")
            elif opcion == 2:
                clear()
                print("-----Frutas--------")
                print("1. Manzanas")
                print("2. Pera")
                print("3. Uva")
                print("4. Pimiento")
                print("5. Tomate")
                print("6. Regresar al Menú")
                opcion = int(input("Que desea comprar?"))
                if opcion == 1:
                    print(f"Manzanas: Precio:{Manzanas.precio}  Stock: {Manzanas.cantidad}")
                    cantidad = int(input("Ingrese cuantas manzanas quiere comprar: "))
                    Jugador1.comprar(Manzanas, cantidad)
                    print(f"Jugador: {Jugador1.nombre}   Productos: {Jugador1.productos}  Dinero Restante: {Jugador1.dinero}")
                    pause()
                elif opcion == 2:
                    print(f"Pera: Precio:{Pera.precio}  Stock: {Pera.cantidad}")
                    cantidad = int(input("Ingrese cuantas peras quiere comprar: "))
                    Jugador1.comprar(Pera, cantidad)
                    print(f"Jugador: {Jugador1.nombre}   Productos: {Jugador1.productos}  Dinero Restante: {Jugador1.dinero}")
                    pause()
                elif opcion == 3:
                    print(f"Uva: Precio:{Uva.precio}  Stock: {Uva.cantidad}")
                    cantidad = int(input("Ingrese cuantas Uvas quiere comprar: "))
                    Jugador1.comprar(Uva, cantidad)
                    print(f"Jugador: {Jugador1.nombre}   Productos: {Jugador1.productos}  Dinero Restante: {Jugador1.dinero}")
                    pause()
                elif opcion == 4:
                    print(f"Pimiento: Precio:{Pimiento.precio}  Stock: {Pimiento.cantidad}")
                    cantidad = int(input("Ingrese cuantos Pimientos quiere comprar: "))
                    Jugador1.comprar(Pimiento, cantidad)
                    print(f"Jugador: {Jugador1.nombre}   Productos: {Jugador1.productos}  Dinero Restante: {Jugador1.dinero}")
                    pause()
                elif opcion == 5:
                    print(f"Tomate: Precio:{Tomate.precio}  Stock: {Tomate.cantidad}")
                    cantidad = int(input("Ingrese cuantos Tosmate quiere comprar: "))
                    Jugador1.comprar(Tomate, cantidad)
                    print(f"Jugador: {Jugador1.nombre}   Productos: {Jugador1.productos}  Dinero Restante: {Jugador1.dinero}")
                    pause()
                elif opcion == 6:
                    pass
                else:
                    print("Opción no valida")
            elif opcion == 3:
                clear()
                print("------Mejoras-------")
                print("1. Fertilizante")
                print("2. Medicamentos")
                print("3. Insecticida")
                print("4. Terreno")
                print("5. Regresar al Menú")
                opcion = int(input("Que desea comprar?"))
                if opcion == 1:
                    print(f"Fertilizante: Precio:{Fertilizante.precio}  Stock: {Fertilizante.cantidad}")
                    cantidad = int(input("Ingrese cuanto Fertilizante quiere comprar: "))
                    Jugador1.comprar(Fertilizante, cantidad)
                    print(f"Jugador: {Jugador1.nombre}   Productos: {Jugador1.productos}  Dinero Restante: {Jugador1.dinero}")
                    pause()
                elif opcion == 2:
                    print(f"Medicamentos: Precio:{Medicamento.precio}  Stock: {Medicamento.cantidad}")
                    cantidad = int(input("Ingrese cuanto Medicamento quiere comprar: "))
                    Jugador1.comprar(Medicamento, cantidad)
                    print(f"Jugador: {Jugador1.nombre}   Productos: {Jugador1.productos}  Dinero Restante: {Jugador1.dinero}")
                    pause()
                elif opcion == 3:
                    print(f"Insecticida: Precio:{Insecticida.precio}  Stock: {Insecticida.cantidad}")
                    cantidad = int(input("Ingrese cuanto Insecticida quiere comprar: "))
                    Jugador1.comprar(Insecticida, cantidad)
                    print(f"Jugador: {Jugador1.nombre}   Productos: {Jugador1.productos}  Dinero Restante: {Jugador1.dinero}")
                    pause()
                elif opcion == 4:
                    print(f"Terreno: Precio:{Terreno.precio}  Stock: {Terreno.cantidad}")
                    cantidad = int(input("Ingrese cuantos Terrenos quiere comprar: "))
                    Jugador1.comprar(Terreno, cantidad)
                    # Mejora de terreno aquis
                    print(f"Terreno Mejorado con éxito")
                    print(f"Jugador: {Jugador1.nombre} Dinero Restante: {Jugador1.dinero}")
                    pause()
                elif opcion == 5:
                    pass
                else:
                    continue

            elif opcion == 4:
                pass
            else:
                continue

        elif opcion == 2:
            print("---------Vender---------")
            i = 0
            for nombre_producto, precio in Jugador1.productos.items():
                i += 1
                print(f"{i}. {nombre_producto}: {precio}")
            opcion = int(input("Que desea vender?"))
            if opcion == 1:
                cantidad = int(input("Cuantas Manzanass quiere vender?"))
                Jugador1.vender(Manzanas, cantidad)
                print(f"Jugador: {Jugador1.nombre}   Productos: {Jugador1.productos}  Dinero Restante: {Jugador1.dinero}")
                pause()
            elif opcion == 2:
                cantidad = int(input("Cuantas Peras quiere vender?"))
                Jugador1.vender(Pera, cantidad)
                print(f"Jugador: {Jugador1.nombre}   Productos: {Jugador1.productos}  Dinero Restante: {Jugador1.dinero}")
                pause()
            elif opcion == 3:
                cantidad = int(input("Cuantas Uvas quiere vender?"))
                Jugador1.vender(Uva, cantidad)
                print(f"Jugador: {Jugador1.nombre}   Productos: {Jugador1.productos}  Dinero Restante: {Jugador1.dinero}")
                pause()
            elif opcion == 4:
                cantidad = int(input("Cuantas Pimientos quiere vender?"))
                Jugador1.vender(Pimiento, cantidad)
                print(f"Jugador: {Jugador1.nombre}   Productos: {Jugador1.productos}  Dinero Restante: {Jugador1.dinero}")
                pause()
            elif opcion == 5:
                cantidad = int(input("Cuantos Tomates quiere vender?"))
                Jugador1.vender(Tomate, cantidad)
                print(f"Jugador: {Jugador1.nombre}   Productos: {Jugador1.productos}  Dinero Restante: {Jugador1.dinero}")
                pause()
            else:
                continue