# 2/4

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QLabel

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()  
        self.setWindowTitle("Hello CS2316")

        hbox1 = QHBoxLayout()
        b1 = QPushButton("Hello!")
        b1.clicked.connect(self.change_label)
        hbox1.addWidget(b1)
        b2 = QPushButton("Hola!")
        b2.clicked.connect(self.change_label)
        hbox1.addWidget(b2)

        hbox2 = QHBoxLayout()
        b3 = QPushButton("Bye!")
        b3.clicked.connect(self.change_label)
        hbox2.addWidget(b3)
        b4 = QPushButton("Chao!")
        b4.clicked.connect(self.change_label)
        hbox2.addWidget(b4)

        b5 = QPushButton("Extra!")
        b5.clicked.connect(lambda x : self.setWindowTitle("GUIs are Fun!"))
        hbox3 = QHBoxLayout()
        hbox3.addWidget(b5)

        vbox = QVBoxLayout()

        self.word_entry = QLineEdit()
        vbox.addWidget(self.word_entry)
        self.word_entry.textEdited.connect(self.on_word_entered)

        self.label = QLabel("I will show you which button you click on!", self)
        vbox.addWidget(self.label)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)

        self.setLayout(vbox) 

    def on_button2_clicked(self):
        print("Hola!")

    def on_button4_clicked(self):
        print("Chao!")

    def on_word_entered(self):
        self.setWindowTitle(self.word_entry.text())

    def do_something(self):
        btn = self.sender()
        btn.setText("Me!")

    def change_label(self):
        self.label.setText(self.sender().text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
