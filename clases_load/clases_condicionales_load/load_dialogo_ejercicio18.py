from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.condicionales.ejercicio18 import Alumnos

class DialogoEjercicio18(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ejercicio18.ui", self)
        self.btn_mostrar.clicked.connect(self.mostrar_grupos)
    
    def mostrar_grupos(self):
        alumno = Alumnos()
        alumno.nombre = self.txt_nombre.text()
        alumno.sexo = self.txt_sexo.text()
        alumno.comparar_alumnos()
        self.lbl_grupo.setText(f"El alumno {alumno.nombre} pertenece al {alumno.grupo}")