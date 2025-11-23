from funciones import *
from ventana3 import Win_3

class Win_2 (QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connect()
        self.show()
        app.exec_() 

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        print('paso')
        self.texto_princ = QLabel (txt_n)
        self.texto_in1 = QLabel (txt_len1)
        self.intr_texto1 = QLineEdit (txt_le1)
        self.texto_in2 = QLabel (txt_len2)
        self.intr_texto2 = QLineEdit (txt_le2)
        self.texto_in3 = QLabel (txt_len3)
        self.intr_texto3 = QLineEdit (txt_le3)
        #_N_W significa nueva ventana
        self.boton_N_V = QPushButton (txt_buttom_next)
        self.H_layout = QHBoxLayout()
        self.V_layout = QVBoxLayout()
        self.V2_layout = QVBoxLayout()
        self.V_layout.addWidget(self.texto_princ)
        self.V_layout.addWidget(self.texto_in1)
        self.V_layout.addWidget(self.intr_texto1)
        self.V_layout.addWidget(self.texto_in2)
        self.V_layout.addWidget(self.intr_texto2)
        self.V_layout.addWidget(self.texto_in3)
        self.V_layout.addWidget(self.intr_texto3)
        self.V_layout.addWidget(self.boton_N_V)
        self.H_layout.addLayout(self.V_layout)
        self.H_layout.addLayout(self.V2_layout)
        self.setLayout(self.H_layout)

    def connect(self):
        self.boton_N_V.clicked.connect(self.next_click)
    def next_click (self):
        self.hide()
        self.camb_pan2 = Win_3()

# main_Win = QWidget()
# main_Win.show()
# app.exec_()
ventana_pantalla = Win_2()
# ventana_pantalla.show()
