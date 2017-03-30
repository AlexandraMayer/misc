import sys
from PyQt4 import QtGui, QtCore

class Widget(QtGui.QWidget):

    def __init__(self):
        super(Widget, self).__init__()

        self.initUI()

    def initUI(self):

        #cb = QtGui.QCheckBox('Show title', self)
        #cb.move(20,20)
        #cb.toggle()
        #cb.stateChanged.connect(self.changeTitle)

        #self.col = QtGui.QColor(0, 0, 0)

        #redb = QtGui.QPushButton('Red', self)
        #redb.setCheckable(True)
        #redb.move(10, 10)

        #redb.clicked[bool].connect(self.setColor)

        #greenb = QtGui.QPushButton('Green', self)
        #greenb.setCheckable(True)
        #greenb.move(10, 60)

        #greenb.clicked[bool].connect(self.setColor)

        #blueb = QtGui.QPushButton('Blue',self)
        #blueb.setCheckable(True)
        #blueb.move(10, 110)

        #blueb.clicked[bool].connect(self.setColor)

        #self.square = QtGui.QFrame(self)
        #self.square.setGeometry(150, 20, 100, 100)
        #self.square.setStyleSheet("QWidget { background-color: %s }"
        #                          % self.col.name())

        #sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        #sld.setFocusPolicy(QtCore.Qt.NoFocus)
        #sld.setGeometry(30, 40, 100, 30)
        #sld.valueChanged[int].connect(self.changeValue)

        #self.label = QtGui.QLabel(self)
        #self.label.setPixmap()

        #self.pbar = QtGui.QProgressBar(self)
        #self.pbar.setGeometry(30, 40, 200, 25)

        #self.btn = QtGui.QPushButton('Start', self)
        #self.btn.move(40, 80)
        #self.btn.clicked.connect(self.doAction)

        #self.timer = QtCore.QBasicTimer()
        #self.step = 0

        cal = QtGui.QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QtCore.QDate].connect(self.showDate)

        self.lbl = QtGui.QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(175, 240)


        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('QtGui.QCheckBock')
        self.show()

    #def changeTitle(self, state):

        #if state == QtCore.Qt.Checked:
            #self.setWindowTitle('QtGui.QCheckBock')
        #else:
            #self.setWindowTitle('')

    #def setColor(self, pressed):

    #    source = self.sender()

    #    if pressed:
    #        val = 255
    #    else: val = 0

    #    if source.text() == "Red":
    #        self.col.setRed(val)
    #    elif source.text() == "Green":
    #        self.col.setGreen(val)
    #    else:
    #        self.col.setBlue(val)

    #    self.square.setStyleSheet("QFrame { background-color: %s }"
    #                              % self.col.name())

    #def changeValue(self, value):

        #if value == 0:
        #    self.label.setPixmap(QtGui.QPixmap("/home/alexandra/develop/misc/PyQt4Tut/mute.png"))

    #def timerEvent(self, e):

    #    if self.step >= 100:

    #        self.timer.stop()
    #        self.btn.setText('Finished')
    #        return

    #    self.step = self.step + 1
    #    self.pbar.setValue(self.step)

    #def doAction(self):

    #    if self.timer.isActive():
    #        self.timer.stop()
    #        self.btn.setText('Start')
    #    else:
    #        self.timer.start(100, self)
    #        self.btn.setText('Stop')

    def showDate(self, date):

        self.lbl.setText(date.toString())

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Widget()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
