
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QRadioButton, QLineEdit,  QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QIntValidator, QDoubleValidator, QPixmap, QColor, QPalette
from random import *

#todas las ventanas
txt_title = 'Salud de Sobre Peso'
win_x, win_y = 200, 100
win_width, win_height = 1000, 600
app = QApplication([])
txt_buttom_next = 'Siguiente'
#ventana 1
txt_princ = 'Bienvenido a Unidad de Sobre Peso y Obesidad'
txt_inf1 = 'Vamos a hacerle unas preguntas responda \n' \
'y despues le diremos cuanto tiene que bajar o subir de peso.\n' \
'\n' \
'lea y acepte o rechaze la propuesta que le estamos haciendo'
txt_btn_nxt_S = 'acepto'
txt_btn_nxt_N = 'rechazo'

#ventana 2
txt_n = 'Introduce lo que te piden abajo'
txt_len1 = 'Introduce tu edad, no mientas viejo'
txt_le1 = 'Introduce tu edad'
txt_len2 = 'Introduce tu peso en kg'
txt_le2 = 'Introduce tu peso'
txt_len3 = 'Ya casi terminamos, introduce tu estatura en cm'
txt_le3 = 'Introduce tu estatura'


#ventana 3
txt_pregunt = 'puedes responder a estas preguntas \n' \
'son necesarias para ser más precisos'
txt_btn_circ1 = 'eres hombre'
txt_btn_circ2 = 'eres mujuer'
inf_txt1 = 'informacion de lo que hacemos'
inf_txt2 = 'Nosotros solo estamos intentando ayudarlos a saber cuanto te falta\n' \
'para que veas de que esa meta es posible no es algo que no puedas lograr\n' \
'no queremos que te sientas mal contigo porque no te podemos ayudar a sentarte bien\n' \
'ya fuera de broma no es para que te sientas mal por que tienes más o menos peso\n' \
'porquue todos somos diferentes. Que tengas un bonito fin de semana.'

#ventana 4
tetxo_introc = 'si las respuestas son negativas necesitas bajar \n' \
'y si las respuestas son positivas necesitas subir'
texto_resp1 = 'esto es lo que te falta para llegar al peso promedio'