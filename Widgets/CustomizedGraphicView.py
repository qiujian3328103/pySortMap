"""
Customized GraphicView Class inheritance from the QGraphicView
see example from: https://gist.github.com/eyllanesc/f305119027ae3b85dfcf8a3ef8c00238
"""
# from PyQt5.QtCore import
import math

import pandas as pd
from PyQt5.QtCore import pyqtSignal, QPoint, QRect, Qt, QSize, QEvent, QPointF
from PyQt5.QtGui import QPainter, QColor, QWheelEvent, QTransform, QMouseEvent
from PyQt5.QtWidgets import QGraphicsView, QRubberBand

from .CustomizedPolygonItem import PolygonAnnotation


class Viewer(QGraphicsView):
    rectChanged = pyqtSignal(QRect)

    def __init__(self, parent):
        super(Viewer, self).__init__(parent)
        self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)

        # define the Rect Items if exit
        self.rect_item_list = []

        # define the inked die shape search algorithm, default is around dies
        self.ink_shape = "Around Dies"

        # define the search Bin number
        self.searchNearestN = 1

        # mouse drag select item to ink off
        self.changeRubberBand = False


        self._zoom = 0
        self._empty = True
        # self._scene = QGraphicsScene(self)

        # define the ink off color, default color is white
        self.ink_color = "#FFFFFF"

        # is ink off mode on
        self._is_ink_mode_on = False

        # is_rubber band mode
        self._is_rubberBand_mode_on = False

        # is polygon ink selector selected
        self._is_polygon_mode_on = False

        # drag mode
        self._is_click_mode = False

        # is remove ink on rubberband
        self._is_remove_ink_from_rubberBand = False

        # flag value, if not select it is 0
        self.flag_list = []

        # stack map color bar
        self._is_colorBar_on = False

        # wafer map data
        self.map_data = pd.DataFrame()

        # add polygon item
        self.polygon_item = None

        # add color bar item
        self.colorBar_item = None

        # origin of the rectangle point
        self.origin_point = QPoint()

        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.TextAntialiasing)
        self.setMinimumSize(100, 100)
        self.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.scale(1, -1)
        self.scale(1.5, 1.5)

        # self.graphicsView.setDragMode(QGraphicsView.RubberBandDrag if self.actionDragMode.isChecked() else QGraphicsView.ScrollHandDrag)
        self.setMouseTracking(True)
        self.setOptimizationFlag(QGraphicsView.DontSavePainterState)
        self.setViewportUpdateMode(QGraphicsView.SmartViewportUpdate)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        # self.area = float()
        # self.setPoints()
        self.viewport().setCursor(Qt.ArrowCursor)

    def wheelEvent(self, event: QWheelEvent):
        """
        Zoom in or out of the view by mouse wheel scroll
        """
        zoomInFactor = 1.1
        zoomOutFactor = 0.9

        # Save the scene pos
        oldPos = self.mapToGlobal(event.pos())
        # oldPos = self.graphmapToScene(event.pos())

        # Zoom
        if event.angleDelta().y() > 0:
            zoomFactor = zoomInFactor
        else:
            zoomFactor = zoomOutFactor
        self.scale(zoomFactor, zoomFactor)
        # Get the new position
        newPos = self.mapToScene(event.pos())

        # Move scene to old position
        delta = newPos - oldPos

        self.translate(delta.x(), delta.y())

    def zoomMap(self, factor=1.1):
        """
        zoom in or out  the graphicView
        :param: default factor zoom in 1.1
        :return:
        """
        scale_tr = QTransform()
        scale_tr.scale(factor, factor)
        tr = self.transform() * scale_tr
        self.setTransform(tr)

    def rotateMap(self, angle=30):
        """
        default clockwise rotate 30 degree

        :param angle: default clockwise 30 degree rotate
        :return:
        """
        self.rotate(angle)

    def mousePressEvent(self, event):
        """
        mouse press event to drag a rectangle box
        :param QMouseEvent:
        :return:
        """
        if event.button() == Qt.LeftButton and (not self._is_click_mode):
            self.origin_point = event.pos()
            self.rubberBand.setGeometry(QRect(self.origin_point, QSize()))
            self.rectChanged.emit(self.rubberBand.geometry())
            self.rubberBand.show()
            self.changeRubberBand = True
            return
        elif event.button() == Qt.MidButton:
            self.viewport().setCursor(Qt.ClosedHandCursor)
            # self.original_event = QMouseEvent
            handmade_event = QMouseEvent(
                QEvent.MouseButtonPress,
                QPointF(event.pos()),
                Qt.LeftButton,
                event.buttons(),
                Qt.KeyboardModifier(),
            )
            QGraphicsView.mousePressEvent(self, handmade_event)

        super(Viewer, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        """
        release of the mouse release event
        :param event:
        :return:
        """
        if event.button() == Qt.LeftButton:
            self.changeRubberBand = False
            if self.rubberBand.isVisible():
                self.rubberBand.hide()
                # define the geometry of the rectangle
                rect = self.rubberBand.geometry()
                rect_scene = self.mapToScene(rect).boundingRect()
                # find all items in the rectangle Rubber Band
                selected_items = self.scene().items(rect_scene)
                # Check if rubber band mode on
                if self._is_rubberBand_mode_on:
                    self.inkSelectBins(selected_items=selected_items)


            QGraphicsView.mouseReleaseEvent(self, event)

        elif event.button() == Qt.MidButton:
            self.viewport().setCursor(Qt.ArrowCursor)
            handmade_event = QMouseEvent(
                QEvent.MouseButtonRelease,
                QPointF(event.pos()),
                Qt.LeftButton,
                event.buttons(),
                Qt.KeyboardModifiers(),
            )
            QGraphicsView.mouseReleaseEvent(self, handmade_event)

        super(Viewer, self).mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        if self.changeRubberBand:
            self.rubberBand.setGeometry(QRect(self.origin_point, event.pos()).normalized())
            self.rectChanged.emit(self.rubberBand.geometry())
            QGraphicsView.mouseMoveEvent(self, event)
        super(Viewer, self).mouseMoveEvent(event)

    def createPolygonSelector(self, polygon_props = None):
        """
        experiment to create a polygon selector to select items and ink-off
        :return:
        """
        props = {
            "polygon_color": QColor("blue"),
            "polygon_radius": 50,
            "polygon_width": 2,
            "polygon_hover_color": QColor(255, 0, 0, 100),
            "grip_number": 4,
            "grip_ellipse_size": 6,
            "grip_square_size": 3,
            "grip_ellipse_width": 1,
            "grip_square_width": 1,
            "grip_ellipse_color": QColor(0, 0, 255),
            "grip_square_color": QColor(0, 255, 0),
            "grip_hover_color": QColor(255, 255, 0),
        }
        if polygon_props is not None:
            if "polygon_color" in polygon_props.keys():
                props["polygon_color"] = QColor(polygon_props["polygon_color"])
            if "polygon_radius" in polygon_props.keys():
                props["polygon_radius"] = polygon_props["polygon_radius"]
            if "polygon_width" in polygon_props.keys():
                props["polygon_width"] = polygon_props["polygon_width"]
            if "grip_number" in polygon_props.keys():
                props["grip_number"] = polygon_props["grip_number"]
            if "grip_ellipse_color" in polygon_props.keys():
                props["grip_ellipse_color"] = polygon_props["grip_ellipse_color"]
            if "grip_hover_color" in polygon_props.keys():
                props["grip_hover_color"] = polygon_props["grip_hover_color"]
            if "grip_ellipse_size" in polygon_props.keys():
                props["grip_ellipse_size"] = polygon_props["grip_ellipse_size"]
            if "polygon_hover_color" in polygon_props.keys():
                props["polygon_hover_color"] = polygon_props["polygon_hover_color"]


        self.addPolygonSelector(self._is_polygon_mode_on, polygon_props=props)


    def addPolygonSelector(self, add_polygon, polygon_props):
        """
        triggered to add or remove the polygon item
        :return:
        """
        # rect = self.rubberBand.geometry()
        # rect_scene = self.mapToScene(rect).boundingRect()
        # selected_items = self.scene().items(rect_scene)
        sides = polygon_props["grip_number"]
        radius = polygon_props["polygon_radius"]
        if add_polygon:
            # check if the polygon selector exist
            if self.scene().polygon_selector_exist is False:
                self.scene().polygon_selector_exist = True
                self.polygon_item = PolygonAnnotation(polygon_props=polygon_props)
                # self.polygon_item.setBoundingRegionGranularity()
                self.polygon_item.polygon_signal.start_polygon_inking_signal.connect(self.doubleClickPolygonInk)
                self.scene().addItem(self.polygon_item)
                for i in range(sides):
                    angle = 2 * math.pi * i / sides
                    x = radius * math.cos(angle)
                    y = radius * math.sin(angle)
                    p = QPointF(x, y) + QPointF(0, 0)
                    self.polygon_item.addPoint(p)

        else:
            # remove base the item name
            for item in self.scene().items():
                if item.name == "polygon_selector":
                    self.scene().removeItem(item)
                    self.scene().polygon_selector_exist = False

    def removePolygonSelector(self):
        for item in self.scene().items():
            if item.name == "polygon_selector":
                self.scene().removeItem(item)
                self.scene().polygon_selector_exist = False

    def updatePolygonSelectorSetting(self, polygon_props):
        """
        update the polygon selector properties if polygon selector exist
        :param polygon_props:
        :return:
        """
        self.polygon_item.updatePolygonItemProperties(polygon_props)

    def doubleClickPolygonInk(self):
        """
        double click the polygon item if exist,
        ink off based on selection mode
        self.polygon_item use the QGraphicPolygonItem.shape() to find the items in the shape
        *** Must to use the self.polygon_item.mapToScene to get the relative location
        :return:
        """
        # if exit polygon item, check the scene

        if self.polygon_item:
            self.polygon_item.prepareGeometryChange()
            self.polygon_item.update()
            shape = self.polygon_item.shape()
            # todo: must to use the polygon_item it self mapToScene to covert
            rect_scene = self.polygon_item.mapToScene(shape)
            selected_item = self.scene().items(rect_scene)
            if selected_item:
                self.inkSelectBins(selected_items=selected_item)

    def findNearestBins(self, items, ink_shape):
        """
        based on the select search options to find the around dies
        Die_Items
            #
            #        (x, y)
            #      /
            #  (x-N, y-N)
        set the rules for bin area select
        :return:
        """
        nearest_item_list = []
        # if ink_shape == "Any Dies":
        #     nearest_item_list = None
        # elif ink_shape == "Around Dies":
        for select_item in items:
            # use the ink flag == 0 to restrict the item that can only select by one
            if ink_shape == "Any Dies":
                if select_item.name == "Die_Item" and select_item.ink_flag != 0:
                    # all the near item list is the selected die item not algorithm apply
                    coord = (select_item.x_label, select_item.y_label)
                    nearest_item_list.append(coord)
            elif ink_shape == "Around Dies":
                if select_item.name == "Die_Item" and select_item.ink_flag == 0:
                    # apply the around die algorithm find the around dies
                    x_start = select_item.x_label - self.searchNearestN
                    y_start = select_item.y_label - self.searchNearestN
                    for i in range(0, 2 * self.searchNearestN + 1):
                        x = x_start + i
                        for j in range(0, 2 * self.searchNearestN + 1):
                            y = y_start + j
                            coord = (x, y)
                            nearest_item_list.append(coord)
            elif ink_shape == "Cross Dies":
                if select_item.name == "Die_Item" and select_item.ink_flag == 0:
                    x_start = select_item.x_label
                    y_start = select_item.y_label
                    for i in range(0, self.searchNearestN + 1):
                        coord1 = (x_start + i, y_start)
                        coord2 = (x_start - i, y_start)
                        coord3 = (x_start, y_start + i)
                        coord4 = (x_start, y_start - i)
                        nearest_item_list.extend([coord1, coord2, coord3, coord4])
            elif ink_shape == "Corner Dies":
                if select_item.name == "Die_Item" and select_item.ink_flag == 0:
                    x_start = select_item.x_label
                    y_start = select_item.y_label
                    for i in range(0, self.searchNearestN + 1):
                        coord1 = (x_start + i, y_start + i)
                        coord2 = (x_start - i, y_start - i)
                        coord3 = (x_start + i, y_start - i)
                        coord4 = (x_start - i, y_start + i)
                        nearest_item_list.extend([coord1, coord2, coord3, coord4])
        # remove the duplicates coordinate
        nearest_item_list = list(set(nearest_item_list))
        return nearest_item_list

    def inkSelectBins(self, selected_items):
        """
        ink select bins
        :param selected_items:
        :return:
        """
        print(self.ink_shape)
        nearest_item_list = self.findNearestBins(items=selected_items, ink_shape=self.ink_shape)
        for die_item_label in nearest_item_list:
            if die_item_label in self.scene().graphics_item_dict.keys():
                die_item = self.scene().graphics_item_dict[die_item_label]
                if die_item.ink_flag == 1:
                    die_item.markInkChange()
                    # change die ink color
                    die_item.setDieInkColor(QColor(self.ink_color))