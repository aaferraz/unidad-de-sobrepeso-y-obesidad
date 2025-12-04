from funciones import *
from ventana4 import Win_4

class Win_3 (QWidget):
    def __init__(self, intr_texto1, intr_texto2, intr_texto3):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connect()
        self.show()
        self.intr_text1 = intr_texto1
        self.intr_text2 = intr_texto2
        self.intr_text3 = intr_texto3
 
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.pregunt = QLabel(txt_pregunt)
        self.boton_inter1 = QRadioButton(txt_btn_circ1)
        self.boton_inter2 = QRadioButton(txt_btn_circ2)
        self.inf1 = QLabel(inf_txt1)
        self.inf2 = QLabel(inf_txt2)
        self.button_NV = QPushButton(txt_buttom_next)
        self.H_Layout = QHBoxLayout()
        self.L_Layout = QVBoxLayout()
        self.R_Layout = QVBoxLayout()
        self.L_Layout.addWidget(self.pregunt)
        self.L_Layout.addWidget(self.boton_inter1)
        self.L_Layout.addWidget(self.boton_inter2)
        self.L_Layout.addWidget(self.inf1)
        self.L_Layout.addWidget(self.inf2)
        self.L_Layout.addWidget(self.button_NV)
        self.H_Layout.addLayout(self.L_Layout)
        self.H_Layout.addLayout(self.R_Layout)
        self.setLayout(self.H_Layout)

    def connect(self):
        self.button_NV.clicked.connect(self.next_click)
    def next_click (self):
        self.hide()
        self.camb_pan2 = Win_4(self.intr_text1, self.intr_text2, self.intr_text3)