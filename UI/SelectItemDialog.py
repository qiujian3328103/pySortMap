# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lot_selection_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Wafer_Dialog(object):
    def setupUi(self, Wafer_Dialog):
        Wafer_Dialog.setObjectName("Wafer_Dialog")
        Wafer_Dialog.resize(506, 625)
        self.gridLayout_3 = QtWidgets.QGridLayout(Wafer_Dialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter = QtWidgets.QSplitter(Wafer_Dialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.treeWidget_lot = QtWidgets.QTreeWidget(self.groupBox)
        self.treeWidget_lot.setObjectName("treeWidget")
        self.treeWidget_lot.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.treeWidget_lot, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.treeWidget_bin = QtWidgets.QTreeWidget(self.groupBox_2)
        self.treeWidget_bin.setObjectName("treeWidget_bin")
        self.treeWidget_bin.headerItem().setText(0, "1")
        self.gridLayout_2.addWidget(self.treeWidget_bin, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 2)
        self.pushButton_expand_lot_items = QtWidgets.QPushButton(Wafer_Dialog)
        self.pushButton_expand_lot_items.setCheckable(True)
        self.pushButton_expand_lot_items.setChecked(True)
        self.pushButton_expand_lot_items.setObjectName("pushButton_expand_items")
        self.gridLayout_3.addWidget(self.pushButton_expand_lot_items, 1, 0, 1, 1)
        self.pushButton_expand_bin_items = QtWidgets.QPushButton(Wafer_Dialog)
        self.pushButton_expand_bin_items.setCheckable(True)
        self.pushButton_expand_bin_items.setChecked(True)
        self.pushButton_expand_bin_items.setObjectName("pushButton_expand_bin_items")
        self.gridLayout_3.addWidget(self.pushButton_expand_bin_items, 1, 1, 1, 1)
        self.pushButton_checked_all_items = QtWidgets.QPushButton(Wafer_Dialog)
        self.pushButton_checked_all_items.setCheckable(True)
        self.pushButton_checked_all_items.setChecked(True)
        self.pushButton_checked_all_items.setObjectName("pushButton_checked_all_items")
        self.gridLayout_3.addWidget(self.pushButton_checked_all_items, 2, 0, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(Wafer_Dialog)
        self.pushButton_close.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton_close, 2, 1, 1, 1)
        self.groupBox.raise_()
        self.pushButton_expand_lot_items.raise_()
        self.splitter.raise_()
        self.treeWidget_lot.raise_()
        self.groupBox_2.raise_()
        self.pushButton_expand_bin_items.raise_()
        self.pushButton_checked_all_items.raise_()
        self.pushButton_close.raise_()

        self.retranslateUi(Wafer_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Wafer_Dialog)

    def retranslateUi(self, Wafer_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Wafer_Dialog.setWindowTitle(_translate("Wafer_Dialog", "Wafer Selection Dialog"))
        self.groupBox.setTitle(_translate("Wafer_Dialog", "Wafer Selection"))
        self.groupBox_2.setTitle(_translate("Wafer_Dialog", "Bin Info"))
        self.pushButton_expand_lot_items.setText(_translate("Wafer_Dialog", "Expand Lot Items"))
        self.pushButton_expand_bin_items.setText(_translate("Wafer_Dialog", "Expand Bin Items"))
        self.pushButton_checked_all_items.setText(_translate("Wafer_Dialog", "Check All "))
        self.pushButton_close.setText(_translate("Wafer_Dialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Wafer_Dialog = QtWidgets.QDialog()
    ui = Ui_Wafer_Dialog()
    ui.setupUi(Wafer_Dialog)
    Wafer_Dialog.show()
    sys.exit(app.exec_())
