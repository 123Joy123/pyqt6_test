from PyQt6.QtWidgets import QApplication, QWidget
import sys

from numpy import append

class Window(QWidget):
    def __init__(self):
        super().__init__()

app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec())