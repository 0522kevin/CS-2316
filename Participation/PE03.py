# Your import statements are provided below. Do NOT import
# any other modules for PE03 base
 
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QRadioButton,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget
    )

class Cryptography(QWidget):

    def __init__(self):
        # everything in self scope is required to be named the same
        super().__init__()

        #set window title
        self.setWindowTitle("Keyword Decoder")

        # set attributes - do NOT change attribute names
        self.key_word_label = QLabel("Keyword:")
        self.key_word = QLineEdit()
        self.encoder = QRadioButton("Encode")
        self.decoder = QRadioButton("Decode")
        self.scrambler = QPushButton("Scramble")
        self.my_reset = QPushButton("Reset")
        self.message_label = QLabel("Message:")
        self.message = QLineEdit()
        self.output_label = QLabel("Output Message...")
        self.output = QLineEdit()
        self.history_label = QLabel("History:\nInput/Output/Keyword")
        self.history = QListWidget()
        

        # set attribute default status
        self.encoder.setChecked(True)
        self.my_reset.setEnabled(False)

        # connect buttons
        self.scrambler.clicked.connect(self.message_scrambler)
        self.my_reset.clicked.connect(self.reset_all)


        ##############################################################
        # Create your own layout. You may use or ignore
        # the layout skeleton below.
        # It is ok if your layout differs from the example,
        # as long as all features are shown and functional.
        # Remember to set your layout!
        ##############################################################
        # layout (is base layout horizontal (hbox) or vertical (vbox))
        # You can create your boxes and add corresponding widgets below.
        # You can also see the Layout examples at the end of the prompt.

        # level 1 - vbox
        vbox1 = QVBoxLayout()

        # level 2 - hbox
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.key_word_label)
        hbox1.addWidget(self.key_word)

        # level 3 - hbox
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.encoder)
        hbox2.addWidget(self.decoder)

        # level 4 - hbox
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.message_label)
        hbox3.addWidget(self.message)

        # level 5 - vbox
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.scrambler)
        vbox2.addWidget(self.output_label)
        vbox2.addWidget(self.output)
        vbox2.addWidget(self.my_reset)

        # level 6 - hbox
        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.history_label)
        hbox4.addWidget(self.history)

        # set layout
        # You can set the layout/arrangement of your boxes here.
        vbox1.addLayout(hbox1)
        vbox1.addLayout(hbox2)
        vbox1.addLayout(hbox3)
        vbox1.addLayout(vbox2)
        vbox1.addLayout(hbox4)
        self.setLayout(vbox1)

    ##################################################################
    # this method is given to you; do NOT change for PE03 base
    def coder(self):
        a_bet = "abcdefghijklmnopqrstuvwxyz .?!,"
        keyword = self.key_word.text().lower()
        new_str = ""
        for i in keyword + a_bet:
            if i not in new_str:
                new_str += i
            else:
                continue
        if self.encoder.isChecked() == True:
            return {key:val for key, val in zip(list(a_bet), list(new_str))}
        if self.decoder.isChecked() == True:
            return {val:key for key, val in zip(list(a_bet), list(new_str))}
    ###################################################################


    def message_scrambler(self):
        self.my_reset.setEnabled(True)
        self.scrambler.setEnabled(False)
        self.key_word.setEnabled(False)
        self.message.setEnabled(False)

        dic = self.coder()
        temp = ""
        for char in self.message.text():
            temp += dic.get(char.lower())
        self.output.setText(temp)

        self.history.addItems(["/".join([self.message.text(), self.output.text(), self.key_word.text()])])

    def reset_all(self):
        self.my_reset.setEnabled(False)
        self.key_word.setEnabled(True)
        self.scrambler.setEnabled(True)
        self.message.setEnabled(True)

        self.message.clear()
        self.key_word.clear()
        self.output.clear()

        self.encoder.setChecked(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Cryptography()
    main.show()
    exit_code = app.exec_()
    sys.exit(exit_code)
