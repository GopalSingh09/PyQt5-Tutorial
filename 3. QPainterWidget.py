import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap, QPen

imagepath = r"C:\Users\GOPAL SINGH\PycharmProjects\PyQt5Tutorial\Profile.jpg"

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.image = QPixmap(imagepath)
    def paintEvent(self, event):
        # print(self.rect()) #this line will print the coordinate of the screen when we increase or decrese the size of window using curson
        pen = QPen()
        pen.setWidth(5)#pixels

        #Upload image
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image) #this line will upload the image on the screen
        painter.setPen(pen)
        painter.drawEllipse(300,300,50,50) #draw an ellipse on the position
        """Due to the rect() if we increase or decrease the size of the screen, image size will also increase and decrease"""




app = QApplication(sys.argv)
demo = Demo()
demo.show()
sys.exit(app.exec())