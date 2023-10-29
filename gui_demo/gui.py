from PyQt5 import QtWidgets,uic,QtGui
import sys

class Demo(QtWidgets.QMainWindow):
    def __init__(self):
        super(Demo,self).__init__()
        uic.loadUi('guidemo/demo.ui',self)
        self.btn_press.clicked.connect(self.pressMe)
        self.sldFontSize.valueChanged.connect(self.slide)
        self.show()

    def pressMe(self):
        self.lblOutput.setText('Pressed!')
        #print('Pressed!')

    def slide(self,value):
        font = QtGui.QFont()
        font.setPointSize(value)
        self.lblOutput.setFont(font)
        self.lblOutput.setText(str(value))

app = QtWidgets.QApplication(sys.argv)
window = Demo()
app.exec_()