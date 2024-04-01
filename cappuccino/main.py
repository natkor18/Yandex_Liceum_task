import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QPushButton, QTableWidgetItem

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.pushButton.clicked.connect(self.load_data)
        self.pushButton_2.clicked.connect(self.update_data)

    def load_data(self):
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM coffee").fetchall()
        # print(result)
        self.tableWidget.setRowCount(len(result))
        if not result:
            self.statusBar().showMessage('Ничего не нашлось')
            return

        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def update_data(self):
        self.w = Window()
        self.w.show()



class Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.pushButton.clicked.connect(self.update_table)
        self.msg = QMessageBox()


    def update_table(self):
        msgBox = QMessageBox()
        cur = self.con.cursor()
        idx = int(self.id.text())
        title_sort = self.title_sort.text()
        degree_roasting = self.degree_roasting.text()
        ground_grains = int(self.ground_grains.text())
        taste = self.taste.text()
        price = float(self.price.text())
        packing_volume = float(self.packing_volume.text())

        lst = (idx, title_sort, degree_roasting, ground_grains, taste, price, packing_volume)
        res = cur.execute("SELECT * FROM coffee WHERE id=?", (idx,)).fetchall()
        title = [discr[0] for discr in cur.description]
        modif = {}
        i = 0
        for key in title:
            modif[key] = lst[i]
            i +=1
        try:
            if res:
                que = f'UPDATE coffee SET\n'
                que += ", ".join([f"{key}='{modif.get(key)}'"
                                  for key in modif.keys()])
                que += " WHERE id = ?"

                cur.execute(que, (self.id.text(),))
                self.con.commit()
                msgBox.setText("Запись успешна добавлена")
                msgBox.exec()
                modif.clear()
            else:
                que = f'INSERT INTO coffee (id, title_sort, degree_roasting, ground_grains, ' \
                      f'taste, price, packing_volume) VALUES {lst}'
                result = cur.execute(que)
                self.con.commit()
                msgBox.setText("Запись успешна добавлена")
                msgBox.exec()


        except ValueError:
            msgBox.setText("Ошибка добавления")
            msgBox.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
