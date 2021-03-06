# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(526, 534)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = Viewer(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 526, 24))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setBaseSize(QtCore.QSize(0, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(33, 255, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 255, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.statusbar.setPalette(palette)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setAllowedAreas(QtCore.Qt.BottomToolBarArea|QtCore.Qt.LeftToolBarArea|QtCore.Qt.RightToolBarArea)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_Ink_Off = QtWidgets.QAction(MainWindow)
        self.action_Ink_Off.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mainwindowIcon/icons8_quill_with_ink.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Ink_Off.setIcon(icon)
        self.action_Ink_Off.setObjectName("action_Ink_Off")
        self.action_Stack_Map = QtWidgets.QAction(MainWindow)
        self.action_Stack_Map.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/mainwindowIcon/icons8_stack.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Stack_Map.setIcon(icon1)
        self.action_Stack_Map.setObjectName("action_Stack_Map")
        self.action_Lot_Dialog = QtWidgets.QAction(MainWindow)
        self.action_Lot_Dialog.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/mainwindowIcon/icons8_electronics.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Lot_Dialog.setIcon(icon2)
        self.action_Lot_Dialog.setObjectName("action_Lot_Dialog")
        self.action_Map_Setting = QtWidgets.QAction(MainWindow)
        self.action_Map_Setting.setCheckable(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/mainwindowIcon/icons8_automatic.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Map_Setting.setIcon(icon3)
        self.action_Map_Setting.setObjectName("action_Map_Setting")
        self.action_Import_File = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/mainwindowIcon/icons8_import_csv.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Import_File.setIcon(icon4)
        self.action_Import_File.setObjectName("action_Import_File")
        self.action_Zoom_In = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/mainwindowIcon/icons8_zoom_in.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Zoom_In.setIcon(icon5)
        self.action_Zoom_In.setObjectName("action_Zoom_In")
        self.action_Zoom_Out = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/mainwindowIcon/icons8_zoom_out.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Zoom_Out.setIcon(icon6)
        self.action_Zoom_Out.setObjectName("action_Zoom_Out")
        self.action_Reset = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/mainwindowIcon/icons8_refresh.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Reset.setIcon(icon7)
        self.action_Reset.setObjectName("action_Reset")
        self.action_Rotation_Left = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/mainwindowIcon/icons8_rotate_left.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Rotation_Left.setIcon(icon8)
        self.action_Rotation_Left.setObjectName("action_Rotation_Left")
        self.action_Rotation_Right = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/mainwindowIcon/icons8_rotate_right.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Rotation_Right.setIcon(icon9)
        self.action_Rotation_Right.setObjectName("action_Rotation_Right")
        self.menuMenu.addAction(self.action_Import_File)
        self.menuMenu.addAction(self.action_Lot_Dialog)
        self.menuMenu.addAction(self.action_Ink_Off)
        self.menuMenu.addAction(self.action_Stack_Map)
        self.menuMenu.addAction(self.action_Map_Setting)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.toolBar.addAction(self.action_Import_File)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Zoom_In)
        self.toolBar.addAction(self.action_Zoom_Out)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Rotation_Left)
        self.toolBar.addAction(self.action_Rotation_Right)
        self.toolBar.addAction(self.action_Reset)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Lot_Dialog)
        self.toolBar.addAction(self.action_Ink_Off)
        self.toolBar.addAction(self.action_Stack_Map)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Map_Setting)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sort Map 1.0"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_Ink_Off.setText(_translate("MainWindow", "Ink Off"))
        self.action_Ink_Off.setToolTip(_translate("MainWindow", "Select Ink Off Mode"))
        self.action_Stack_Map.setText(_translate("MainWindow", "Stack Map"))
        self.action_Lot_Dialog.setText(_translate("MainWindow", "Lot Dialog"))
        self.action_Map_Setting.setText(_translate("MainWindow", "Map Setting"))
        self.action_Import_File.setText(_translate("MainWindow", "Import File"))
        self.action_Zoom_In.setText(_translate("MainWindow", "Zoom_In"))
        self.action_Zoom_In.setToolTip(_translate("MainWindow", "Zoom In Map"))
        self.action_Zoom_Out.setText(_translate("MainWindow", "Zoom_Out"))
        self.action_Reset.setText(_translate("MainWindow", "reset"))
        self.action_Reset.setToolTip(_translate("MainWindow", "Reset Map"))
        self.action_Rotation_Left.setText(_translate("MainWindow", "Rotation_Left"))
        self.action_Rotation_Left.setToolTip(_translate("MainWindow", "Rotate Map Left"))
        self.action_Rotation_Right.setText(_translate("MainWindow", "Rotation_Right"))
        self.action_Rotation_Right.setToolTip(_translate("MainWindow", "Rotate Map Right"))
from Widgets import Viewer

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
