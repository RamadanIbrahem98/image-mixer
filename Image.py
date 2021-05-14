import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        self.path = qtw.QFileDialog.getOpenFileName(None, 'Load Image', './', "Image File(*.png *.jpg *.jpeg)")[0]
        if self.path:
            self.raw_data = plt.imread(self.path)
            self.format = self.path.split('.')[-1]
            if (self.format in ['jpg', 'jpeg']):
                self.raw_data = self.raw_data.astype('float32')
                self.raw_data /= 255
            self.shape = self.raw_data.shape
            self.WIDTH = self.shape[0]
            self.HEIGHT = self.shape[1]
            self.fft = np.fft.fft2(self.raw_data)
            self.magnitude = np.abs(self.fft)
            self.phase = np.angle(self.fft)
            self.real = np.real(self.fft)
            self.imaginary = np.imag(self.fft)
            self.pixmap = qtg.QPixmap(self.path)
            self.components = {
                '':'',
                'Magnitude':self.magnitude,
                'Phase':self.phase,
                'Real':self.real,
                'Imaginary': self.imaginary,
            }

    def compare(self, image2: 'Image') -> bool:
        return self.WIDTH == image2.WIDTH and self.HEIGHT == image2.HEIGHT

    def mix(self, image_2: 'Image', type_1: str, type_2: str, component_1_ratio: float, component_2_ratio: float, mode: str) -> qtg.QPixmap:
        pass