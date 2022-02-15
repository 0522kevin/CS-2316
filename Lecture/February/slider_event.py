# Given by professor

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, 
    QVBoxLayout, QApplication,QLineEdit,QLabel, QPushButton)

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()      
        
        self.lcd = QLCDNumber(self)
        self.sld = QSlider(Qt.Horizontal, self)
        self.myline = QLineEdit()
        self.myline.returnPressed.connect(self.lcd_change2)
        self.alabel = QLabel("")
        self.button = QPushButton("Press me")
        self.button.setEnabled(False)
        self.button.clicked.connect(self.winner)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.lcd)
        self.vbox.addWidget(self.sld)
        self.vbox.addWidget(self.myline)
        self.vbox.addWidget(self.alabel)
        self.vbox.addWidget(self.button)

        self.setLayout(self.vbox)
        self.sld.valueChanged.connect(self.lcd_change)
        self.sld.valueChanged.connect(self.press)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Slider Example')
        self.show()
    
    def lcd_change(self):
        self.lcd.display(self.sld.value())
        if self.sld.value() > self.sld.maximum()*.75:
            self.alabel.setText("Too High!")
        elif self.sld.value() < self.sld.maximum()*.25:
            self.alabel.setText("Too Low!")
        else:
            self.alabel.setText("")

    def lcd_change2(self):
        self.lcd.display(int(self.myline.text())) 

    def press(self):
        if self.sld.value() >= 25:
            self.button.setEnabled(True)
        else:
            self.button.setEnabled(False)

    def winner(self):
        self.setWindowTitle("Winner!")




if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
