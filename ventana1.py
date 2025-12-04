from funciones import *
from ventana2 import *

class Win_1 (QWidget):
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
        self.texto_princ = QLabel (txt_princ)
        self.informacion = QLabel (txt_inf1)
        self.botton_S = QPushButton (txt_btn_nxt_S)
        self.botton_N = QPushButton (txt_btn_nxt_N)
        self.H_layout = QHBoxLayout()
        self.V_layout = QVBoxLayout()
        self.V2_layout = QVBoxLayout() 
        self.V_layout.addWidget(self.texto_princ)
        self.V_layout.addWidget(self.informacion)
        self.V_layout.addWidget(self.botton_S)
        self.V_layout.addWidget(self.botton_N)
        self.H_layout.addLayout(self.V_layout)
        self.H_layout.addLayout(self.V2_layout)
        self.setLayout(self.H_layout)
    def connect(self):
        self.botton_S.clicked.connect(self.next_click)
        self.botton_N.clicked.connect(self.End_click)
    def next_click (self):
        self.hide()
        self.camb_pan1 = Win_2()
    def End_click (self):
        self.hide()

ventana_pantalla = Win_1()