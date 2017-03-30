import sys
from PyQt4 import QtGui


class ExampleLayout(QtGui.QWidget):

    def __init__(self):
        super(ExampleLayout,self).__init__()

        self.initUI()

    def initUI(self):

        title = QtGui.QLabel('Title')
        author = QtGui.QLabel('Author')
        review = QtGui.QLabel('Review')

        titleEdit = QtGui.QLineEdit()
        authorEdit = QtGui.QLineEdit()
        reviewEdit = QtGui.QTextEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        #names = ['Cls', 'Bck', '', 'Close',
        #         '7', '8', '9', '/',
        #         '4', '5', '6', '*',
        #         '1', '2', '3', '-',
        #         '0', '.', '=', '+']

        #positions = [(i,j) for i in range(5) for j in range(4)]

        #for position, name in zip(positions,names):
        #
        #    if name == '':
        #        continue
        #
        #    button = QtGui.QPushButton(name)
        #    grid.addWidget(button, *position)


        #okButton = QtGui.QPushButton("OK")
        #cancelButton = QtGui.QPushButton("Cancel")

        #hbox = QtGui.QHBoxLayout()
        #hbox.addStretch(1)
        #hbox.addWidget(okButton)
        #hbox.addWidget(cancelButton)

        #vbox = QtGui.QVBoxLayout()
        #vbox.addStretch(1)
        #vbox.addLayout(hbox)

        #self.setLayout(vbox)

        #lbl1 = QtGui.QLabel('ZetCode', self)
        #lbl1.move(15,10)

        #lbl2 = QtGui.QLabel('tutorials', self)
        #lbl2.move(35,40)

        #lbl3 = QtGui.QLabel('for programmers', self)
        #lbl3.move(55,70)

        #self.setGeometry(400,400,400,200)

        self.move(300,150)
        self.setWindowTitle('Calculator')
        self.show()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = ExampleLayout()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()