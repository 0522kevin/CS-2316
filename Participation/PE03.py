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
        pass

        # set attributes - do NOT change attribute names
        self.key_word_label = None
        self.key_word = None
        self.encoder = None
        self.decoder = None
        self.message_label = None
        self.message = None
        self.scrambler = None
        self.output_label = None
        self.output
        self.history_label = None
        self.history = None
        self.my_reset = None

        # set attribute default status
        pass

        # connect buttons
        pass


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
        vbox1 = None

        # level 2 - hbox
        hbox1 = None

        # level 3 - hbox
        hbox2 = None

        # level 4 - hbox
        hbox3 = None

        # level 5 - vbox
        vbox2 = None

        # level 6 - hbox
        hbox4 = None

        # set layout
        # You can set the layout/arrangement of your boxes here.

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

'''
    def message_scrambler(self):
        pass

    def reset_all(self):
        pass
'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Cryptography()
    main.show()
    exit_code = app.exec_()
    sys.exit(exit_code)
