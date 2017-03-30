import sys
from PyQt4 import QtGui, QtCore


class Communicate(QtCore.QObject):

    closeApp = QtCore.pyqtSignal()


class Events(QtGui.QWidget):

    def __init__(self):
        super(Events, self).__init__()

        self.initUI()

    def initUI(self):

        lcd = QtGui.QLCDNumber(self)
        sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()

    def keyPressEvent(self, e):

        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

    def mousePressEvent(self, event):

            self.c.closeApp.emit()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Events()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()