import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QPushButton,
QDesktopWidget,QHBoxLayout,QVBoxLayout, QLineEdit,QInputDialog, QTextEdit)

class Main(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.hbox = QHBoxLayout()
        self.h1box = QHBoxLayout()
        self.h2box = QHBoxLayout()

        self.vbox = QVBoxLayout()

        self.btn = QPushButton('COM Select', self)

        self.Com_Status = QLineEdit(self)
        self.chat_body = QTextEdit(self)

        self.Message = QLineEdit(self)
        self.Message.setText("")

        self.btn_send = QPushButton('Send', self)

        self.hbox.addWidget(self.btn)
        self.hbox.addWidget(self.Com_Status)

        self.h1box.addWidget(self.chat_body)

        self.h2box.addWidget(self.Message)
        self.h2box.addWidget(self.btn_send)

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.h1box)
        self.vbox.addLayout(self.h2box)

        self.setLayout(self.vbox)

        self.resize(300,300)
        self.center()
        self.show()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Main()

    sys.exit(app.exec_())
