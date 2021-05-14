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

        self.images = {
            '1': {
                'original': self.ui.image_1_original,
                'filtered': self.ui.image_1_after_filter,
                'picker': self.ui.image_1_pick
            },
            '2': {
                'original': self.ui.image_2_original,
                'filtered': self.ui.image_2_after_filter,
                'picker': self.ui.image_2_pick
            }
        }

        self.img = {}

        self.ui.action_new.triggered.connect(self.new_instance)
        self.ui.action_exit.triggered.connect(self.close)

        self.ui.action_open_image_1.triggered.connect(lambda: self.open_image(self.images['1'], 1))
        self.ui.action_open_image_2.triggered.connect(lambda: self.open_image(self.images['2'], 2))

    def new_instance(self) -> None:
        self.child_window = MainWindow()
        self.child_window.show()

    def open_image(self, imageWidget: dict, channel: int) -> None:
        image = Image()
        if not image.path:
            return
        if len(self.img) == 1:
            if not image.compare(self.img[f'Image {2//channel}']['image']):
                qtw.QMessageBox.warning(self, 'failed', 'The Two Images Must be of the same size')
                return
            else : 
                self.img[f'Image {channel}'] = {'image': image, 'widgets': imageWidget}

        elif len(self.img) >= 2:
            if not image.compare(self.img[f'Image {2//channel}']['image']):
                qtw.QMessageBox.warning(self, 'failed', 'The Two Images Must be of the same size')
                return
            self.img[f'Image {channel}']["image"] = image
            self.img[f'Image {channel}']["widgets"] = imageWidget
        else :  
            self.img[f'Image {channel}'] = {'image': image, 'widgets': imageWidget}
        imageWidget['original'].setPixmap(image.get_pixmap().scaled(300,300, aspectRatioMode=qtc.Qt.KeepAspectRatio, transformMode=qtc.Qt.SmoothTransformation))
        imageWidget['picker'].setDisabled(False)
        self.ui.output_select.setDisabled(False)


def main_window():
    app = qtw.QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main_window()