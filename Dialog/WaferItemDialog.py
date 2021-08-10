from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QDialog, QApplication, QHeaderView, QTreeWidgetItem, QLabel

from UI import Ui_Wafer_Dialog


class ShowWaferItemDialog(QDialog, Ui_Wafer_Dialog):
    select_item = pyqtSignal(dict)

    def __init__(self):
        super(QDialog, self).__init__()

        Ui_Wafer_Dialog.__init__(self)

        self.setupUi(self)

        # set up the splitter
        splitter_size = self.splitter.size()
        self.splitter.setSizes([splitter_size.height() * 0.9, splitter_size.height() * 0.1])

        # store lot data as dictionary for treeWidget
        self.lot_data = {}

        # store bin data as dictionary for treeWidget
        self.bin_group_data = {}

        # treeWidget set up
        self.treeWidget_lot.setAlternatingRowColors(True)
        # set up the header for treeWidget
        self.tree_header = self.treeWidget_lot.header()
        # content fit the cell size last column stretch
        self.tree_header.setSectionResizeMode(QHeaderView.Stretch)
        self.tree_header.setSectionResizeMode(0, QHeaderView.ResizeToContents)

        # tree Widget Item collapse
        self.item_collapse = False

        self.current_select_item = {}

        #
        self.pushButton_expand_bin_items.clicked.connect(self.binItemExpansion)
        self.pushButton_expand_lot_items.clicked.connect(self.lotItemExpansion)
        self.pushButton_checked_all_items.clicked.connect(self.checkAllBinItems)
        self.pushButton_close.clicked.connect(self.closeDialog)
        # self.treeWidget_lot.itemClicked.connect(self.clickItemEmitSignal)
        self.treeWidget_lot.itemSelectionChanged.connect(self.selectItemChangeEmitSignal)
        self.treeWidget_bin.itemClicked.connect(self.selectItemChangeEmitSignal)
        # self.treeWidget_bin..connect(self.selectItemChangeEmitSignal)



    def selectItemChangeEmitSignal(self):
        """
        click the item in the treeWidget to emit select item and emit the (wafer_id, wafer_number) to main
        :return:
        """
        # get lot and wafer select info
        lot_item = self.treeWidget_lot.currentItem()
        if lot_item.parent() is not None:
            lot_id = lot_item.parent().text(0)
            wafer_id = lot_item.text(0)
        else:
            lot_id = lot_item.text(0)
            wafer_id = None

        # get bin group select info
        # bin_group_item = self.treeWidget_bin.currentItem()
        root = self.treeWidget_bin.invisibleRootItem()
        parent_group = root.childCount()

        checked_items_list = []
        for i in range(parent_group):
            item = root.child(i)
            for j in range(item.childCount()):
                sub_item = item.child(j)
                if sub_item.checkState(0) == Qt.Checked:
                    # convert the bin_number string to int if read as number
                    checked_items_list.append(int(sub_item.text(1)))

        self.current_select_item = {"LOT_ID":[lot_id], "VENDOR_SCRIBE":[wafer_id], "BIN_NUMBER":checked_items_list}

        self.select_item.emit(self.current_select_item)


    def initializeLotTreeWidget(self):
        """
        initialize treeWidget based on data provides

        :input_data:

        {
            lot_id:
            [
            (number_of_wafers, (wafer_id_1, wafer_number_1)),
            (number_of_wafers, (wafer_id_2, wafer_number_2)),
            (number_of_wafers, (wafer_id_3, wafer_number_3)),
            (number_of_wafers, (wafer_id_4, wafer_number_4))
            ]
        }

        :return:

        -treeWidget Item Structure contains two columns

        Lot_ID_1
            Wafer_ID_1  Wafer_Alias_1
            Wafer_ID_2  wafer_Alias_2
        Lot_ID_2
            Wafer_ID_1  Wafer_Alias_1
            Wafer_ID_2  Wafer_Alias_2
        ...

        """

        if self.lot_data:
            self.treeWidget_lot.clear()
            self.treeWidget_lot.setColumnCount(2)
            self.treeWidget_lot.setHeaderLabels(["Lot/Wafer", "Wafer_Alias"])
            for lot in self.lot_data.keys():

                parent_item = QTreeWidgetItem([lot, " "])

                for wafer_data in enumerate(self.lot_data[lot]):
                    wafer_id = wafer_data[1][0]
                    wafer_alias = wafer_data[1][1]

                    child_item = QTreeWidgetItem([wafer_id, str(wafer_alias)])

                    parent_item.addChild(child_item)

                self.treeWidget_lot.addTopLevelItem(parent_item)

        self.treeWidget_lot.expandAll()


    def initializeBinTreeWidget(self):
        """
        initialize the bin treeWidget
        :input data:
        {
            (1, 'TEST ERROR'):
            [
                (900, 'WLC_LOG'),
                (999, 'Missing Limit')
            ]
        }
        :return:
        """

        if self.bin_group_data:
            self.treeWidget_bin.clear()
            self.treeWidget_bin.setColumnCount(4)
            self.treeWidget_bin.setHeaderLabels(["Check Box", "Layer Order", "Color", "Bin Desc"])

            for index, key in enumerate(self.bin_group_data):

                layer_num = key[0]
                bin_group_name = key[1]
                bin_group_color = key[2]

                parent_item = QTreeWidgetItem(self.treeWidget_bin)
                parent_item.setText(0, "")
                parent_item.setText(1, str(layer_num))

                label = QLabel("")
                label.setStyleSheet('''
                     background-color: {};
                     border: 1px solid black;
                     min-width: 40px;
                     max-width: 40px;'''.format(bin_group_color))

                parent_item.setText(3, bin_group_name)

                parent_item.setFlags(parent_item.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)

                self.treeWidget_bin.setItemWidget(parent_item, 2, label)

                for bin_info in self.bin_group_data[key]:

                    bin_number = bin_info[0]
                    bin_desc = bin_info[1]

                    child_item = QTreeWidgetItem(parent_item)
                    child_item.setText(0, "")
                    child_item.setText(1, str(bin_number))
                    # child_item.setFlags(Qt.NoItemFlags)
                    label_2 = QLabel("")
                    label_2.setWordWrap(True)
                    # label_2.setStyleSheet('''background-color: {}; border: 3px solid {};'''.format(bin_color, bin_color))
                    label_2.setStyleSheet('''background-color: {};
                                                 border: 1px solid black;
                                                 min-width: 40px;
                                                 max-width: 40px; '''.format(bin_group_color))

                    child_item.setText(3, bin_desc)
                    child_item.setCheckState(0, Qt.Checked)

                    self.treeWidget_bin.setItemWidget(child_item, 2, label_2)

                self.treeWidget_bin.addTopLevelItem(parent_item)

                header = self.treeWidget_bin.header()
                # header.setSectionResizeMode(QHeaderView.ResizeToContents)
                # header.setSectionResizeMode(QHeaderView.Stretch)
                header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
                header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
                header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
                header.setSectionResizeMode(3, QHeaderView.Stretch)


    def lotItemExpansion(self):
        """
        pushButton connect to treeWidget Expansion
        :param treeWidget:
        :return:
        """
        if self.pushButton_expand_lot_items.isChecked():
            self.treeWidget_lot.expandAll()
        else:
            self.treeWidget_lot.collapseAll()


    def binItemExpansion(self):
        """
        pushButton connect to treeWidget Expansion
        :return:
        """
        if self.pushButton_expand_bin_items.isChecked():
            self.treeWidget_bin.expandAll()
        else:
            self.treeWidget_bin.collapseAll()


    def checkAllBinItems(self):
        """
        pushButton connect to item check all selected bins
        :return:
        """
        root = self.treeWidget_bin.invisibleRootItem()
        parent_number = root.childCount()

        if root:
            for i in range(parent_number):
                parent_item = root.child(i)
                for j in range(parent_item.childCount()):
                    child_item = parent_item.child(j)
                    if self.pushButton_checked_all_items.isChecked():
                        child_item.setCheckState(0, Qt.Checked)
                    else:
                        child_item.setCheckState(0, Qt.Unchecked)


    def closeDialog(self):
        """
        close dialog
        :return:
        """
        self.close()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = ShowWaferItemDialog()
    Dialog.show()
    sys.exit(app.exec_())