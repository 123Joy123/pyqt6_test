from PyQt6.QtWidgets import QApplication, QWidget
import sys
from PyQt6.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
         # 设置标题
        self.setWindowTitle("PyQt6 Window")

        # 设置固定宽高
        # self.setFixedHeight(500)
        # self.setFixedWidth(500)
        self.setGeometry(500, 300, 400, 300) # 屏幕显示位置x，y值，和宽高

        # 设置背景颜色
        # self.setStyleSheet("background-color:red")
        stylesheet = (
            "background-color:red"
        )
        self.setStyleSheet(stylesheet)





app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec())