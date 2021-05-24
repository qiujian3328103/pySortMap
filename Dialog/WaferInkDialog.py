from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QDialog, QApplication, QHeaderView, QTreeWidgetItem, QLabel

from UI import Ui_Ink_Dialog


class ShowInkDialog(QDialog, Ui_Ink_Dialog):

    ink_signal = pyqtSignal(dict)

    def __init__(self):
        super(QDialog, self).__init__()

        Ui_Ink_Dialog.__init__(self)

        self.setupUi(self)

        self.ink_selection = {
            "auto_ink": False,
            "click_die_ink": self.toolButton_click.isChecked(),
            "drag_ink": self.toolButton_drag.isChecked(),
            "polygon_ink": self.toolButton_polygon.isChecked(),
        }

        self.toolButton_click.clicked.connect(self.emitInkSignal)
        self.toolButton_drag.clicked.connect(self.emitInkSignal)
        self.toolButton_polygon.clicked.connect(self.emitInkSignal)
        self.toolButton_reset.clicked.connect(self.emitInkSignal)
        self.toolButton_auto_ink.clicked.connect(self.emitInkSignal)


    def emitInkSignal(self):
        """
        change the tool states on toolButton
        :return:
        """
        # click and drag mode can only either one be use

        if self.toolButton_click.isChecked():
            self.toolButton_drag.setChecked(False)

        if self.toolButton_drag.isChecked():
            self.toolButton_click.setChecked(False)
            self.toolButton_polygon.setChecked(False)

        if self.toolButton_polygon.isChecked():
            self.toolButton_drag.setChecked(False)

        self.ink_selection = {
            "auto_ink": False,
            "click_die_ink": self.toolButton_click.isChecked(),
            "drag_ink": self.toolButton_drag.isChecked(),
            "polygon_ink": self.toolButton_polygon.isChecked(),
        }
        self.ink_signal.emit(self.ink_selection)





if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = ShowInkDialog()
    Dialog.show()
    sys.exit(app.exec_())