from PyQt5.QtGui import QColor
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QDialog, QApplication, QHeaderView, QTreeWidgetItem, QLabel, QColorDialog

from UI import Ui_App_Setting_Dialog



class ShowWaferSettingDialog(QDialog, Ui_App_Setting_Dialog):
    wafer_layout_changed = pyqtSignal(dict)
    wafer_title_changed = pyqtSignal(dict)
    die_props_changed = pyqtSignal(dict)
    substrate_color_changed = pyqtSignal(dict)

    def __init__(self):
        super(QDialog, self).__init__()

        Ui_App_Setting_Dialog.__init__(self)

        self.setupUi(self)

        self.toolButton_die_line_color.clicked.connect(lambda:self.pickColor(toolButton=self.toolButton_die_line_color))
        self.toolButton_flash_line_color.clicked.connect(lambda:self.pickColor(toolButton=self.toolButton_flash_line_color))
        self.toolButton_wafer_substrate_color.clicked.connect(lambda:self.pickColor(toolButton=self.toolButton_wafer_substrate_color, is_substrate_color=True))
        self.toolButton_die_untest_color.clicked.connect(lambda:self.pickColor(toolButton=self.toolButton_die_untest_color))

        self.spinBox_die_edge_size.valueChanged.connect(self.emitWaferLayoutSetting)
        self.checkBox_show_pass_die.stateChanged.connect(self.emitWaferLayoutSetting)
        self.checkBox_show_flash.stateChanged.connect(self.emitWaferLayoutSetting)
        self.checkBox_die_cosmetic.stateChanged.connect(self.emitWaferLayoutSetting)
        self.comboBox_die_line_style.currentTextChanged.connect(self.emitWaferLayoutSetting)

        self.plainTextEdit_wafer_title_name.textChanged.connect(self.emitWaferTitleSetting)
        self.spinBox_title_pos_x.valueChanged.connect(self.emitWaferTitleSetting)
        self.spinBox_title_pos_y.valueChanged.connect(self.emitWaferTitleSetting)
        self.spinBox_wafer_title_font.valueChanged.connect(self.emitWaferTitleSetting)


    def initialSetting(self):
        """
        initialize the setting dialog
        :return:
        """
        pass


    def pickColor(self, toolButton, is_substrate_color=False):
        """
        emit picked color and change the background of toolButton Color
        :return:
        :param toolButton:
        :param  is_substrate_color: based on the is substrate color to determine the emit signal
        """
        # get the current background color of toolButton
        # current_color = toolButton.palette().color(1)
        color = QColorDialog.getColor()
        if color.isValid():
            toolButton.setStyleSheet("background-color: {}".format(color.name()))
            # emit color by signal
            # if is_substrate_color:
            if is_substrate_color:
                self.emitWaferLayoutSetting()
            else:
                self.emitDieProperties()


    def emitWaferLayoutSetting(self):
        """
        get wafer layout setting and return the setting as dictionary to MainWindow
        redraw the entire wafer including the dies layout
        :return: dictionary with the setting
        """
        if self.comboBox_die_line_style.currentText() == "SolidLine":
            die_line_type = Qt.SolidLine
        elif self.comboBox_die_line_style.currentText() == "DashLine":
            die_line_type = Qt.DashLine
        elif self.comboBox_die_line_style.currentText() == "DashDotDotLine":
            die_line_type = Qt.DashDotDotLine
        elif self.comboBox_die_line_style.currentText() == "CustomerDashLine":
            die_line_type = Qt.CustomDashLine
        elif self.comboBox_die_line_style.currentText() == "DashDotLine":
            die_line_type = Qt.DashDotLine
        else:
            die_line_type = Qt.SolidLine


        layout_props = {
                        'die_default_color': self.toolButton_die_untest_color.palette().color(1),
                        'show_pass_die': self.checkBox_show_pass_die.isChecked(),
                        'show_flash_die': self.checkBox_show_flash.isChecked(),
                        'wafer_background_color': self.toolButton_wafer_substrate_color.palette().color(1)}

        die_props = {
            'die_line_type': die_line_type,
            'die_line_color': self.toolButton_die_line_color.palette().color(1),
            'die_line_width': self.spinBox_die_edge_size.value(),
            'die_cosmetic': self.checkBox_die_cosmetic.isChecked()
        }


        self.wafer_layout_changed.emit({
            "layout_props": layout_props,
            "die_props": die_props
        })


    def emitWaferTitleSetting(self):
        """
        get wafer title setting and return the setting as dictionary to MainWindow
        :return:
        """
        title_props = {
            'show_wafer_title': self.checkBox_wafer_title.isChecked(),
            'wafer_title': self.plainTextEdit_wafer_title_name.toPlainText(),
            'wafer_title_font': self.spinBox_wafer_title_font.value(),
            'wafer_title_pos_x': self.spinBox_title_pos_x.value(),
            'wafer_title_pos_y': self.spinBox_title_pos_y.value(),
        }
        self.wafer_title_changed.emit(title_props)


    def emitDieProperties(self):
        """
        emit the die properties signal to mianwindow
        :return:
        """
        if self.comboBox_die_line_style.currentText() == "SolidLine":
            die_line_type = Qt.SolidLine
        elif self.comboBox_die_line_style.currentText() == "DashLine":
            die_line_type = Qt.DashLine
        elif self.comboBox_die_line_style.currentText() == "DashDotDotLine":
            die_line_type = Qt.DashDotDotLine
        elif self.comboBox_die_line_style.currentText() == "CustomerDashLine":
            die_line_type = Qt.CustomDashLine
        elif self.comboBox_die_line_style.currentText() == "DashDotLine":
            die_line_type = Qt.DashDotLine
        else:
            die_line_type = Qt.SolidLine

        die_props = {
        'die_line_type': die_line_type,
        'die_line_color': self.toolButton_die_line_color.palette().color(1),
        'die_line_width': self.spinBox_die_edge_size.value(),
        'die_cosmetic': self.checkBox_die_cosmetic.isChecked()
        }

        self.die_props_changed.emit(die_props)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = ShowWaferSettingDialog()
    Dialog.show()
    sys.exit(app.exec_())
