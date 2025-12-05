from funciones import *

class Win_4 (QWidget):
    def __init__(self, intr_texto1, intr_texto2, intr_texto3, boton_inter1, boton_inter2):
        super().__init__()
        self.intr_texto1 = float(intr_texto1.text())
        self.intr_texto2 = float(intr_texto2.text())
        self.intr_texto3 = float(intr_texto3.text())
        self.boton_inter1 = boton_inter1
        self.boton_inter2 = boton_inter2
        self.set_appear()
        self.initUI()
        self.show()
        app.exec_()
        
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.txt_intr = QLabel(tetxo_introc)
        self.txt_intr.setFont(QFont(tetxo_introc, 10, QFont.Bold))
        self.txt_resp1 = QLabel(texto_resp1)
        self.H_layout = QHBoxLayout()
        self.V_layout = QVBoxLayout()
        self.V2_layout = QVBoxLayout()
        self.V_layout.addWidget(self.txt_intr)
        self.V_layout.addWidget(self.txt_resp1)
        print(self.boton_inter1, 'asdlasdaldasdasda')
        if self.boton_inter1.isChecked():
            self.calc1 = float(self.intr_texto3 - 100)
            self.resp1 = QLabel(str(self.calc1 - self.intr_texto2))
            self.V_layout.addWidget(self.resp1)
        else:
            self.calc2 = float(self.intr_texto3 - 104)
            self.resp2 = QLabel(str(self.calc2 - self.intr_texto2))
            self.V_layout.addWidget(self.resp2)
        self.H_layout.addLayout(self.V2_layout)
        self.H_layout.addLayout(self.V_layout)
        self.setLayout(self.H_layout)
