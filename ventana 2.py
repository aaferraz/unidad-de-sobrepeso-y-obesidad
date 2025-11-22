from funciones import *

class Win_2 (QWidget):
    def __init__(self):
        QWidget().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle('REGLAS')
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.poner_nombre = QLabel ()
        #_N_W significa nueva ventana
        self.boton_N_V = QPushButton ()
        self.V_layout = QVBoxLayout ()
        self.poner_nombre.addWidget(self.V_layout)
        self.boton_N_V.addWidget(self.V_layout)
        
    def connect(self):
        pass