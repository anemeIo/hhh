import sys
from PyQt5 import QtWidgets
from youi import Ui_MainWindow
import webbrowser

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.youi = Ui_MainWindow()
        self.youi.setupUi(self)

    def on_pushButton_clicked(self):
        query = self.youi.cc.text()
        url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(url)


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()

sys.exit(app.exec())
