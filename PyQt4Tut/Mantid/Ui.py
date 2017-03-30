import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):

    font = QtGui.QFont()
    font.setBold(True)
    font.setUnderline(True)

    def __init__(self):

        super(Window, self).__init__()

        self.initWindow()

    def initWindow(self):

        Layout = QtGui.QHBoxLayout(self)

        Lbox = QtGui.QVBoxLayout(self)


        topleft = QtGui.QFrame(self)
        Lbox.addWidget(topleft)
        topleft.setFrameStyle(QtGui.QFrame.StyledPanel)
        topleft.setGeometry(10, 10, 440, 155)

        self.initTopLeft(topleft)

        midleft = QtGui.QFrame(self)
        midleft.setFrameStyle(QtGui.QFrame.StyledPanel)
        midleft.setGeometry(10, 175, 440, 65)

        Lbox.addWidget(midleft)

        self.initMidLeft(midleft)

        bottomleft = QtGui.QFrame(self)
        bottomleft.setFrameStyle(QtGui.QFrame.StyledPanel)
        bottomleft.setGeometry(10, 250, 440, 290)

        Lbox.addWidget(bottomleft)

        self.initBottomLeft(bottomleft)

        Rbox = QtGui.QVBoxLayout(self)

        topright = QtGui.QFrame(self)
        topright.setFrameStyle(QtGui.QFrame.StyledPanel)
        topright.setGeometry(460, 10, 440, 195)

        Rbox.addWidget(topright)

        self.initTopRight(topright)

        bottomright = QtGui.QFrame(self)
        bottomright.setFrameStyle(QtGui.QFrame.StyledPanel)
        bottomright.setGeometry(460, 215, 440, 325)

        Rbox.addWidget(bottomright)

        self.initBottomRight(bottomright)

        run = QtGui.QPushButton("Run", self)
        run.move(690, 555)

        cancel = QtGui.QPushButton("Cancel", self)
        cancel.move(800, 555)

        self.setLayout(Layout)
        self.setGeometry(300, 300, 910, 600)
        self.show()


    def initTopLeft(self, top):

        lbl = QtGui.QLabel('General', top)
        lbl.move(15, 5)

        lbl.setFont(self.font)

        currtabel = QtGui.QLabel('Coil currents table', top)
        currtabel.move(15,35)
        currtabel.adjustSize()

        currtabelLine = QtGui.QLineEdit(top)
        currtabelLine.move(180, 30)

        openfile = QtGui.QPushButton('Browse', top)
        openfile.move(350, 30)
        openfile.clicked.connect(self.showFiles)

        theta = QtGui.QLabel('2-Theta tolerance', top)
        theta.move(15, 65)
        theta.adjustSize()

        thetaLine = QtGui.QLineEdit(top)
        thetaLine.move(180, 60)

        normal = QtGui.QLabel('Normalization', top)
        normal.move(15, 95)

        buttongroup = QtGui.QButtonGroup()

        normalradio = QtGui.QRadioButton('duration', top)
        normalradio.setCheckable(True)
        normalradio.setChecked(True)
        normalradio.move(180,92)
        normalradio2 = QtGui.QRadioButton('monitor', top)
        normalradio2.setCheckable(True)
        normalradio2.move(280, 92)

        buttongroup.addButton(normalradio)
        buttongroup.addButton(normalradio2)

        wave = QtGui.QLabel("Neutron wavelength (\305)", top)
        wave.move(15, 125)

        waveline = QtGui.QLineEdit(top)
        waveline.move(200, 120)


    def initMidLeft(self, mid):

        lbl2 = QtGui.QLabel("Mask Detectors", mid)
        lbl2.move(15, 5)
        lbl2.setFont(self.font)

        minAngle = QtGui.QLabel("Min Angle", mid)
        minAngle.move(15, 35)

        minAngleLine = QtGui.QLineEdit(mid)
        minAngleLine.setGeometry(100, 30, 80, 27)

        maxAngle = QtGui.QLabel("Max Angle", mid)
        maxAngle.move(190, 35)

        maxAngleLine = QtGui.QLineEdit(mid)
        maxAngleLine.setGeometry(275, 30, 80, 25)


    def initBottomLeft(self, bot):

        lbl3 = QtGui.QLabel("Output", bot)
        lbl3.move(15, 5)
        lbl3.setFont(self.font)

        outdir = QtGui.QLabel("Output directory", bot)
        outdir.move(15, 35)

        outdirLine = QtGui.QLineEdit(bot)
        outdirLine.move(180, 30)

        openFile = QtGui.QPushButton("Browse", bot)
        openFile.move(350, 30)
        openFile.clicked.connect(self.showFiles)

        outfile = QtGui.QLabel("Output file prefix", bot)
        outfile.move(15, 65)

        outfileLine = QtGui.QLineEdit(bot)
        outfileLine.move(180, 60)

        buttongroup2 = QtGui.QButtonGroup()

        soft = QtGui.QRadioButton("Soft matter", bot)
        soft.move(15, 130)
        soft.setChecked(True)

        buttongroup2.addButton(soft)

        magnetic = QtGui.QRadioButton("Magnetic powder", bot)
        magnetic.move(15, 175)

        buttongroup2.addButton(magnetic)

        single = QtGui.QRadioButton("Single Crystal", bot)
        single.move(15, 220)

        buttongroup2.addButton(single)


    def initTopRight(self, topr):

        lbl4 = QtGui.QLabel("Standard data", topr)
        lbl4.move(15, 5)
        lbl4.setFont(self.font)

        path = QtGui.QLabel("Path", topr)
        path.move(15,35)

        pathLine = QtGui.QLineEdit(topr)
        pathLine.move(180, 30)

        openFile = QtGui.QPushButton("Browse", topr)
        openFile.move(350, 30)
        openFile.clicked.connect(self.showFiles)

        vand = QtGui.QLabel("Vanadium Suffix", topr)
        vand.move(15, 65)

        vandLine = QtGui.QLineEdit(topr)
        vandLine.move(180, 60)

        nicr = QtGui.QLabel("NiCr Suffix", topr)
        nicr.move(15, 95)

        nircLine = QtGui.QLineEdit(topr)
        nircLine.move(180, 90)

        background = QtGui.QLabel("Background Suffix", topr)
        background.move(15, 125)

        backgroundLine = QtGui.QLineEdit(topr)
        backgroundLine.move(180, 120)

        sum = QtGui.QCheckBox("Sum Vanadium", topr)
        sum.move(15, 160)


    def initBottomRight(self, bot):

        lbl4 = QtGui.QLabel("Sample data", bot)
        lbl4.move(15, 5)
        lbl4.setFont(self.font)

        data = QtGui.QLabel("Data path", bot)
        data.move(15, 35)

        dataLine = QtGui.QLineEdit(bot)
        dataLine.move(180, 30)

        openFile = QtGui.QPushButton("Browse", bot)
        openFile.move(350, 30)
        openFile.clicked.connect(self.showFiles)

        file = QtGui.QLabel("File", bot)
        file.move(15, 65)

        pre = QtGui.QLabel("prefix", bot)
        pre.move(60, 65)

        preLine = QtGui.QLineEdit(bot)
        preLine.setGeometry(125, 60, 80, 27)

        suf = QtGui.QLabel("suffix", bot)
        suf.move(225, 65)

        sufLine = QtGui.QLineEdit(bot)
        sufLine.setGeometry(290, 60, 80, 27)

        Table = QtGui.QTableWidget(8, 2, bot)
        Table.setGeometry(15, 105, 400, 200)
        Table.setHorizontalHeaderLabels(["Run numbers", "Comment"])
        #Table.setItem(0,0,QtGui.QTableWidgetItem("110:115"))
        Table.setColumnWidth(0, 181.5)
        Table.setColumnWidth(1, 181.5)






    def showFiles(self):

        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')





def main():

    app = QtGui.QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()