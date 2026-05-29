from menus.basicos import Basicos
from menus.condicionales import Condicional
from menus.ciclos import Ciclos

class Principal(object):
    def __init__(self):
        self.opcion = 0
        
    def mostrar_menu_principal(self):
        print("\n----------MENU PRICIPAL----------")
        print("1. Básicos")
        print("2. Condicionales")
        print("3. Cíclos")
        print("4. Salir")
        
    def leer_ejecutar_opcion(self):
        self.opcion = int(input("Seleccione una opción: "))
        match self.opcion:
            case 1:
                menu_basicos = Basicos()
                menu_basicos.ejecutar()
            case 2:
                menu_condicionales = Condicional()
                menu_condicionales.ejecutar()
            case 3:
                menu_ciclos = Ciclos()
                menu_ciclos.ejecutar()
                
    def ejecutar(self):
        while self.opcion != 4:
            self.mostrar_menu_principal()
            self.leer_ejecutar_opcion()