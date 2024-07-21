import sys
from datetime import datetime
import calendar
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget
from PyQt5.QtCore import QDate

class Calender(QWidget):
    global currentYear, currentMonth
    currentYear = datetime.now().year
    currentMonth = datetime.now().month


    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calender")
        self.setGeometry(300,300,400,300)
        self.iniUI()
    def iniUI(self):
        self.calender = QCalendarWidget(self)
        self.calender.move(20,20)

        """Methods in calender"""

        self.calender.setGridVisible(True) #if True than you can see the line that divide date, a tabular form calender

        # self.calender.setMinimumDate(QDate(currentYear, currentMonth-1, 1)) #Set the minimum date you can access

        # self.calender.setMaximumDate(QDate(currentYear, currentMonth+1, calendar.monthrange(currentYear,currentMonth)[1])) #set the maximum date you can access

        # self.calender.setSelectedDate(QDate(currentYear, currentMonth, 1)) #if we use this, it open the calender by the mentioned date, like here curent year and month with day 1 selected

        """Signals in Calender"""

        # self.calender.clicked.connect(lambda val:print(val)) #this line print the dates you clicked on calender
        #convert the val in string
        # self.calender.clicked.connect(lambda val: print(val.toString())) #this one is more readable way.

        self.calender.clicked.connect(self.printData)

    def printData(self, qDate):
        print('(0)/(1)/(2)'.format(qDate.month(), qDate.day(), qDate.year())) #this will format the date
        print(f'Day number of the year {qDate.dayOfYear()}') #this statement print the number of day till the selected date
        print(f'Day number of the week {qDate.dayOfWeek()}') #this will print the week number monday = 1, tues = 2 etc, to selected date

app = QApplication([])
demo = Calender()
demo.show()
sys.exit(app.exec())