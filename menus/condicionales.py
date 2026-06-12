from clases.condicionales.ejercicio4 import Calculo
from clases.condicionales.ejercicio14 import Numero
from clases.condicionales.ejercicio17 import Division
from clases.condicionales.ejercicio18 import Alumnos
from clases.condicionales.ejercicio20 import IMC
from clases.condicionales.ejercicio24 import Entrada

class Condicional(object):
    def __init__(self):
        self.opcion = 0
        
    def mostrar_menu_condicionales(self):
        print("\n-----------MENU CONDICIONALES----------")
        print("1. Punto dentro, fuera o sobre una circunferencia")
        print("2. Identificar números primos")
        print("3. División de dos números")
        print("4. División de alumnos en grupos A y B")
        print("5. Calculo del IMC")
        print("6. Pago por sala de juego según la edad")
        print("7. Volver al menú principal")
        
    def leer_ejecutar_opcion(self):
        self.opcion = int(input("\nSeleccione una opción: "))
        match self.opcion:
            case 1:
                print("\nPUNTO DENTRO, FUERA O SOBRE UNA CIRCUNFERENCIA")
                calculo = Calculo()
                calculo.leer_datos()
                calculo.calcular()
                calculo.imprimir()
            case 2:
                print("\nIDENTIFICAR NÚMEROS PRIMOS")
                numero = Numero()
                numero.leer_datos()
                numero.imprimir_numero()
            case 3:
                print("\nDIVISIÓN DE DOS NÚMEROS")
                division = Division()
                division.leer_datos()
                division.dividir()
                division.imprimir_resultado()
            case 4:
                print("\nDIVISIÓN DE ALUMNOS EN GRUPOS")
                alumno = Alumnos()
                alumno.leer_datos()
                alumno.comparar_alumnos()
                alumno.imprimir_grupo()
            case 5:
                print("\nCALCULO DEL IMC")
                imc = IMC()
                imc.leer_datos()
                imc.calcular_imc()
                imc.comparar()
                imc.imprimir_resultado()
            case 6:
                print("\nPAGO POR SALA DE JUEGO SEGÚN LA EDAD")
                entrada = Entrada()
                entrada.leer_datos()
                entrada.calcular_entrada()
                entrada.mostrar_entrada()
                
    def ejecutar(self):
        while self.opcion != 7:
            self.mostrar_menu_condicionales()
            self.leer_ejecutar_opcion()