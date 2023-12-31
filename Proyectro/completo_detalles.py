import sys
from PyQt6 import QtCore
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtWidgets import  QApplication, QVBoxLayout, QLabel, QWidget,QLineEdit, QPushButton, QMessageBox, QCheckBox

class ventana (QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setGeometry(0,0,800,800)
        self.setWindowTitle("Iniciar")
        self.generar()

    def generar(self):
        nom_l=QLabel(self)
        nom_l.setText('Nombre del Puesto')
        nom_l.setFont(QFont('Bond',10))
        nom_l.move(20,20)
        nom_t=QLineEdit(self)
        nom_t.setText('Ingrese el puesto...')
        nom_t.setFont(QFont('Bond',8))
        nom_t.move(20,40)
        nom_t.setFixedSize(750,20)

        codp_l=QLabel(self)
        codp_l.setText('Codigo de Puesto')
        codp_l.setFont(QFont('Bond',10))
        codp_l.move(20,60)
        codpt_t=QLineEdit(self)
        codpt_t.setText('Ingrese el codigo del puesto...')
        codpt_t.setFont(QFont('Bond',8))
        codpt_t.move(20,78)
        codpt_t.setFixedSize(400,20)

        area_l=QLabel(self)
        area_l.setText('Area de adscripcion')
        area_l.setFont(QFont('Bond',10))
        area_l.move(425,60)
        area_t=QLineEdit(self)
        area_t.setText('Ingrese el area de adscripcion...')
        area_t.setFont(QFont('Bond',8))
        area_t.move(425,78)
        area_t.setFixedSize(345,20)

        super_l=QLabel(self)
        super_l.setText('Puesto del Jefe Superior')
        super_l.setFont(QFont('Bond',10))
        super_l.move(20,100)
        super_t=QLineEdit(self)
        super_t.setText('Ingrese el puesto del jefe...')
        super_t.setFont(QFont('Bond',8))
        super_t.move(20,118)
        super_t.setFixedSize(750,20)

        jornada_l=QLabel(self)
        jornada_l.setText('Jornada')
        jornada_l.setFont(QFont('Bond',10))
        jornada_l.move(20,138)
        jornada_t=QLineEdit(self)
        jornada_t.setText('Ingrese la jornada...')
        jornada_t.setFont(QFont('Bond',8))
        jornada_t.move(20,155)
        jornada_t.setFixedSize(450,20)

        remuneracion_l=QLabel(self)
        remuneracion_l.setText('Remuneracion Mensual')
        remuneracion_l.setFont(QFont('Bond',10))
        remuneracion_l.move(475,138)
        area_tremuneracion_t=QLineEdit(self)
        area_tremuneracion_t.setText('Ingresa la remuneracion mensual...')
        area_tremuneracion_t.setFont(QFont('Bond',8))
        area_tremuneracion_t.move(475,155)
        area_tremuneracion_t.setFixedSize(295,20)

        prestaciones_l=QLabel(self)
        prestaciones_l.setText('Prestaciones')
        prestaciones_l.setFont(QFont('Bond',10))
        prestaciones_l.move(20,178)
        prestaciones_t=QLineEdit(self)
        prestaciones_t.setText('Ingrese las prestaciones...')
        prestaciones_t.setFont(QFont('Bond',8))
        prestaciones_t.move(20,196)
        prestaciones_t.setFixedSize(750,20)

        descripccion_l=QLabel(self)
        descripccion_l.setText('Descripcion General')
        descripccion_l.setFont(QFont('Bond',10))
        descripccion_l.move(20,218)
        descripccion_t=QLineEdit(self)
        descripccion_t.setText('Ingrese la descripccion...')
        descripccion_t.setFont(QFont('Bond',8))
        descripccion_t.move(20,236)
        descripccion_t.setFixedSize(750,20)

        funciones_l=QLabel(self)
        funciones_l.setText('Funciones')
        funciones_l.setFont(QFont('Bond',10))
        funciones_l.move(20,258)
        funciones_t=QLineEdit(self)
        funciones_t.setText('Ingrese las funciones...')
        funciones_t.setFont(QFont('Bond',8))
        funciones_t.move(20,273)
        funciones_t.setFixedSize(750,20)

        edad_l=QLabel(self)
        edad_l.setText('Edad')
        edad_l.setFont(QFont('Bond',10))
        edad_l.move(20,298)
        edad_t=QLineEdit(self)
        edad_t.setText('Ingrese su edad...')
        edad_t.setFont(QFont('Bond',8))
        edad_t.move(20,316)
        edad_t.setFixedSize(225,20)

        sexo_l=QLabel(self)
        sexo_l.setText('Sexo')
        sexo_l.setFont(QFont('Bond',10))
        sexo_l.move(255,298)
        sexo_t=QLineEdit(self)
        sexo_t.setText('Ingrese su sexo...')
        sexo_t.setFont(QFont('Bond',8))
        sexo_t.move(255,316)
        sexo_t.setFixedSize(225,20)

        civil_l=QLabel(self)
        civil_l.setText('Estado Civil')
        civil_l.setFont(QFont('Bond',10))
        civil_l.move(485,298)
        civil_t=QLineEdit(self)
        civil_t.setText('Ingrese su estado civil...')
        civil_t.setFont(QFont('Bond',8))
        civil_t.move(485,316)
        civil_t.setFixedSize(283,20)

#
        escolaridad_l=QLabel(self)
        escolaridad_l.setText('Escolaridad')
        escolaridad_l.setFont(QFont('Bond',10))
        escolaridad_l.move(20,340)
        escolaridad_t=QLineEdit(self)
        escolaridad_t.setText('Ingrese su nivel de educacion...')
        escolaridad_t.setFont(QFont('Bond',8))
        escolaridad_t.move(20,358)
        escolaridad_t.setFixedSize(225,20)

        gradoa_l=QLabel(self)
        gradoa_l.setText('Grado Avance')
        gradoa_l.setFont(QFont('Bond',10))
        gradoa_l.move(255,340)
        gradoa_t=QLineEdit(self)
        gradoa_t.setText('Ingrese si esta cursando...')
        gradoa_t.setFont(QFont('Bond',8))
        gradoa_t.move(255,358)
        gradoa_t.setFixedSize(225,20)

        carrera_l=QLabel(self)
        carrera_l.setText('Carrera')
        carrera_l.setFont(QFont('Bond',10))
        carrera_l.move(485,340)
        carrera_t=QLineEdit(self)
        carrera_t.setText('Ingrese su carrera...')
        carrera_t.setFont(QFont('Bond',8))
        carrera_t.move(485,358)
        carrera_t.setFixedSize(283,20)

        experiencia_l=QLabel(self)
        experiencia_l.setText('Experiencia')
        experiencia_l.setFont(QFont('Bond',10))
        experiencia_l.move(20,380)
        experiencia_t=QLineEdit(self)
        experiencia_t.setText('Ingrese los años de experiencia...')
        experiencia_t.setFont(QFont('Bond',8))
        experiencia_t.move(20,397)
        experiencia_t.setFixedSize(750,20)

        conocimentos_l=QLabel(self)
        conocimentos_l.setText('Conocimentos')
        conocimentos_l.setFont(QFont('Bond',10))
        conocimentos_l.move(20,419)
        conocimentos_t=QLineEdit(self)
        conocimentos_t.setText('Ingrese sus conocimientos...')
        conocimentos_t.setFont(QFont('Bond',8))
        conocimentos_t.move(20,435)
        conocimentos_t.setFixedSize(750,20)

        mequipo_l=QLabel(self)
        mequipo_l.setText('ManejoEquipo')
        mequipo_l.setFont(QFont('Bond',10))
        mequipo_l.move(20,457)
        mequipo_t=QLineEdit(self)
        mequipo_t.setText('Ingrese que equipo utiliza...')
        mequipo_t.setFont(QFont('Bond',8))
        mequipo_t.move(20,473)
        mequipo_t.setFixedSize(750,20)

        rfisicos_l=QLabel(self)
        rfisicos_l.setText('Requisitos Fisicos')
        rfisicos_l.setFont(QFont('Bond',10))
        rfisicos_l.move(20,495)
        rfisicos_t=QLineEdit(self)
        rfisicos_t.setText('Ingrese requisitos fisicos...')
        rfisicos_t.setFont(QFont('Bond',8))
        rfisicos_t.move(20,512)
        rfisicos_t.setFixedSize(750,20)

        rpsicologicos_l=QLabel(self)
        rpsicologicos_l.setText('Requisitos Psicologicos')
        rpsicologicos_l.setFont(QFont('Bond',10))
        rpsicologicos_l.move(20,535)
        rpsicologicos_t=QLineEdit(self)
        rpsicologicos_t.setText('Ingrese requisitos psicologicos...')
        rpsicologicos_t.setFont(QFont('Bond',8))
        rpsicologicos_t.move(20,551)
        rpsicologicos_t.setFixedSize(750,20)

        responsabilidades_l=QLabel(self)
        responsabilidades_l.setText('Responsabilidades')
        responsabilidades_l.setFont(QFont('Bond',10))
        responsabilidades_l.move(20,573)
        responsabilidades_t=QLineEdit(self)
        responsabilidades_t.setText('Ingrese las responsabilidades...')
        responsabilidades_t.setFont(QFont('Bond',8))
        responsabilidades_t.move(20,590)
        responsabilidades_t.setFixedSize(750,20)

        condiciones_l=QLabel(self)
        condiciones_l.setText('Condiciones de Trabajo')
        condiciones_l.setFont(QFont('Bond',10))
        condiciones_l.move(20,610)
        condiciones_t=QLineEdit(self)
        condiciones_t.setText('Ingrese las condiciones...')
        condiciones_t.setFont(QFont('Bond',8))
        condiciones_t.move(20,628)
        condiciones_t.setFixedSize(750,20)

        idiomas_l=QLabel(self)
        idiomas_l.setText('Idiomas')
        idiomas_l.setFont(QFont('Bond',10))
        idiomas_l.move(20,648)
        idiomast_t=QLineEdit(self)
        idiomast_t.setText('Ingrese los idiomas...')
        idiomast_t.setFont(QFont('Bond',8))
        idiomast_t.move(20,665)
        idiomast_t.setFixedSize(400,20)

        habilidades_l=QLabel(self)
        habilidades_l.setText('Habilidades')
        habilidades_l.setFont(QFont('Bond',10))
        habilidades_l.move(425,648)
        habilidades_t=QLineEdit(self)
        habilidades_t.setText('Ingrese sus habilidades...')
        habilidades_t.setFont(QFont('Bond',8))
        habilidades_t.move(425,665)
        habilidades_t.setFixedSize(345,20)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vent = ventana()
    vent.show()
    sys.exit(app.exec())