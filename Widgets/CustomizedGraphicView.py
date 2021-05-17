"""
Customized GraphicView Class inheritance from the QGraphicView
see example from: https://gist.github.com/eyllanesc/f305119027ae3b85dfcf8a3ef8c00238
"""
# from PyQt5.QtCore import
import pandas as pd
from PyQt5.QtCore import pyqtSignal, QPoint, QRect, Qt
from PyQt5.QtGui import QPainter, QColor, QWheelEvent, QTransform
from PyQt5.QtWidgets import QGraphicsView, QRubberBand


class Viewer(QGraphicsView):
    rectChanged = pyqtSignal(QRect)

    def __init__(self, parent):
        super(Viewer, self).__init__(parent)
        self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)

        # define the Rect Items if exit
        self.rect_item_list = []

        # define the inked die shape search algorithm
        self.search_shape = "Around"

        # define the search Bin number
        self.searchNearestN = 1

        # mouse drag select item to ink off
        self.changeRubberBand = False


        self._zoom = 0
        self._empty = True
        # self._scene = QGraphicsScene(self)

        # define the ink off color, default color is white
        self.ink_off_color = QColor("#FFFFFF")

        # is ink off mode on
        self._is_inkoff_mode_on = False

        # is_rubber band mode
        self._is_rubberband_mode = False

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


    # def hoverChange(self):
    #     """
    #     hover on the item for the Cursor
    #     :return:
    #     """
    #     self.viewport().setCursor(Qt.PointingHandCursor)
    #
    # def notHoverChange(self):
    #     self.viewport().setCursor(Qt.ArrowCursor)
    #
    # def mousePressEvent(self, event):
    #     if event.button() == Qt.LeftButton and (not self._is_click_mode):
    #         self.origin = event.pos()
    #         self.rubberBand.setGeometry(QRect(self.origin, QSize()))
    #         self.rectChanged.emit(self.rubberBand.geometry())
    #         self.rubberBand.show()
    #         self.changeRubberBand = True
    #         return
    #         # QGraphicsView.mousePressEvent(self,event)
    #     elif event.button() == Qt.MidButton:
    #         self.viewport().setCursor(Qt.ClosedHandCursor)
    #         self.original_event = event
    #         handmade_event = QMouseEvent(
    #             QEvent.MouseButtonPress,
    #             QPointF(event.pos()),
    #             Qt.LeftButton,
    #             event.buttons(),
    #             Qt.KeyboardModifiers(),
    #         )
    #         QGraphicsView.mousePressEvent(self, handmade_event)
    #
    #     super(Viewer, self).mousePressEvent(event)
    #
    # def mouseReleaseEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         self.changeRubberBand = False
    #         if self.rubberBand.isVisible():
    #             self.rubberBand.hide()
    #             rect = self.rubberBand.geometry()
    #             rect_scene = self.mapToScene(rect).boundingRect()
    #             selected_items = self.scene().items(rect_scene)
    #             # get all the item
    #             if self._is_rubberband_mode:
    #                 if selected_items:
    #                     # self.markNearestBins(selected_items=selected_items, search_type="ink all")
    #                     self.markNearestBins(selected_items=selected_items)
    #                     self.countInkedDies()
    #
    #         QGraphicsView.mouseReleaseEvent(self, event)
    #     elif event.button() == Qt.MidButton:
    #         self.viewport().setCursor(Qt.ArrowCursor)
    #         handmade_event = QMouseEvent(
    #             QEvent.MouseButtonRelease,
    #             QPointF(event.pos()),
    #             Qt.LeftButton,
    #             event.buttons(),
    #             Qt.KeyboardModifiers(),
    #         )
    #         QGraphicsView.mouseReleaseEvent(self, handmade_event)
    #     super(Viewer, self).mouseReleaseEvent(event)
    #
    # def mouseMoveEvent(self, event):
    #     if self.changeRubberBand:
    #         self.rubberBand.setGeometry(
    #             QRect(self.origin, event.pos()).normalized()
    #         )
    #         self.rectChanged.emit(self.rubberBand.geometry())
    #         QGraphicsView.mouseMoveEvent(self, event)
    #     super(Viewer, self).mouseMoveEvent(event)
    #
    # def rubberBandModeOn(self, rubberband_mode):
    #     """
    #     customized ink off mode if selected
    #     create a ink_off_list, if ink off list is not none, create ink off
    #     :return:
    #     """
    #     # if self._is_rubberband_mode:
    #     #     self._is_rubberband_mode = False
    #     # else:
    #     #     self._is_rubberband_mode = True
    #     if self._is_inkoff_mode_on:
    #         self._is_rubberband_mode = rubberband_mode
    #
    # def clickItemModeOn(self, click_mode):
    #     """
    #     set the mouse tracking and interaction
    #     allow the mouse click single item in graphicview
    #     :return:
    #     """
    #     if self._is_inkoff_mode_on:
    #         self._is_click_mode = click_mode
    #
    #         # self.setDragMode(self.RubberBandDrag if self._is_drag else self.ScrollHandDrag)
    #         self.setInteractive(self._is_click_mode)
    #         # self.setMouseTracking(self._is_click_mode)
    #
    # def clickRemoveModeOn(self, remove_mode):
    #     """
    #     remove_mode is Ture, the rubberBand select item covert the ink dies to un-ink
    #     :param remove_mode:
    #     :return:
    #     """
    #     if self._is_inkoff_mode_on:
    #         self._is_remove_ink_from_rubberBand = remove_mode
    #
    # def changeInkOffColorDie(self, changed_color):
    #     """
    #     the default ink off color need to changed
    #     the plotted dies color need to change by query the item for the scene
    #     :return:
    #     """
    #     self.ink_off_color = QColor(changed_color)
    #     items = self.scene().items()
    #     if items:
    #         for item in items:
    #             if item.name not in ["waferFrame", "titleName", "polygon_selector"]:
    #                 item.inked_color = QColor(changed_color)
    #
    # def autoInkOff(self, bin_list):
    #     """
    #     auto ink off the entire map by select items
    #     :return:
    #     """
    #     if len(bin_list) == 0:
    #         return
    #     else:
    #         # auto ink off the bin list
    #         select_item_list = []
    #         for item in self.scene().items():
    #             if item.name not in ["waferFrame", "titleName", "polygon_selector"]:
    #                 if item.bin_number in bin_list:
    #                     select_item_list.append(item)
    #
    #         if len(select_item_list) != 0:
    #             self.markNearestBins(selected_items=select_item_list)
    #             self.countInkedDies()
    #
    # def addPolygonSelector(self, add_polygon, polygon_props):
    #     """
    #     triggered to add or remove the polygon item
    #     :return:
    #     """
    #     # rect = self.rubberBand.geometry()
    #     # rect_scene = self.mapToScene(rect).boundingRect()
    #     # selected_items = self.scene().items(rect_scene)
    #
    #     sides = polygon_props["grip_number"]
    #     r = polygon_props["polygon_radius"]
    #     if add_polygon:
    #         self.polygon_item = PolygonAnnotation(polygon_props=polygon_props)
    #         # self.polygon_item.setBoundingRegionGranularity()
    #         self.polygon_item.polygon_signal.start_polygon_inking_signal.connect(self.doubleClickPolygonInk)
    #         self.scene().addItem(self.polygon_item)
    #         for i in range(sides):
    #             angle = 2 * math.pi * i / sides
    #             x = r * math.cos(angle)
    #             y = r * math.sin(angle)
    #             p = QPointF(x, y) + QPointF(0, 0)
    #             self.polygon_item.addPoint(p)
    #     else:
    #         # remove base the item name
    #         for item in self.scene().items():
    #             if item.name == "polygon_selector":
    #                 self.scene().removeItem(item)
    #
    # def doubleClickPolygonInk(self):
    #     """
    #     double click the polygon item if exist,
    #     ink off based on selection mode
    #     self.polygon_item use the QGraphicPolygonItem.shape() to find the items in the shape
    #     *** Must to use the self.polygon_item.mapToScene to get the relative location
    #     :return:
    #     """
    #     # if exit polygon item, check the scene
    #     if self.polygon_item:
    #         self.polygon_item.prepareGeometryChange()
    #         self.polygon_item.update()
    #         shape = self.polygon_item.shape()
    #         # todo: must to use the polygon_item it self mapToScene to covert
    #         rect_scene = self.polygon_item.mapToScene(shape)
    #         selected_item = self.scene().items(rect_scene)
    #         if selected_item:
    #             # self.markNearestBins(selected_items=selected_items, search_type="ink all")
    #             self.markNearestBins(selected_items=selected_item)
    #             self.countInkedDies()
    #
    # def inkOffModeOn(self, is_mode):
    #     """
    #     _is_inkoff_mode_on global control all other mode
    #     such as click ink off mode and rubber band select mode
    #     :param is_mode:
    #     :return:
    #     """
    #     self._is_inkoff_mode_on = is_mode
    #
    # def markNearestBins(self, selected_items):
    #     """
    #         #
    #         #        (x, y)
    #         #      /
    #         #  (x-N, y-N)
    #     set the rules for bin area select
    #     :param selected_items:
    #     :return:
    #     """
    #     if self.search_shape == "All":
    #         for child in selected_items:
    #             # avoid the wafer circle item
    #             if child.name not in ["waferFrame", "titleName", "polygon_selector"]:
    #                 if not self._is_remove_ink_from_rubberBand:
    #                     if child.ink_flag != 0 and child.ink_flag == 1:
    #                         # Rect Item change ink or un-ink  1 or 2
    #                         # use child.ink_flag = 1 condition to avoid the click inked dies
    #                         child.markInkChange()
    #                         child.setBrush(self.ink_off_color)
    #                 else:
    #                     if child.ink_flag != 0 and child.ink_flag == 2:
    #                         # find the orignal color
    #                         # orignal_color = child.color
    #                         child.markInkChange()
    #                         child.setBrush(child.color)
    #     elif self.search_shape == "Around":
    #         N = self.searchNearestN
    #         mark_item_list = []
    #         for child in selected_items:
    #             # use the ink flag == 0 to restrict the item that can only select by one
    #             if child.name not in ["waferFrame", "titleName", "polygon_selector"] and child.ink_flag == 0:
    #                 x_start = child.x_label-N
    #                 y_start = child.y_label-N
    #                 for i in range(0, 2*N+1):
    #                     x = x_start+i
    #                     for j in range(0, 2*N+1):
    #                         y = y_start + j
    #                         coord = (x, y)
    #                         mark_item_list.append(coord)
    #         # remove the duplicates coordinate
    #         mark_item_list = list(set(mark_item_list))
    #
    #         for child in self.scene().items():
    #             if child.name not in ["waferFrame", "titleName", "polygon_selector"]:
    #                 if child.ink_flag != 0 and child.ink_flag == 1:
    #                     current_label = (child.x_label, child.y_label)
    #                     if current_label in mark_item_list:
    #                         child.markInkChange()
    #                         child.setBrush(self.ink_off_color)
    #     elif self.search_shape == "Cross":
    #         N = self.searchNearestN
    #         mark_item_list = []
    #         for child in selected_items:
    #             if child.name not in ["waferFrame", "titleName", "polygon_selector"] and child.ink_flag == 0:
    #                 x_start = child.x_label
    #                 y_start = child.y_label
    #                 for i in range(0, N+1):
    #                     coord1 = (x_start + i, y_start)
    #                     coord2 = (x_start - i, y_start)
    #                     coord3 = (x_start, y_start + i)
    #                     coord4 = (x_start, y_start - i)
    #                     mark_item_list.extend([coord1, coord2, coord3, coord4])
    #
    #         mark_item_list = list(set(mark_item_list))
    #
    #         for child in self.scene().items():
    #             if child.name not in ["waferFrame", "titleName", "polygon_selector"]:
    #                 if child.ink_flag != 0 and child.ink_flag == 1:
    #                     current_label = (child.x_label, child.y_label)
    #                     if current_label in mark_item_list:
    #                         child.markInkChange()
    #                         child.setBrush(self.ink_off_color)
    #     elif self.search_shape == "Corner":
    #         N = self.searchNearestN
    #         mark_item_list = []
    #         for child in selected_items:
    #             if child.name not in ["waferFrame", "titleName", "polygon_selector"] and child.ink_flag == 0:
    #                 x_start = child.x_label
    #                 y_start = child.y_label
    #                 for i in range(0, N+1):
    #                     coord1 = (x_start + i, y_start + i)
    #                     coord2 = (x_start - i, y_start - i)
    #                     coord3 = (x_start + i, y_start - i)
    #                     coord4 = (x_start - i, y_start + i)
    #                     mark_item_list.extend([coord1, coord2, coord3, coord4])
    #
    #         mark_item_list = list(set(mark_item_list))
    #
    #         for child in self.scene().items():
    #             if child.name not in ["waferFrame", "titleName", "polygon_selector"]:
    #                 if child.ink_flag != 0 and child.ink_flag == 1:
    #                     current_label = (child.x_label, child.y_label)
    #                     if current_label in mark_item_list:
    #                         child.markInkChange()
    #                         child.setBrush(self.ink_off_color)
    #
    # def downloadInkOffFile(self, path, lot_id, wafer_number, vendor_scribe, format_type='BTF'):
    #     """
    #     Download the inked files
    #     format as
    #     DIE X, DIE Y
    #     :return:
    #     """
    #     die_x = []
    #     die_y = []
    #     file_name = file_name = lot_id + "__" + "W"+str(wafer_number) + "__" + vendor_scribe + ".csv"
    #
    #     for item in self.scene().items():
    #         if item.name not in ["waferFrame", "titleName", "polygon_selector"]:
    #             if item.ink_flag == 2:
    #                 die_x.append(item.x_label)
    #                 die_y.append(item.y_label)
    #     try:
    #         if len(die_x) != 0:
    #             lot_list = [lot_id]*len(die_x)
    #             wafer_list = [wafer_number]*len(die_x)
    #             vendor_list = [vendor_scribe]*len(die_x)
    #             # print(format_type)
    #             # format decide by format type
    #             if format_type == 'BTF':
    #                 df = pd.DataFrame(
    #                     {
    #                         "PARENT_LOT": lot_list,
    #                         "WAFER": wafer_list,
    #                         "SCRIBE": vendor_list,
    #                         "SORT_X": die_x,
    #                         "SORT_Y": die_y
    #                     }
    #                 )
    #             elif format_type == 'OSAT':
    #                 df = pd.DataFrame(
    #                     {
    #                         "LOT_ID": lot_list,
    #                         "WAFER": wafer_list,
    #                         "SCRIBE": vendor_list,
    #                         "DIE_X": die_x,
    #                         "DIE_Y": die_y
    #                     }
    #                 )
    #             file_path = os.path.join(path, file_name)
    #             # print(file_path)
    #             if os.path.exists(file_path):
    #                 # print("exit file", file_path)
    #                 create_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    #                 file_name = lot_id + "__" + "W" + str(wafer_number) + "__" + vendor_scribe + " " + create_time + ".csv"
    #                 file_path = os.path.join(path, file_name)
    #                 # print("new file name ", file_path)
    #             df.to_csv(file_path, index=False)
    #     except Exception as e:
    #         print("Error Download CSV")
    #         print(e)
    #         pass
    #
    # def downloadImageFile(self, path, lot_id, wafer_number, vendor_scribe, dpi=None):
    #     """
    #     download the image files
    #     :return:
    #     """
    #     try:
    #         file_name = lot_id + "__" + "W"+str(wafer_number) + "__" + vendor_scribe + ".png"
    #
    #         file_path = os.path.join(path, file_name)
    #         if os.path.exists(file_path):
    #             create_time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    #             file_name = lot_id + "__" + "W" + str(wafer_number) + "__" + vendor_scribe + " " + create_time + ".png"
    #             file_path = os.path.join(path, file_name)
    #
    #         # self.update()
    #         # update the total ink bins
    #         self.scale(0.9, 0.9)
    #         self.scale(1.1, 1.1)
    #         rect = self.viewport().rect()
    #         image = QImage(rect.size(), QImage.Format_A2BGR30_Premultiplied)
    #         # image = image.scaled(1, -1)
    #         painter = QPainter(image)
    #         self.render(painter)
    #         if dpi is not None:
    #             dpm = dpi/0.0254
    #             image.setDotsPerMeterX(dpm)
    #             image.setDotsPerMeterY(dpm)
    #         image.save(file_path)
    #         # must include the painter.end
    #         painter.end()
    #     except Exception as e:
    #         print(e)
    #         print("Error, Cannot save image")
    #
    # def countInkedDies(self):
    #     """
    #     count total how many dies inked based on the action select
    #     :return:
    #     """
    #     items = self.scene().items()
    #     total_ink_number = 0
    #     if items:
    #         for item in items:
    #             if item.name not in ["waferFrame", "titleName", "polygon_selector"]:
    #                 if item.ink_flag == 2:
    #                     total_ink_number += 1
    #             if item.name == "titleName":
    #                 current_text = item.toPlainText()
    #                 if "Ink Counts" in current_text:
    #                     # eixt the counts number, split the string and update it
    #                     current_text = current_text.splitlines()[0]
    #                 text_item = item
    #         if total_ink_number != 0:
    #             current_text = current_text + "\nInk Counts:     %d"%total_ink_number
    #             text_item.setPlainText(current_text)
    #
    # def addColorBar(self, col_start, col_stop, add_bar=True, contrast_amplifier=1):
    #     """
    #     add color bar on the graphics view and text on the color bar
    #          _
    #     1   |_|
    #     0.8 |_|
    #     0.5 |_|
    #     0.2 |_|
    #     0.1 |_|
    #     :param col_start:
    #     :param col_stop:
    #     :param add_bar:
    #     :param contrast_amplifier:
    #     :return:
    #     """
    #     color_start = QColor.fromRgb(col_start[0], col_start[1], col_start[2])
    #     color_stop = QColor.fromRgb(col_stop[0], col_stop[1], col_stop[2])
    #     if add_bar:
    #         # clear the color bar first
    #         try:
    #             for item in self.scene().items():
    #                 if item.name == "ColorBarItem":
    #                     self.scene().removeItem(item)
    #         except Exception as e:
    #             print("ColorBarItem No Name: ", e)
    #
    #         try:
    #             pos_x, pos_y, width, height = 180, -100, 10, 200
    #             self.colorBar_item = ColorBarItem(x=pos_x, y=pos_y, width=width, height=height,
    #                                               start_color=color_start, end_color=color_stop)
    #             self.colorBar_item.fillColorRectangle()
    #             self.scene().addItem(self.colorBar_item)
    #
    #             # add the cursor on the color bar, text increase by the size on the color bar
    #             size = 10
    #             for i in range(0, size+1, 1):
    #                 if contrast_amplifier == 1:
    #                     text_content = "%.1f-" % (i * 0.1 / contrast_amplifier)
    #                     font_size = 6
    #                 else:
    #                     text_content = "%.3f-" % (i * 0.1 / contrast_amplifier)
    #                     font_size = 4
    #                 text_pos_y = pos_y-10 + 20*(i+1)
    #                 text_item = TextItem(name="ColorBarItem", x=pos_x-2*width, y=text_pos_y, text_content=text_content,
    #                                      font_size=font_size)
    #                 self.scene().addItem(text_item)
    #
    #         except Exception as e:
    #             print("Cannot add color bar: ", e)
    #     else:
    #         # remove base the item name
    #         try:
    #             for item in self.scene().items():
    #                 if item.name == "ColorBarItem":
    #                     self.scene().removeItem(item)
    #         except Exception as e:
    #             print("Cannot remove Color Bar Item ", e)



