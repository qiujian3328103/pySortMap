from PyQt5.QtWidgets import QGraphicsTextItem
from PyQt5.QtGui import QBrush, QColor, QTransform, QFont
from PyQt5.QtCore import QRectF, Qt, pyqtSignal, QObject
import numpy as np


class TextItem(QGraphicsTextItem):
    """
    Text Item
    """
    def __init__(self, name, text_content="", font_size=6, x=-55, y=180):
        super(TextItem, self).__init__()

        self.x = x
        self.y = y
        # default is -55, 180, this is th position as wafer title, if use as cursor for color bar, change the x, y
        self.setPos(self.x, self.y)

        self.name = name

        # font.setWeight(100)
        self.resetFontSize(font_size=font_size)

        # flip the text item, since the previous entire graphic is flipped
        self.t = QTransform()
        # center_pos = self.boundingRect().center()
        # self.t.translate(-center_pos.x(), -center_pos.y())
        # self.t.rotate(-180)
        self.t.scale(1, -1)
        self.setTransform(self.t)

        # set the default text input
        self.setPlainText("{}".format(text_content))

    def resetFontSize(self, font_size):
        font = QFont()
        font.setPointSize(font_size)
        self.setFont(font)