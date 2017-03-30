import sys
from PyQt4 import QtGui, QtCore

class WidgetII(QtGui.QWidget):

    def __init__(self):
        super(WidgetII, self).__init__()

        self.initUI()

    def initUI(self):

        #LineEdit

        #self.lbl = QtGui.QLabel(self)
        #qle = QtGui.QLineEdit(self)

        #qle.move(60, 100)
        #self.lbl.move(60, 40)

        #qle.textChanged[str].connect(self.onChanged)

        #Splitter

        #hbox = QtGui.QHBoxLayout(self)

        #topleft = QtGui.QFrame(self)
        #topleft.setFrameShape(QtGui.QFrame.StyledPanel)

        #topright = QtGui.QFrame(self)
        #topright.setFrameShape(QtGui.QFrame.StyledPanel)

        #bottom = QtGui.QFrame(self)
        #bottom.setFrameShape(QtGui.QFrame.StyledPanel)

        #splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        #splitter1.addWidget(topleft)
        #splitter1.addWidget(topright)

        #splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        #splitter2.addWidget(splitter1)
        #splitter2.addWidget(bottom)

        #hbox.addWidget(splitter2)
        #self.setLayout(hbox)
        #QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))

        # ComboBox

        self.lbl = QtGui.QLabel("Ubuntu", self)

        combo = QtGui.QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Red Hat")
        combo.addItem("Gentoo")

        combo.move(50, 50)
        self.lbl.move(50, 150)

        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('WidgetsII')
        self.show()

    def onActivated(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()

    #def onChanged(self, text):

    #LineEdit

    #    self.lbl.setText(text)
    #    self.lbl.adjustSize()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = WidgetII()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()