import os
import sys
from moviepy.editor import VideoFileClip
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic, QtCore, QtGui, QtWidgets

app = QApplication(sys.argv)

class ImgComp(QMainWindow):
    def __init__(self):
        super(ImgComp, self).__init__()
        uic.loadUi("mainui.ui", self)

        self.actionQuit.triggered.connect(lambda x: app.quit())
        self.actionAdd.triggered.connect(self.open)

        self.add.clicked.connect(self.open)

    def open(self):
        fname = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Videos (*.mp4)')

        fdir = fname[0].split('/')

        for element in fdir:
            if element.endswith('.mp4'):

                clip = VideoFileClip(fname[0])

                save_path = QFileDialog.getSaveFileName(self, 'Save Image', '', 'All files (*)')

                self.IMAGE.setText('Look at the console')

                gif_name = str(save_path[0].split('.mp4')[0] + '.gif')

                clip.write_gif(gif_name, fps=10)

                self.IMAGE.setText('Done.')

                msg = QMessageBox()

                msg.setWindowTitle('Done')
                msg.setText('Done converting video ' + element +' to gif' + gif_name)
                msg.setIcon(QMessageBox.Information)
                
                msg.exec_()


def main():
    window = ImgComp()
    window.show()

    app.exec_()

if __name__ == "__main__":
    main()