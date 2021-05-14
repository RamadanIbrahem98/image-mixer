import sys
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
from Image import Image
from main_layout import Ui_MainWindow

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


def main_window():
    app = qtw.QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main_window()