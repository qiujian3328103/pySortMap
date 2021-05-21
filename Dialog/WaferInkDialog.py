from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QDialog, QApplication, QHeaderView, QTreeWidgetItem, QLabel

from UI import Ui_Ink_Dialog


class ShowInkDialog(QDialog, Ui_Ink_Dialog):

    def __init__(self):
        super(QDialog, self).__init__()

        Ui_Ink_Dialog.__init__(self)

        self.setupUi(self)




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = ShowInkDialog()
    Dialog.show()
    sys.exit(app.exec_())