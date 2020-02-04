
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

if __name__ == '__main__':
     class mainform(QWidget):
          def __init__(self):
               super().__init__()
               self.getgui()

          def getgui(self):
               self.resize(300,100)
               self.move(300,300)
               self.setWindowTitle('calc')

               self.textbox = QLineEdit()
               self.textbox.setPlaceholderText('masukkan operasi hitung yang akan dijalankan..')
               self.button = QPushButton('hitung')
               self.button.clicked.connect(self.eval)
               self.hasil = QLineEdit()
               self.hasil.setReadOnly(True)

               vbox = QVBoxLayout()
               vbox.addWidget(self.textbox)
               vbox.addWidget(self.hasil)
               vbox.addWidget(self.button)
               self.setLayout(vbox)

          def eval(self):
               angka = self.textbox.text()
               result = str(eval(angka))
               self.hasil.setText(result)

     app = QApplication(sys.argv)
     form = mainform()
     form.show()
     app.exec_()
