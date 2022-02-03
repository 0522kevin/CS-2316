# 2/2

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()  
        self.setWindowTitle("Hello CS2316")

        hbox1 = QHBoxLayout()
        b1 = QPushButton("Hello!")
        b1.clicked.connect(lambda x : print("Hi!"))
        hbox1.addWidget(b1)
        b2 = QPushButton("Hola!")
        b2.clicked.connect(self.on_button2_clicked)
        b2.clicked.connect(lambda x : b2.setText("Bonjour!"))
        hbox1.addWidget(b2)

        hbox2 = QHBoxLayout()
        b3 = QPushButton("Bye!")
        b3.clicked.connect(lambda x : print("Bye!"))
        hbox2.addWidget(b3)
        b4 = QPushButton("Chao!")
        b4.clicked.connect(self.on_button4_clicked)
        b4.clicked.connect(lambda x : b4.setText("Au revoir!"))
        hbox2.addWidget(b4)

        b5 = QPushButton("Extra!")
        b5.clicked.connect(lambda x : self.setWindowTitle("GUIs are Fun!"))
        hbox3 = QHBoxLayout()
        hbox3.addWidget(b5)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)

        self.setLayout(vbox)

    def on_button2_clicked(self):
        print("Hola!")

    def on_button4_clicked(self):
        print("Chao!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
