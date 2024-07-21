import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
class DropDrag(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drop and Drag Example")
        self.resize(720, 420)
        self.initUI()
    def initUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(20,30) #left, top

        edit2 = QLineEdit('', self)
        edit2.setDragEnabled(False)
        edit2.move(20,70) #left, top

        btn = button('&button', self)
        btn.move(20, 100)

class button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)
    def dragInterEvent(self, event):
        if event.mineData().hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()
    def dragEvent(self, event):
        print("Drop Event")
        self.setText(event.mineData().text)




app = QApplication([sys.argv])
demo = DropDrag()
demo.show()
sys.exit(app.exec())