from clases.basicos.ejercicio1 import Recta
from clases.basicos.ejercicio2 import Distancia
from clases.basicos.ejercicio3 import Funcion

class Basicos(object):
    def __init__(self):
        self.opcion = 0
        
    def mostrar_menu_basicos(self):
        print("\n-----------MENU BÁSICOS----------")
        print("1. Pendiente de una recta")
        print("2. Distancia entre dos puntos")
        print("3. Función de densidad de probabilidad")
        print("4. Volver al menú principal")
        
    def leer_ejecutar_opcion(self):
        self.opcion = int(input("\nSeleccione una opción: "))
        match self.opcion:
            case 1:
                print("\nPENDIENTE DE UNA RECTA")
                recta = Recta(0, 0, 0, 0)
                recta.leer_datos()
                recta.calcular_pendiente()
                recta.imprimir_pendiente()
            case 2:
                print("\nDISTANCIA ENTRE DOS PUNTOS")
                distancia = Distancia()
                distancia.leer_datos()
                distancia.calcular_distancia()
                distancia.imprimir_distancia()
            case 3:
                print("\nFUNCIÓN DE DENSIDAD DE PROBABILIDAD")
                funcion = Funcion()
                funcion.leer_datos()
                funcion.calcular_fx()
                funcion.imprimir_fx()
                
    def ejecutar(self):
        while self.opcion != 4:
            self.mostrar_menu_basicos()
            self.leer_ejecutar_opcion()