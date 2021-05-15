from PyQt5.QtWidgets import QTreeWidget, QHeaderView, QTreeWidgetItem
from PyQt5.QtGui import QBrush, QColor, QTransform, QPen, QCursor, QPolygonF, QPainterPath, QLinearGradient, QPainter, QGradient
from PyQt5.QtCore import QRectF, Qt, pyqtSignal, QObject
import pandas as pd
import numpy as np


class LotTreeWidget(QTreeWidget):
    """
    customized Tree widget for select lot and wafer id

    data dictionary --->
    {
        "lot_1":(wafer_id, wafer_alias)
    }

    """
    def __init__(self, parent):
        super(LotTreeWidget, self).__init__(parent)

        # store data as dictionary for treeWidget
        self.data = {}

        # set up the header for treeWidget
        self.tree_header = self.header()
        # content fit the cell size last column stretch
        self.tree_header.setSectionResizeMode(QHeaderView.Stretch)
        self.tree_header.setSectionResizeMode(0, QHeaderView.ResizeToContents)

        # tree Widget Item collapse
        self.item_collapse = False

    def initializeTreeWidget(self):
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

        if self.data:
            self.clear()
            self.setColumnCount(2)
            self.setHeaderLabels(["Lot/Wafer", "Wafer_Alias"])
            for lot in self.data.keys():

                parent_item = QTreeWidgetItem([lot, " "])

                for wafer_data in enumerate(self.data[lot]):
                    wafer_id = wafer_data[1][0]
                    wafer_alias = wafer_data[1][1]

                    child_item = QTreeWidgetItem([wafer_id, str(wafer_alias)])

                    parent_item.addChild(child_item)

                self.addTopLevelItem(parent_item)

        self.expandAll()
