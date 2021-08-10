from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QColor, QPixmap, QPalette
from PyQt5.QtWidgets import QDialog, QApplication, QColorDialog

from UI import Ui_Ink_Dialog


class ShowInkDialog(QDialog, Ui_Ink_Dialog):
    ink_signal = pyqtSignal(dict)
    close_ink_dialog_signal = pyqtSignal(bool)
    def __init__(self):
        super(QDialog, self).__init__()

        Ui_Ink_Dialog.__init__(self)

        self.setupUi(self)

        # inital color for polygon tool
        self.toolButton_pick_poly_edge_color.setText("")
        self.toolButton_pick_poly_edge_color.setStyleSheet("background-color: {}".format(QColor('blue').name()))
        self.toolButton_pick_poly_point_color.setText("")
        self.toolButton_pick_poly_point_color.setStyleSheet("background-color: {}".format(QColor('green').name()))
        self.toolButton_pick_poly_click_color.setText("")
        self.toolButton_pick_poly_click_color.setStyleSheet("background-color: {}".format(QColor('red').name()))

        self.ink_selection = {
            "auto_ink": False,
            "click_die_ink": self.toolButton_click.isChecked(),
            "drag_ink": self.toolButton_drag.isChecked(),
            "polygon_ink": self.toolButton_polygon.isChecked(),
            "update_polygon_ink": False,
            "redraw_polygon": False,
            "ink_shape": self.comboBox_ink_shape.currentText(),
            "nearest_die_number": self.spinBox_ink_number.value(),
            "window_close": False,
            "polygon_props":{
                "polygon_color": self.toolButton_pick_poly_edge_color.palette().color(QPalette.Background),
                "polygon_radius": self.spinBox_polygon_radius.value(),
                "polygon_width": self.spinBox_polygon_width_size.value(),
                "grip_number": self.spinBox_polygon_num_points.value(),
                "grip_ellipse_size": self.spinBox_point_size.value(),
                "grip_ellipse_color": self.toolButton_pick_poly_point_color.palette().color(QPalette.Background),
                "polygon_hover_color": self.toolButton_pick_poly_click_color.palette().color(QPalette.Background)

            }
        }

        self.toolButton_click.clicked.connect(self.emitClickInkSignal)
        self.toolButton_drag.clicked.connect(self.emitDragInkSignal)
        self.toolButton_polygon.clicked.connect(self.emitPolygonInkSignal)
        self.toolButton_reset.clicked.connect(self.emitClickInkSignal)
        self.toolButton_auto_ink.clicked.connect(self.emitClickInkSignal)

        self.toolButton_pick_poly_edge_color.clicked.connect(lambda : self.clickButtonPickColor(self.toolButton_pick_poly_edge_color))
        self.toolButton_pick_poly_point_color.clicked.connect(lambda : self.clickButtonPickColor(self.toolButton_pick_poly_point_color))
        self.toolButton_pick_poly_click_color.clicked.connect(lambda: self.pickDoubleClickPolygonColor(self.toolButton_pick_poly_click_color))
        self.spinBox_polygon_num_points.valueChanged.connect(self.emitReDrawPolygonSignal)
        self.spinBox_polygon_radius.valueChanged.connect(self.emitReDrawPolygonSignal)
        self.spinBox_point_size.valueChanged.connect(self.emitReDrawPolygonSignal)
        self.spinBox_polygon_width_size.valueChanged.connect(self.emitPolygonLineWidthChangeSignal)
        self.spinBox_ink_number.valueChanged.connect(self.changeInkNearestDieNumber)
        self.comboBox_ink_shape.currentTextChanged.connect(self.changeInkDieShape)

    def emitClickInkSignal(self):
        """
        change the tool states on toolButton
        :return:
        """
        # click and drag mode can only either one be use
        # print(self.toolButton_click.isChecked())
        #
        if self.toolButton_click.isChecked():
            self.toolButton_drag.setChecked(False)
            self.toolButton_polygon.setChecked(False)

        self.ink_selection.update({
            "click_die_ink": self.toolButton_click.isChecked(),
            "drag_ink": self.toolButton_drag.isChecked(),
            "polygon_ink": self.toolButton_polygon.isChecked(),
            "update_polygon_ink": False,
            "redraw_polygon": False,
        })
        self.ink_signal.emit(self.ink_selection)

    def emitDragInkSignal(self):
        """
        change th tool sates to drag mode
        :return:
        """
        if self.toolButton_drag.isChecked():
            self.toolButton_click.setChecked(False)
            self.toolButton_polygon.setChecked(False)

        self.ink_selection.update({
            "click_die_ink": self.toolButton_click.isChecked(),
            "drag_ink": self.toolButton_drag.isChecked(),
            "polygon_ink": self.toolButton_polygon.isChecked(),
            "update_polygon_ink": False,
            "redraw_polygon": False
        })
        self.ink_signal.emit(self.ink_selection)

    def emitPolygonInkSignal(self):
        """
        emit the PolygonInk
        :return:
        """
        if self.toolButton_polygon.isChecked():
            self.toolButton_click.setChecked(True)
            self.toolButton_drag.setChecked(False)

        self.ink_selection.update({
            "polygon_ink": self.toolButton_polygon.isChecked(),
            "click_die_ink": self.toolButton_click.isChecked(),
            "update_polygon_ink": False,
            "redraw_polygon": False,
            "polygon_props": {
                "polygon_color": self.toolButton_pick_poly_edge_color.palette().color(QPalette.Background),
                "polygon_radius": self.spinBox_polygon_radius.value(),
                "polygon_width": self.spinBox_polygon_width_size.value(),
                "grip_number": self.spinBox_polygon_num_points.value(),
                "grip_ellipse_size": self.spinBox_point_size.value(),
                "grip_ellipse_color": self.toolButton_pick_poly_point_color.palette().color(QPalette.Background),
                "polygon_hover_color": self.toolButton_pick_poly_click_color.palette().color(QPalette.Background),
            }
        })
        self.ink_signal.emit(self.ink_selection)

    def clickButtonPickColor(self, Button):
        """
        click the pick color button
        :return:
        """
        color = QColorDialog.getColor()
        if color.isValid():
            self.die_edge_color = color
            Button.setStyleSheet("background-color: {}".format(color.name()))

        self.ink_selection.update({
            "update_polygon_ink": True,
            "redraw_polygon": False,
            "polygon_props": {
                "polygon_color": self.toolButton_pick_poly_edge_color.palette().color(QPalette.Background),
                "polygon_radius": self.spinBox_polygon_radius.value(),
                "polygon_width": self.spinBox_polygon_width_size.value(),
                "grip_number": self.spinBox_polygon_num_points.value(),
                "grip_ellipse_size": self.spinBox_point_size.value(),
                "grip_ellipse_color": self.toolButton_pick_poly_point_color.palette().color(QPalette.Background),
                "polygon_hover_color": self.toolButton_pick_poly_click_color.palette().color(QPalette.Background),
            }
        })
        self.ink_signal.emit(self.ink_selection)

    def emitPolygonLineWidthChangeSignal(self):
        """
        emit signal when the value changed
        :return:
        """
        self.ink_selection.update({
            "update_polygon_ink": True,
            "redraw_polygon": False,
            "polygon_props": {
                "polygon_color": self.toolButton_pick_poly_edge_color.palette().color(QPalette.Background),
                "polygon_radius": self.spinBox_polygon_radius.value(),
                "polygon_width": self.spinBox_polygon_width_size.value(),
                "grip_number": self.spinBox_polygon_num_points.value(),
                "grip_ellipse_size": self.spinBox_point_size.value(),
                "grip_ellipse_color": self.toolButton_pick_poly_point_color.palette().color(QPalette.Background),
                "polygon_hover_color": self.toolButton_pick_poly_click_color.palette().color(QPalette.Background),
            }
        })
        self.ink_signal.emit(self.ink_selection)

    def emitReDrawPolygonSignal(self):
        """
        todo: find better way to change in GripItem instead of current method redo the plot for polygon
        :return:
        """
        self.ink_selection.update({
            "update_polygon_ink": False,
            "redraw_polygon": True,
            "polygon_props": {
                "polygon_color": self.toolButton_pick_poly_edge_color.palette().color(QPalette.Background),
                "polygon_radius": self.spinBox_polygon_radius.value(),
                "polygon_width": self.spinBox_polygon_width_size.value(),
                "grip_number": self.spinBox_polygon_num_points.value(),
                "grip_ellipse_size": self.spinBox_point_size.value(),
                "grip_ellipse_color": self.toolButton_pick_poly_point_color.palette().color(QPalette.Background),
                "polygon_hover_color": self.toolButton_pick_poly_click_color.palette().color(QPalette.Background),
            }
        })
        self.ink_signal.emit(self.ink_selection)

    def pickDoubleClickPolygonColor(self, Button):
        color = QColorDialog.getColor()
        if color.isValid():
            self.die_edge_color = color
            Button.setStyleSheet("background-color: {}".format(color.name()))

        self.ink_selection.update({
            "update_polygon_ink": False,
            "redraw_polygon": True,
            "polygon_props": {
                "polygon_color": self.toolButton_pick_poly_edge_color.palette().color(QPalette.Background),
                "polygon_radius": self.spinBox_polygon_radius.value(),
                "polygon_width": self.spinBox_polygon_width_size.value(),
                "grip_number": self.spinBox_polygon_num_points.value(),
                "grip_ellipse_size": self.spinBox_point_size.value(),
                "grip_ellipse_color": self.toolButton_pick_poly_point_color.palette().color(QPalette.Background),
                "polygon_hover_color": self.toolButton_pick_poly_click_color.palette().color(QPalette.Background),
            }
        })
        self.ink_signal.emit(self.ink_selection)

    def changeInkDieShape(self):
        """
        current four modes, for ink die shape
        around
        cross
        conner
        all
        :return:
        """
        try:
            self.comboBox_ink_shape.currentText()
            pixmap = QPixmap()
            pixmap.load(":/mainwindowIcon/icons8_automatic.ico")
            pixmap = pixmap.scaledToWidth(96)
            self.label_type.setPixmap(pixmap)
        except Exception as e:
            print(e)

        self.ink_selection.update({
            "ink_shape": self.comboBox_ink_shape.currentText()
        })
        self.ink_signal.emit(self.ink_selection)

    def changeInkNearestDieNumber(self):
        """
        change inked dies numbers
        :return:
        """
        self.ink_selection.update({
            "nearest_die_number":self.spinBox_ink_number.value()
        })
        self.ink_signal.emit(self.ink_selection)




        # try:
        #     name = self.comboBox_inkoff_shape_type.currentText()
        #     pixmap = QPixmap()
        #     pixmap.load(":/newPrefix/{}.ico".format(name))
        #     pixmap = pixmap.scaledToWidth(96)
        #     self.label_inkoff_display.setPixmap(pixmap)
        #     self.statusBar().showMessage("Ink Search Algorithm Changed To {}".format(name))
        #     self.statusBar().setStyleSheet("QStatusBar{color:#008000;}")
        # except Exception as e:
        #     print(e)
        #     self.statusBar().showMessage("Cannot find the shape icon!")
        #     self.statusBar().setStyleSheet("QStatusBar{color:#E74C3C;}")
        #
        # self.graphicsView.search_shape = self.comboBox_inkoff_shape_type.currentText()
        # self.graphicsView.searchNearestN = int(self.comboBox_inkoff_number.currentText())

    def closeEvent(self, event):
        """
        close event signal emit
        :param event:
        :return:
        """
        # close = QMessageBox()
        # close.setText("?")
        # close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        # close = close.exec()
        # self.close_ink.emit(True)
        # self.ink_selection = {
        #     "window_close": True
        # }
        # self.ink_signal.emit(self.ink_selection)
        # event.accept()
        self.close_ink_dialog_signal.emit(True)
        self.hide()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = ShowInkDialog()
    Dialog.show()
    sys.exit(app.exec_())