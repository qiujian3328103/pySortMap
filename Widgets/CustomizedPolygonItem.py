from PyQt5.QtCore import QRectF, Qt, pyqtSignal, QObject
from PyQt5.QtGui import QBrush, QColor, QPen, QCursor, QPolygonF, QPainterPath
from PyQt5.QtWidgets import (QGraphicsItem, QGraphicsPolygonItem, QGraphicsPathItem)


class PolygonAction(QObject):
    """
    class signal for polygon action
    """
    start_polygon_inking_signal = pyqtSignal()


class PolygonAnnotation(QGraphicsPolygonItem):
    def __init__(self, parent=None, polygon_props=None):
        super(PolygonAnnotation, self).__init__(parent)
        # set the polygon_setting
        if polygon_props is None:
            polygon_props={
                "polygon_color": QColor("green"),
                "polygon_radius": 50,
                "polygon_width": 2,
                "polygon_hover_color": QColor(255, 0, 0, 100),
                "grip_number": 10,
                "grip_ellipse_size": 6,
                "grip_square_size": 3,
                "grip_ellipse_width": 1,
                "grip_square_width": 1,
                "grip_ellipse_color": QColor(0, 0, 255),
                "grip_square_color": QColor(0, 255, 0),
                "grip_hover_color": QColor(255, 255, 0),
            }

        self.polygon_props = polygon_props
        self.name = "polygon_selector"

        # polygon ink action signal
        self.polygon_signal = PolygonAction()

        self.m_points = []
        # self.setZValue(10)
        self.setPen(QPen(self.polygon_props["polygon_color"], self.polygon_props["polygon_width"]))
        self.setAcceptHoverEvents(True)

        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)

        self.setCursor(QCursor(Qt.PointingHandCursor))

        self.m_items = []

    def addPoint(self, p):
        self.m_points.append(p)
        self.setPolygon(QPolygonF(self.m_points))
        grip_props = {
            "grip_ellipse_size": self.polygon_props["grip_ellipse_size"],
            "grip_square_size": self.polygon_props["grip_square_size"],
            "grip_ellipse_width": self.polygon_props["grip_ellipse_width"],
            "grip_square_width": self.polygon_props["grip_square_width"],
            "grip_ellipse_color": self.polygon_props["grip_ellipse_color"],
            "grip_square_color": self.polygon_props["grip_square_color"],
            "grip_hover_color": self.polygon_props["grip_hover_color"],
        }
        item = GripItem(self, len(self.m_points) - 1, grip_props=grip_props)
        self.scene().addItem(item)
        self.m_items.append(item)
        item.setPos(p)

    def movePoint(self, i, p):
        if 0 <= i < len(self.m_points):
            self.m_points[i] = self.mapFromScene(p)
            self.setPolygon(QPolygonF(self.m_points))
            # self.po

    def move_item(self, index, pos):
        if 0 <= index < len(self.m_items):
            # restrict the pos move out of the dics
            # if pos.x()**2 + pos.y()**2 >= math.pi*(160**2):
            item = self.m_items[index]
            item.setEnabled(False)
            item.setPos(pos)
            item.setEnabled(True)

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionHasChanged:
            for i, point in enumerate(self.m_points):
                self.move_item(i, self.mapToScene(point))

        return super(PolygonAnnotation, self).itemChange(change, value)

    def hoverEnterEvent(self, event):
        self.setBrush(self.polygon_props["polygon_hover_color"])
        super(PolygonAnnotation, self).hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.setBrush(QBrush(Qt.NoBrush))
        super(PolygonAnnotation, self).hoverLeaveEvent(event)

    def mouseDoubleClickEvent(self, event):
        """
        emit signal to graphic views in exist
        :param event:
        :return:
        """
        self.polygon_signal.start_polygon_inking_signal.emit()


class GripItem(QGraphicsPathItem):
    # circle = QPainterPath()
    # circle.addEllipse(QRectF(-5, -5, 10, 10))
    # square = QPainterPath()
    # square.addRect(QRectF(-5, -5, 10, 10))

    def __init__(self, annotation_item, index, grip_props):
        """
        grip the item and show the properties

        QRectF(x, y, width, height)
        grip_props={
            grip_ellipse_size: 6,
            grip_square_size: 3,
            grip_ellipse_color:
            grip_square_color:
        }
        :param annotation_item:
        :param index:
        :param grip_props: grip properties from the PolygonAnnotation
        """
        super(GripItem, self).__init__()
        self.name = "polygon_selector"

        self.ellipse_size = grip_props["grip_ellipse_size"]
        self.square_size = grip_props["grip_square_size"]
        self.ellipse_color = grip_props["grip_ellipse_color"]
        self.square_color = grip_props["grip_square_color"]
        self.ellipse_width = grip_props["grip_ellipse_width"]
        self.square_width = grip_props["grip_square_width"]
        self.grip_hover_color = grip_props["grip_hover_color"]

        self.circle = QPainterPath()
        self.circle.addEllipse(QRectF(-self.ellipse_size / 2, -self.ellipse_size / 2,
                                      self.ellipse_size, self.ellipse_size))

        self.square = QPainterPath()
        self.square.addRect(QRectF(-self.square_size / 2, -self.square_size / 2,
                                   self.square_size, self.square_size))

        self.m_annotation_item = annotation_item
        self.m_index = index

        # self.setPath(GripItem.circle)
        self.setPath(self.circle)
        self.setBrush(self.ellipse_color)
        self.setPen(QPen(self.ellipse_color, self.ellipse_width))
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setAcceptHoverEvents(True)
        self.setZValue(11)
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def hoverEnterEvent(self, event):
        # self.setPath(GripItem.square)
        self.setPath(self.square)
        self.setBrush(self.square_color)
        super(GripItem, self).hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        # self.setPath(GripItem.circle)
        self.setPath(self.circle)
        self.setBrush(self.grip_hover_color)
        # self.setBrush(QColor("green"))
        super(GripItem, self).hoverLeaveEvent(event)

    def mouseReleaseEvent(self, event):
        self.setSelected(False)
        super(GripItem, self).mouseReleaseEvent(event)

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange and self.isEnabled():
            self.m_annotation_item.movePoint(self.m_index, value)
        return super(GripItem, self).itemChange(change, value)

