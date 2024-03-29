import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QPushButton, QTableWidgetItem

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.pushButton.clicked.connect(self.load_data)

    def load_data(self):

        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM coffee").fetchall()
        self.tableWidget.setRowCount(len(result))
        if not result:
            self.statusBar().showMessage('Ничего не нашлось')
            return

        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
