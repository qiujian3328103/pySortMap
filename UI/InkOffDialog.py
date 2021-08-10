# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inkoff_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ink_Dialog(object):
    def setupUi(self, Ink_Dialog):
        Ink_Dialog.setObjectName("Ink_Dialog")
        Ink_Dialog.resize(296, 633)
        self.gridLayout_5 = QtWidgets.QGridLayout(Ink_Dialog)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox = QtWidgets.QGroupBox(Ink_Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.toolButton_reset = QtWidgets.QToolButton(self.groupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/inkoffIcon/icons8_clear_formatting.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_reset.setIcon(icon)
        self.toolButton_reset.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_reset.setObjectName("toolButton_reset")
        self.gridLayout.addWidget(self.toolButton_reset, 0, 0, 1, 1)
        self.toolButton_click = QtWidgets.QToolButton(self.groupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/inkoffIcon/icons8_select_none_96.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_click.setIcon(icon1)
        self.toolButton_click.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_click.setCheckable(True)
        self.toolButton_click.setObjectName("toolButton_click")
        self.gridLayout.addWidget(self.toolButton_click, 0, 1, 1, 1)
        self.toolButton_drag = QtWidgets.QToolButton(self.groupBox)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/inkoffIcon/icons8_rectangular_4.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_drag.setIcon(icon2)
        self.toolButton_drag.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_drag.setCheckable(True)
        self.toolButton_drag.setChecked(True)
        self.toolButton_drag.setObjectName("toolButton_drag")
        self.gridLayout.addWidget(self.toolButton_drag, 0, 2, 1, 1)
        self.toolButton_polygon = QtWidgets.QToolButton(self.groupBox)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/inkoffIcon/icons8_polygon_96.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_polygon.setIcon(icon3)
        self.toolButton_polygon.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_polygon.setCheckable(True)
        self.toolButton_polygon.setObjectName("toolButton_polygon")
        self.gridLayout.addWidget(self.toolButton_polygon, 0, 3, 1, 1)
        self.toolButton_auto_ink = QtWidgets.QToolButton(self.groupBox)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/inkoffIcon/icons8_automatic_96_1zI_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_auto_ink.setIcon(icon4)
        self.toolButton_auto_ink.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_auto_ink.setObjectName("toolButton_auto_ink")
        self.gridLayout.addWidget(self.toolButton_auto_ink, 0, 4, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Ink_Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox_ink_number = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_ink_number.setMinimum(1)
        self.spinBox_ink_number.setMaximum(10)
        self.spinBox_ink_number.setProperty("value", 1)
        self.spinBox_ink_number.setObjectName("spinBox_ink_number")
        self.horizontalLayout.addWidget(self.spinBox_ink_number)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_ink_shape = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_ink_shape.setObjectName("comboBox_ink_shape")
        self.comboBox_ink_shape.addItem("")
        self.comboBox_ink_shape.addItem("")
        self.comboBox_ink_shape.addItem("")
        self.comboBox_ink_shape.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_ink_shape)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.pushButton_select_ink_bin = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_select_ink_bin.setObjectName("pushButton_select_ink_bin")
        self.gridLayout_2.addWidget(self.pushButton_select_ink_bin, 0, 0, 1, 1)
        self.pushButton_auto_ink = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_auto_ink.setObjectName("pushButton_auto_ink")
        self.gridLayout_2.addWidget(self.pushButton_auto_ink, 1, 0, 1, 1)
        self.pushButton_use_template_ink_off = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_use_template_ink_off.setObjectName("pushButton_use_template_ink_off")
        self.gridLayout_2.addWidget(self.pushButton_use_template_ink_off, 2, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(Ink_Dialog)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.page)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.toolButton_pick_poly_edge_color = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton_pick_poly_edge_color.setMinimumSize(QtCore.QSize(50, 25))
        self.toolButton_pick_poly_edge_color.setObjectName("toolButton_pick_poly_edge_color")
        self.horizontalLayout_3.addWidget(self.toolButton_pick_poly_edge_color)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.toolButton_pick_poly_click_color = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton_pick_poly_click_color.setMinimumSize(QtCore.QSize(50, 0))
        self.toolButton_pick_poly_click_color.setObjectName("toolButton_pick_poly_click_color")
        self.horizontalLayout_7.addWidget(self.toolButton_pick_poly_click_color)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.toolButton_pick_poly_point_color = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton_pick_poly_point_color.setMinimumSize(QtCore.QSize(50, 25))
        self.toolButton_pick_poly_point_color.setObjectName("toolButton_pick_poly_point_color")
        self.horizontalLayout_4.addWidget(self.toolButton_pick_poly_point_color)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.spinBox_polygon_num_points = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_polygon_num_points.setMinimum(2)
        self.spinBox_polygon_num_points.setProperty("value", 10)
        self.spinBox_polygon_num_points.setObjectName("spinBox_polygon_num_points")
        self.horizontalLayout_5.addWidget(self.spinBox_polygon_num_points)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.spinBox_point_size = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_point_size.setMinimum(1)
        self.spinBox_point_size.setProperty("value", 6)
        self.spinBox_point_size.setObjectName("spinBox_point_size")
        self.horizontalLayout_8.addWidget(self.spinBox_point_size)
        self.gridLayout_3.addLayout(self.horizontalLayout_8, 5, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.spinBox_polygon_width_size = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_polygon_width_size.setMinimum(1)
        self.spinBox_polygon_width_size.setMaximum(20)
        self.spinBox_polygon_width_size.setProperty("value", 2)
        self.spinBox_polygon_width_size.setObjectName("spinBox_poly_width_size")
        self.horizontalLayout_9.addWidget(self.spinBox_polygon_width_size)
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 6, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.spinBox_polygon_radius = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_polygon_radius.setMinimum(1)
        self.spinBox_polygon_radius.setMaximum(150)
        self.spinBox_polygon_radius.setProperty("value", 30)
        self.spinBox_polygon_radius.setObjectName("spinBox_polygon_radius")
        self.horizontalLayout_6.addWidget(self.spinBox_polygon_radius)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 4, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_5.addWidget(self.stackedWidget, 2, 0, 1, 1)

        self.retranslateUi(Ink_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Ink_Dialog)

    def retranslateUi(self, Ink_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Ink_Dialog.setWindowTitle(_translate("Ink_Dialog", "Ink Dialog"))
        self.groupBox.setTitle(_translate("Ink_Dialog", "Ink Off Tool"))
        self.toolButton_reset.setToolTip(_translate("Ink_Dialog", "rest the ink"))
        self.toolButton_reset.setText(_translate("Ink_Dialog", "..."))
        self.toolButton_click.setToolTip(_translate("Ink_Dialog", "click single die to ink"))
        self.toolButton_click.setText(_translate("Ink_Dialog", "..."))
        self.toolButton_drag.setToolTip(_translate("Ink_Dialog", "drag a square to ink"))
        self.toolButton_drag.setText(_translate("Ink_Dialog", "..."))
        self.toolButton_polygon.setToolTip(_translate("Ink_Dialog", "use polygon tool to ink"))
        self.toolButton_polygon.setText(_translate("Ink_Dialog", "..."))
        self.toolButton_auto_ink.setText(_translate("Ink_Dialog", "..."))
        self.groupBox_2.setTitle(_translate("Ink_Dialog", "Ink Off Mode Setting"))
        self.label.setText(_translate("Ink_Dialog", "Ink Dies Number:"))
        self.label_2.setText(_translate("Ink_Dialog", "Ink Mode:"))
        self.comboBox_ink_shape.setItemText(0, _translate("Ink_Dialog", "Around Dies"))
        self.comboBox_ink_shape.setItemText(1, _translate("Ink_Dialog", "Cross Dies"))
        self.comboBox_ink_shape.setItemText(2, _translate("Ink_Dialog", "Corner Dies"))
        self.comboBox_ink_shape.setItemText(3, _translate("Ink_Dialog", "Any Dies"))
        self.pushButton_select_ink_bin.setText(_translate("Ink_Dialog", "Select Ink Bins"))
        self.pushButton_auto_ink.setText(_translate("Ink_Dialog", "Auto Ink Off"))
        self.pushButton_use_template_ink_off.setText(_translate("Ink_Dialog", "Use Template"))
        self.groupBox_3.setTitle(_translate("Ink_Dialog", "Ink Tool Setting"))
        self.label_4.setText(_translate("Ink_Dialog", "Polygon Edge Color:"))
        self.toolButton_pick_poly_edge_color.setText(_translate("Ink_Dialog", "..."))
        self.label_3.setText(_translate("Ink_Dialog", "Polygon Point Click Color:"))
        self.toolButton_pick_poly_click_color.setText(_translate("Ink_Dialog", "..."))
        self.label_5.setText(_translate("Ink_Dialog", "Poloygon Point Color:"))
        self.toolButton_pick_poly_point_color.setText(_translate("Ink_Dialog", "..."))
        self.label_6.setText(_translate("Ink_Dialog", "Polygon Point Number:"))
        self.label_8.setText(_translate("Ink_Dialog", "Polygon Point Size:"))
        self.label_9.setText(_translate("Ink_Dialog", "Polygon Width Size:"))
        self.label_7.setText(_translate("Ink_Dialog", "Polygon Radius:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ink_Dialog = QtWidgets.QDialog()
    ui = Ui_Ink_Dialog()
    ui.setupUi(Ink_Dialog)
    Ink_Dialog.show()
    sys.exit(app.exec_())
