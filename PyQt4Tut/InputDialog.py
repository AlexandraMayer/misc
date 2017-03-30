import sys
from PyQt4 import QtGui

class Dialog(QtGui.QMainWindow):

    def __init__(self):

        super(Dialog,self).__init__()

        self.initUI()

    def initUI(self):

        self.btn = QtGui.QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        #self.le = QtGui.QLineEdit(self)
        #self.le.move(130,22)

        #col = QtGui.QColor(0, 0, 0)

       # self.frm = QtGui.QFrame(self)
        #self.frm.setStyleSheet("QWidget { background-color: %s }"
        #                       % col.name())
        #self.frm.setGeometry(130, 22, 100, 100)

        vbox = QtGui.QVBoxLayout()

        self.btn.setSizePolicy(QtGui.QSizePolicy.Fixed,
                               QtGui.QSizePolicy.Fixed)

        #vbox.addWidget(self.btn)

        self.lbl = QtGui.QLabel('Knowledge only matters', self)
        self.lbl.move(130,20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        #self.textEdit = QtGui.QTextEdit()
        #self.setCentralWidget(self.textEdit)
        #self.statusBar()

        #openfile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        #openfile.setShortcut('Ctrl+O')
        #openfile.setStatusTip('Open new File')
        #openfile.triggered.connect(self.showDialog)

        #menubar = self.menuBar()
        #fileMenu = menubar.addMenu('&File')
        #fileMenu.addAction(openfile)



        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Dialogs')
        self.show()

    def showDialog(self):

        #text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog',
        #                                      'Enter your name:')

        #if ok:
        #    self.le.setText(str(text))

        #col = QtGui.QColorDialog.getColor()

        #if col.isValid():
        #    self.frm.setStyleSheet("QWidget { background-color: %s }"
        #                       % col.name())

        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)

        #fname = QtGui.QFileDialog.getOpenFileName(self,'Open file',
        #                                          '/home')
        #f = open(fname, 'r')

        #with f:
        #    data = f.read()
        #    self.textEdit.setText(data)


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Dialog()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()