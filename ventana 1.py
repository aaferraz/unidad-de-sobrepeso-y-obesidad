from funciones import *

class Win_1 (QWidgets):
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
       pass 
    def connect(self):
        pass