"""

Hello Guyz, thankyou for reaching my profile and this tutorial repository.
I am going to cover every topic that i have learn about PyQt5 , which is one of the Module for
GUI in Python.
Let's get started
"""
"""
What is PyQt
It is an library created by RiverBank based on Qt framework to let you build desktop application
in python. Qt framework itself written in c/c++ abd the framework is also available in other programming
languages.

Pros&Cons:
Pros:
1. Has an UI design editor. UI file can be shared accross different languages.
2. Has much larger libraries and UI component.
3. Many learning resources available.
Cons:
1. Licence fee is expensive if you want to distribute your app commercially.
2. GPL licence
3. Steeper learning curve comparing to other framework.
"""
"""
Creating First application
"""
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
class myapp(QWidget):
    def __int___(self):
        super().__init__()
        self.resize(1200, 800)
        label = QLabel("Hello World")
        layout = QVBoxLayout
        self.setLayout(layout)
        layout.addWidget(label)

app = QApplication([])
app.setStyleSheet("""
QWidget{
font-size:50px;
}
""")
myApp = myapp()
myApp.show()
try:
    app.exec()
except SystemExit:
    print("Closing Windows")

