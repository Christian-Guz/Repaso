from clases.ciclos.ejercicio5 import Calculo
from clases.ciclos.ejercicio6 import Sumatoria
from clases.ciclos.ejercicio7 import Tabla
from clases.ciclos.ejercicio8 import Tablas
from clases.ciclos.ejercicio9 import Palabra
from clases.ciclos.ejercicio10 import Conteo
from clases.ciclos.ejercicio11 import Conteo_impares
from clases.ciclos.ejercicio12 import Numero
from clases.ciclos.ejercicio13 import Inversion
from clases.ciclos.ejercicio15 import Palabra_reves
from clases.ciclos.ejercicio16 import Frase_letra
from clases.ciclos.ejercicio19 import Saludo
from clases.ciclos.ejercicio21 import Division_div_rest
from clases.ciclos.ejercicio22 import Ahorro
from clases.ciclos.ejercicio23 import Venta
from clases.ciclos.ejercicio25 import Palabra_invertida

class Ciclos(object):
    def __init__(self):
        self.opcion = 0
        
    def mostrar_menu_ciclos(self):
        print("\n----------MENU CICLOS----------")
        print("1. Cálculo de sumatoria")
        print("2. Cálculo de sumatoria con e")
        print("3. Generar tabla de multiplicar")
        print("4. Generar tablas de multiplicar")
        print("5. Repetir 10 veces una palabra")
        print("6. Conteo de edad")
        print("7. Conteo de números impares")
        print("8. Cuenta atrás de números")
        print("9. Cálculo de inversión")
        print("10. Palabra al revés letra a letra")
        print("11. Número de letras de una frase")
        print("12. Saludo")
        print("13. Division con cociente y resto")
        print("14. Cálculo de ahorro con interés compuesto")
        print("15. Venta de panes con descuento")
        print("16. Palabra invertida")
        print("17. Volver al menú principal")
    
    def leer_ejecutar_opcion(self):
        self.opcion = int(input("\nSeleccione una opción: "))
        match self.opcion:
            case 1:
                print("\nCÁLCULO DE SUMATORIA")
                calculo = Calculo()
                calculo.leer_datos()
                calculo.calcular()
                calculo.imprimir()
            case 2:
                print("\nCÁLCULO DE SUMATORIA CON E")
                sumatoria = Sumatoria()
                sumatoria.leer_datos()
                sumatoria.calcular()
                sumatoria.imprimir()
            case 3:
                print("\nGENERAR TABLA DE MULTIPLICAR")
                tabla = Tabla()
                tabla.leer_datos()
                tabla.calcular_tabla()
            case 4:
                print("\nGENERAR TABLAS DE MULTIPLICAR")
                tablas = Tablas()
                tablas.calcular_tabla()
            case 5:
                print("\nREPETIR 10 VECES UNA PALABRA")
                palabra = Palabra()
                palabra.leer_datos()
                palabra.imprimir_palabra()
            case 6:
                print("\nCONTEO DE EDAD")
                conteo = Conteo()
                conteo.leer_datos()
                conteo.imprimir_conteo()
            case 7:
                print("\nCONTEO DE NÚMEROS IMPARES")
                conteo_impares = Conteo_impares()
                conteo_impares.leer_datos()
                conteo_impares.imprimir_conteo()
            case 8:
                print("\nCUENTA ATRÁS DE NÚMEROS")
                numero = Numero()
                numero.leer_datos()
                numero.imprimir_numero()
            case 9:
                print("\nCÁLCULO DE INVERSIÓN")
                inversion = Inversion()
                inversion.leer_datos()
                inversion.calcular_inversion()
            case 10:
                print("\nPALABRA AL REVÉS LETRA A LETRA")
                palabra = Palabra_reves()
                palabra.leer_datos()
                palabra.imprimir_palabra()
            case 11:
                print("\nNÚMERO DE LETRAS DE UNA FRASE")
                frase_letra = Frase_letra()
                frase_letra.leer_datos()
                frase_letra.buscar_letra()
                frase_letra.imprimir_palabra()
            case 12:
                print("\nSALUDO")
                saludo = Saludo()
                saludo.leer_datos()
                saludo.saludo()
                saludo.imprimir_saludo()
            case 13:
                print("\nDIVISIÓN CON COCIENTE Y RESTO")
                division = Division_div_rest()
                division.leer_datos()
                division.calcular_division()
                print(f"El cociente de la division es {division.c} y el resto es {division.r}")
            case 14:
                print("\nCÁLCULO DE AHORRO CON INTERÉS COMPUESTO")
                ahorro = Ahorro()
                ahorro.leer_datos()
                ahorro.calcular_ahorro()
                ahorro.imprimir_ahorro()
            case 15:
                print("\nVENTA DE PANES CON DESCUENTO")
                venta = Venta()
                venta.leer_datos()
                venta.calcular_venta()
                venta.mostrar_venta()
            case 16:
                print("\nPALABRA INVERTIDA")
                palabra_invertida = Palabra_invertida()
                palabra_invertida.leer_datos()
                palabra_invertida.invertir_palabra()
            
    def ejecutar(self):
        while self.opcion != 17:
            self.mostrar_menu_ciclos()
            self.leer_ejecutar_opcion()