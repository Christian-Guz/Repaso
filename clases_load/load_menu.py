from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from clases_load.clases_basicas_load.load_dialogo_ejercicio1 import DialogoEjercicio1
from clases_load.clases_basicas_load.load_dialogo_ejercicio2 import DialogoEjercicio2
from clases_load.clases_basicas_load.load_dialogo_ejercicio3 import DialogoActividad3
from clases_load.clases_condicionales_load.load_dialogo_ejercicio4 import DialogoEjercicio4
from clases_load.clases_ciclos_load.load_dialogo_ejercicio5 import DialogoEjercicio5
from clases_load.clases_ciclos_load.load_dialogo_ejercicio6 import DialogoEjercicio6
from clases_load.clases_ciclos_load.load_dialogo_ejercicio7 import DialogoEjercicio7
from clases_load.clases_ciclos_load.load_dialogo_ejercicio8 import DialogoEjercicio8
from clases_load.clases_ciclos_load.load_dialogo_ejercicio9 import DialogoEjercicio9
from clases_load.clases_ciclos_load.load_dialogo_ejercicio10 import DialogoEjercicio10
from clases_load.clases_ciclos_load.load_dialogo_ejercicio11 import DialogoEjercicio11
from clases_load.clases_ciclos_load.load_dialogo_ejercicio12 import DialogoEjercicio12
from clases_load.clases_ciclos_load.load_dialogo_ejercicio13 import DialogoEjercicio13
from clases_load.clases_condicionales_load.load_dialogo_ejercicio14 import DialogoEjercicio14
from clases_load.clases_ciclos_load.load_dialogo_ejercicio15 import DialogoEjercicio15
from clases_load.clases_ciclos_load.load_dialogo_ejercicio16 import DialogoEjercicio16
from clases_load.clases_condicionales_load.load_dialogo_ejercicio17 import DialogoEjercicio17
from clases_load.clases_condicionales_load.load_dialogo_ejercicio18 import DialogoEjercicio18
from clases_load.clases_ciclos_load.load_dialogo_ejercicio19 import DialogoEjercicio19
from clases_load.clases_condicionales_load.load_dialogo_ejercicio20 import DialogoEjercicio20
from clases_load.clases_ciclos_load.load_dialogo_ejercicio21 import DialogoEjercicio21
from clases_load.clases_ciclos_load.load_dialogo_ejercicio22 import DialogoEjercicio22
from clases_load.clases_ciclos_load.load_dialogo_ejercicio23 import DialogoEjercicio23
from clases_load.clases_condicionales_load.load_dialogo_ejercicio24 import DialogoEjercicio24
from clases_load.clases_ciclos_load.load_dialogo_ejercicio25 import DialogoEjercicio25

class LoadMenu(QMainWindow):
    def  __init__(self):
        super().__init__()
        uic.loadUi("ui/Menu_Repaso.ui", self)
    
        self.actionEjercicio_1.triggered.connect(self.abrir_ejercicio1)
        self.actionEjercicio_2.triggered.connect(self.abrir_ejercicio2)
        self.actionEjercicio_3.triggered.connect(self.abrir_ejercicio3)
        self.actionEjercicio_4.triggered.connect(self.abrir_ejercicio4)
        self.actionEjercicio_5.triggered.connect(self.abrir_ejercicio5)
        self.actionEjercicio_6.triggered.connect(self.abrir_ejercicio6)
        self.actionEjercicio_7.triggered.connect(self.abrir_ejercicio7)
        self.actionEjercicio_8.triggered.connect(self.abrir_ejercicio8)
        self.actionEjercicio_9.triggered.connect(self.abrir_ejercicio9)
        self.actionEjercicio_10.triggered.connect(self.abrir_ejercicio10)
        self.actionEjercicio_11.triggered.connect(self.abrir_ejercicio11)
        self.actionEjercicio_12.triggered.connect(self.abrir_ejercicio12)
        self.actionEjercicio_13.triggered.connect(self.abrir_ejercicio13)  
        self.actionEjercicio_14.triggered.connect(self.abrir_ejercicio14)
        self.actionEjercicio_15.triggered.connect(self.abrir_ejercicio15)
        self.actionEjercicio_16.triggered.connect(self.abrir_ejercicio16)
        self.actionEjercicio_17.triggered.connect(self.abrir_ejercicio17)
        self.actionEjercicio_18.triggered.connect(self.abrir_ejercicio18)
        self.actionEjercicio_19.triggered.connect(self.abrir_ejercicio19)
        self.actionEjercicio_20.triggered.connect(self.abrir_ejercicio20)
        self.actionEjercicio_21.triggered.connect(self.abrir_ejercicio21)
        self.actionEjercicio_22.triggered.connect(self.abrir_ejercicio22)
        self.actionEjercicio_23.triggered.connect(self.abrir_ejercicio23)
        self.actionEjercicio_24.triggered.connect(self.abrir_ejercicio24)
        self.actionEjercicio_25.triggered.connect(self.abrir_ejercicio25)
        self.actionSalir.triggered.connect(self.close)
        
    def abrir_ejercicio1(self):
        ejercicio1 = DialogoEjercicio1()
        ejercicio1.exec_()
    def abrir_ejercicio2(self):
        ejercicio2 = DialogoEjercicio2()
        ejercicio2.exec_()
    def abrir_ejercicio3(self):
        actividad3 = DialogoActividad3()
        actividad3.exec_()
    def abrir_ejercicio4(self):
        actividad4 = DialogoEjercicio4()
        actividad4.exec_()
    def abrir_ejercicio5(self):
        actividad5 = DialogoEjercicio5()
        actividad5.exec_()
    def abrir_ejercicio6(self):
        actividad6 = DialogoEjercicio6()
        actividad6.exec_()
    def abrir_ejercicio7(self):
        actividad7 = DialogoEjercicio7()
        actividad7.exec_()
    def abrir_ejercicio8(self):
        actividad8 = DialogoEjercicio8()
        actividad8.exec_()
    def abrir_ejercicio9(self):
        actividad9 = DialogoEjercicio9()
        actividad9.exec_()
    def abrir_ejercicio10(self):
        actividad10 = DialogoEjercicio10()
        actividad10.exec_()
    def abrir_ejercicio11(self):
        actividad11 = DialogoEjercicio11()
        actividad11.exec_()
    def abrir_ejercicio12(self):
        actividad12 = DialogoEjercicio12()
        actividad12.exec_()
    def abrir_ejercicio13(self):
        actividad13 = DialogoEjercicio13()
        actividad13.exec_()
    def abrir_ejercicio14(self):
        actividad14 = DialogoEjercicio14()
        actividad14.exec_()
    def abrir_ejercicio15(self):
        actividad15 = DialogoEjercicio15()
        actividad15.exec_()
    def abrir_ejercicio16(self):
        actividad16 = DialogoEjercicio16()
        actividad16.exec_()
    def abrir_ejercicio17(self):
        actividad17 = DialogoEjercicio17()
        actividad17.exec_()
    def abrir_ejercicio18(self):
        actividad18 = DialogoEjercicio18()
        actividad18.exec_()
    def abrir_ejercicio19(self):
        actividad19 = DialogoEjercicio19()
        actividad19.exec_()
    def abrir_ejercicio20(self):
        actividad20 = DialogoEjercicio20()
        actividad20.exec_()
    def abrir_ejercicio21(self):
        actividad21 = DialogoEjercicio21()
        actividad21.exec_()
    def abrir_ejercicio22(self):
        actividad22 = DialogoEjercicio22()
        actividad22.exec_()
    def abrir_ejercicio23(self):
        actividad23 = DialogoEjercicio23()
        actividad23.exec_()
    def abrir_ejercicio24(self):
        actividad24 = DialogoEjercicio24()
        actividad24.exec_()
    def abrir_ejercicio25(self):
        actividad25 = DialogoEjercicio25()
        actividad25.exec_()
    def close(self):
        return super().close()