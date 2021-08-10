import numpy as np
from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QBrush, QColor, QLinearGradient, QGradient
from PyQt5.QtWidgets import (QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsItem)


class RectItem(QGraphicsRectItem):
    '''
    Rectangle call-back class inheritante from the QGraphicsRectItem
    for default the ink-flag is 0.
    0. not selectable to ink off
    1. prime yield or ship yield selectable to ink
    2. item selected and inked
    '''

    def __init__(self, x, y, x_label, y_label, width, height, color, alpha=1, name='Die_Item', inked_color=QColor('#FFFFFF'),
                 bin_number=None, **kwargs):
        """
        ink_flag to determine if dies can be ink-off
        ink_flag = 0: cannot be ink off
        ink_flag = 1: original prime / natural / ship yield die can be ink off
        ink_flag = 2: die inked
        :param x: Rect Item actual x position in graphic Scene
        :param y: Rect Item actual y position in graphic Scene
        :param width: Rect Item Width
        :param height: Rect item Height
        :param color: Rect Item brush color
        :param alpha: Rect Transparent value
        :param name: Rect Item name
        :param inked_color: ink color when select the die
        """
        super(RectItem, self).__init__(QRectF(x, y, width, height))
        # self.setZValue(2)
        # define the Rect name
        self.name = name
        # define the bin number for later auto ink off
        self.bin_number = bin_number
        # define the Rect Brush Color
        self.color = color
        # define the ink flag 0 un-markable, markable
        self.ink_flag = 0
        # define the color
        self._ink_color = inked_color

        # set the x label and y label, relative coordinate. Sort Coordinate in this application
        self.x_label = x_label
        self.y_label = y_label

        # set the position of the left bottom
        # self.setPos(x, y)

        # set the fill color
        self.setBrush(QBrush(self.color))
        # set the transparent of item
        self.setOpacity(alpha)
        #
        self.setAcceptHoverEvents(True)

        # set item selectable
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)

    def mousePressEvent(self, event):
        """
        customized press mouse to change the color
        :param event:
        :return:
        """
        # print(self.ink_flag)
        if self.ink_flag != 0:
            if self.brush() == self._ink_color:
                self.setBrush(self.color)
                # reset the ink flag back to 1
                self.markInkChange()
            else:
                self.setBrush(self._ink_color)
                # change the ink flag to 2, die already inked off
                self.markInkChange()
        QGraphicsRectItem.mousePressEvent(self, event)

    def markInkChange(self):
        """
        change the die to inked or un-ink

        1 is marked as die did not inked off
        2 is marked as die inked off
        :return:
        """
        if self.ink_flag == 1:
            self.ink_flag = 2
        elif self.ink_flag == 2:
            self.ink_flag = 1

    def setDieInkColor(self, color):
        """
        based on the ink flag value to change the ink off color
        :return:
        """
        if self.ink_flag ==2:
            self.setBrush(color)


class EllipseItem(QGraphicsEllipseItem):
    """
    customized the frame of the wafer
    """
    def __init__(self, x, y, width, height, color=Qt.black, bg_color=None, alpha=1, name='Wafer_Item'):
        super(EllipseItem, self).__init__(QRectF(-150, -150, 300, 300))

        self.name = name
        self.color = color
        self.setPen(self.color)
        if bg_color is not None:
            self.setBrush(bg_color)
            self.setZValue(-1)

        # set the oder of the z axis
        self.setOpacity(alpha)



class ColorBarItem(QGraphicsRectItem):
    def __init__(self, x, y, width, height, start_color, end_color, name='ColorBarItem'):
        """

        :param x: x position
        :param y: y position
        :param width: width of rectItem
        :param height: height of rectItem
        :param name: name of the color bar item
        :param start_color: start color the QGradientColor
        :param end_color: end color of the QGradientColor
        """
        super(ColorBarItem, self).__init__(QRectF(x, y, width, height))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = "ColorBarItem"
        self.start_color = start_color
        self.end_color = end_color
        self.text = ""

    def color_interpolator(self, factor):
        h0 = self.start_color.hsvHueF()
        h1 = self.end_color.hsvHueF()
        h1 -= round(h1-h0)
        hue = (h0*(1-factor) + h1*factor) % 1
        sat = self.start_color.hsvSaturationF() * (1 - factor) + self.end_color.hsvSaturationF() * factor
        val = self.start_color.valueF() * (1 - factor) + self.end_color.valueF() * factor
        return QColor.fromHsvF(hue, sat, val)

    def fillColorRectangle(self):
        """
        fill the color base assign gradient
        1. use the linearGradient create a list of color from 0 to 1
        2. use the setColorAt method in the linearGradient to assign the data range from 0 to 1
        :return:
        """
        gradient = QLinearGradient(0, 0, 0, 1)

        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)

        for i in np.linspace(0, 1, 10):
            gradient.setColorAt(i, self.color_interpolator(factor=i))
        self.setBrush(QBrush(gradient))

