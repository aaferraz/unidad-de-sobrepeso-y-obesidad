from funciones import *

class Win_4 (QWidget):
    def __init__(self, intr_texto1, intr_texto2, intr_texto3):
        super().__init__()
        self.intr_texto1 = float(intr_texto1.text())
        self.intr_texto2 = float(intr_texto2.text())
        self.intr_texto3 = float(intr_texto3.text())
        self.set_appear()
        self.initUI()
        self.show()
        app.exec_()
        
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.calc1 = float(pow(self.intr_texto3, 2) * 18.5)
        self.calc2 = float(pow(self.intr_texto3, 2) * 24.99)
        self.txt_intr = QLabel(tetxo_introc).setFont(QFont(tetxo_introc, 36, QFont.Bold))
        self.txt_resp1 = QLabel(texto_resp1)
        self.resp1 = QLabel(str(self.calc1 - self.intr_texto2))
        self.txt_resp2 = QLabel(texto_resp2)
        self.resp2 = QLabel(str(self.calc2 - self.intr_texto2))
        self.H_layout = QHBoxLayout()
        self.V_layout = QVBoxLayout()
        self.V2_layout = QVBoxLayout()
        self.V_layout.addWidget(self.txt_intr)
        self.V_layout.addWidget(self.txt_resp1)
        self.V_layout.addWidget(self.txt_resp2)
        self.H_layout.addLayout(self.V2_layout)
        self.H_layout.addLayout(self.V_layout)
        self.setLayout(self.H_layout)
