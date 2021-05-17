from PyQt5.QtCore import *
from PyQt5.QtGui import QPen, QColor
from PyQt5.QtWidgets import QGraphicsRectItem

from Widgets import EllipseItem, RectItem, TextItem


class SortMap():

    def __init__(self, ucs_map_df, scene, layout_props=None, title_props=None):
        """

        :param ucs_map_df:
        :param scene:
        :param wafer_info:
        :param props: properties of the wafer layout and die properties
        ":param title_props: properties of the wafer title setting
        """
        super(SortMap, self).__init__()

        if layout_props is None:
            layout_props = {'die_line_type': Qt.SolidLine,
                            'die_line_color': QColor(255, 255, 255),
                            'die_line_width': 2,
                            'die_default_color': Qt.white,
                            'die_cosmetic': True,
                            'show_pass_die': False,
                            'show_flash_die': False,
                            'wafer_background_color': QColor(132, 132, 132, 90)}

        if title_props is None:
            title_props = {
                'show_wafer_title': True,
                'wafer_title': "Wafer ID:    ",
                'wafer_title_font': 8,
                'wafer_title_pos_x': -55,
                'wafer_title_pos_y': 180,
            }

        # define the ucs map data
        self.ucs_map_df = ucs_map_df
        # self.graphicView = self.graphicView
        self.scene = scene

        self.layout_props = layout_props

        self.title_props = title_props

        self.graphic_item_dict = {}

        # dict to store if title exist or not exist
        self.wafer_title_dict = {"Title_Exist": False, "Title_Item": None}

    def update_wafer_title(self):
        """
        create the wafer title
        :return:
        """

        if self.title_props['show_wafer_title']:
            if not self.wafer_title_dict['Title_Exist']:
                wafer_title_item = TextItem(name="Wafer_Title_Item")
                self.wafer_title_dict['Title_Exist'] = True
                self.wafer_title_dict['Title_Item'] = wafer_title_item
                self.scene.addItem(wafer_title_item)
            else:
                wafer_title_item = self.wafer_title_dict["Title_Item"]

            wafer_title_item.setPos(self.title_props['wafer_title_pos_x'], self.title_props['wafer_title_pos_y'])
            wafer_title_item.setPlainText(self.title_props['wafer_title'])
            wafer_title_item.resetFontSize(font_size=self.title_props['wafer_title_font'])
        else:
            if not self.wafer_title_dict['Title_Exist']:
                return
            else:
                item = self.wafer_title_dict['Title_Item']
                self.wafer_title_dict['Title_Item'] = None
                self.scene().removeItem(item)
                self.wafer_title_dict['Title_Exist'] = False



    def create_wafer_map(self):
        """

        +------+------+-------------+-------------+------------+-----------|---------- |--------|---------+---------+
        |DIE_ORIGIN_X |DIE_ORIGIN_Y | DIE_SIZE_X  |DIE_SIZE_Y  |SORT_DIE_X |SORT_DIE_Y |FLASH_X | FLASH_Y |TEST FLAG
        |------+------+-------------+-------------+------------+-----------|---------- |--------|-------- +---------+
        |    -112.008 |      66.372 |        6223 |       5098 |    0      |    1      |   5    |    3    |   T     |
        |    -105.785 |      40.882 |        6223 |       5098 |    1      |    2      |   5    |    3    |   P     |
         ------------------------------------------------------------------------------------------------------------

        DIE_X

        :param ucs_map_df:
        :param graphicView:
        :param scene: graphic scene where put the plot
        :param wafer_info: current only wafer id, can be show count number, lot id, etc
        :param show_pass_die: determine if need to show the passed dies
        :param show_flash_die: determine if need to show the flash die
        :param die_props: die properties for plot Rect
        :return:
        """

        show_pass_die = self.layout_props["show_pass_die"]
        show_flash_die = self.layout_props['show_flash_die']

        if not show_pass_die:
            ucs_map_df_filter = self.ucs_map_df[self.ucs_map_df ["TEST_FLAG"] == 'T']
        else:
            ucs_map_df_filter = self.ucs_map_df

        # convert to numpy data structure
        data = ucs_map_df_filter.to_numpy()

        # clear the scene
        self.scene.clear()
        # reset the wafer title setting
        self.wafer_title_dict = {"Title_Exist": False, "Title_Item": None}
        factor = 0.001

        pen = QPen(self.layout_props['die_line_type'])
        pen.setWidth(self.layout_props['die_line_width'])
        pen.setColor(self.layout_props['die_line_color'])
        pen.setCosmetic(self.layout_props['die_cosmetic'])


        for row_index, row in enumerate(data):
            graphic_item = RectItem(x=row[0], y=row[1], width=row[2], height=row[3],
                                    color=self.layout_props['die_default_color'], name='Die_Item')
            graphic_item.setPen(pen)

            tool_tip = '''<h5>Sort (X, Y): ({}, {}) <hr>
                              BIN_NUMBER:
                          </h5>'''.format(str(int(row[6])), str(int(row[7])))

            graphic_item.setToolTip(tool_tip)
            graphic_item.setCacheMode(QGraphicsRectItem.DeviceCoordinateCache)
            self.scene.addItem(graphic_item)
            self.graphic_item_dict.update({(row[4], row[5]): graphic_item})

        # issue for wafer from layout
        # todo: if Pass Die show in layout, then need to set the wafer frame on top, otherwise,
        # todo: the test map too big and cannot see the wafer layout. Not a best solution so far

        if show_pass_die:
            wafer_frame = EllipseItem(x=-150, y=-150, width=300, height=300, name='Wafer_Item')
        else:
            wafer_frame = EllipseItem(x=-150, y=-150, width=300, height=300,
                                      bg_color=self.layout_props['wafer_background_color'], name='Wafer_Item')

        self.scene.addItem(wafer_frame)

        self.update_wafer_title()
        # scene.addItem
        # text_item = None

    def updateWaferMap(self, bin_data):
        """
        graphic_item_dict
        {
            (sort_x_1, sort_y_1) : graphic_item_1;
            (sort_x_2, sort_y_2) : graphic_item_2;
        }
        update the wafer map sort info based on the bin data
        :param bin_data: dataframe with each die coordinate and bin number info
        :return:
        """

        if bin_data.empty:
            return

        # key_list = list(self.graphic_item_dict.keys())
        if not bin_data.empty:
            color_list = bin_data["BIN_COLOR"].tolist()
            # data.loc[:, 'COLOR_DIE'] = ""
            bin_data['COLOR_DIE'] = list(zip(bin_data["DIE_X"], bin_data["DIE_Y"]))
            # die_x_list = data["DIE_X"].tolist()
            # die_y_list = data["DIE_Y"].tolist()
            key_list = list(self.graphic_item_dict.keys())
            data_list = bin_data["COLOR_DIE"].tolist()
            # cols = ['DIE_X', 'DIE_Y', 'BIN_NUMBER', "BIN_TYPE"]
            X_COORDINATE = bin_data["DIE_X"].tolist()
            Y_COORDINATE = bin_data["DIE_Y"].tolist()
            BIN_NUMBER = bin_data["BIN_NUMBER"].tolist()
            BIN_TYPE = bin_data["BIN_TYPE"].tolist()
            INK_FLAG = bin_data["INK_FLAG"].tolist()

            for item_name in key_list:
                if item_name in data_list:
                    # change color of die
                    # find the index of this coordinate
                    index = data_list.index(item_name)
                    self.graphic_item_dict[item_name].setBrush(QColor(color_list[index]))
                    # assign the color from the callbackRectItem
                    self.graphic_item_dict[item_name].color = QColor(color_list[index])
                    # assign the ink flag number to the callbackRectItem
                    self.graphic_item_dict[item_name].ink_flag = INK_FLAG[index]
                    # assign the bin number into the graphic_item
                    self.graphic_item_dict[item_name].bin_number = BIN_NUMBER[index]
                    tool_tip = '''<h5>SORT_DIE: ({}), ({})<hr>Bin Type: {}<hr>Bin Number: {}</h5>'''.format(
                        str(X_COORDINATE[index]), str(Y_COORDINATE[index]), str(BIN_TYPE[index]),
                        str(BIN_NUMBER[index]))
                    self.graphic_item_dict[item_name].setToolTip(tool_tip)
                else:
                    self.graphic_item_dict[item_name].setBrush(Qt.white)

        # use the filter is slow, use the index way if faster


        # for item_name in key_list:
        #     filter_bin_data = bin_data[(bin_data['DIE_X']==item_name[0])& (bin_data['DIE_Y']==item_name[1])].to_dict('list')
        #     if len(filter_bin_data['BIN_NUMBER']) != 0:
        #         color = filter_bin_data['BIN_COLOR'][0]
        #         bin_type = filter_bin_data['BIN_TYPE'][0]
        #         ink_flag = filter_bin_data['INK_FLAG'][0]
        #         bin_number = filter_bin_data['BIN_NUMBER'][0]
        #         self.graphic_item_dict[item_name].setBrush(QColor(color))
        #         # assign the color from the callbackRectItem
        #         self.graphic_item_dict[item_name].color = QColor(color)
        #         # assign the ink flag number to the callbackRectItem
        #         self.graphic_item_dict[item_name].ink_flag = ink_flag
        #         # assign the bin number into the graphic_item
        #         self.graphic_item_dict[item_name].bin_number = bin_number
        #         # assign die info to tool tip
        #         tool_tip = '''<h5>SORT_DIE: ({}), ({})<hr>Bin Type: {}<hr>Bin Number: {}</h5>'''.format(
        #             str(item_name[0]), str(item_name[1]), str(bin_type), str(bin_number))
        #         self.graphic_item_dict[item_name].setToolTip(tool_tip)
        #     else:
        #         self.graphic_item_dict[item_name].setBrush(Qt.white)


def create_wafer_map(ucs_map_df, graphicView, scene, wafer_info, show_pass_die=False, die_props=None):
    """
    +------+------+-------------+-------------+------------+-----------|----------|-----------|----------+
    |DIE_X |DIE_Y |DIE_ORIGIN_X |DIE_ORIGIN_Y | DIE_SIZE_X |DIE_SIZE_Y |SORT_DIE_X|SORT_DIE_Y | TEST FLAG|
    |------+------+-------------+-------------+------------+-----------|----------|-----------|----------+
    |  -14 |   17 |     -112008 |       66372 |       6223 |      5098 |   0      |    1      |  P       |
    |  -13 |   12 |     -105785 |       40882 |       6223 |      5098 |   1      |    2      |  T       |

    :param ucs_map_df:
    :param graphicView:
    :param scene: graphic scene where put the plot
    :param wafer_info: current only wafer id, can be show count number, lot id, etc
    :param show_pass_die: determine if need to show the passed dies
    :param die_props: die properties for plot Rect
    :return:
    """
    if not show_pass_die:
        ucs_map_df = ucs_map_df[ucs_map_df["TEST_FLAG"] == 'T']

    # convert to numpy data structure
    data = ucs_map_df.to_numpy()

    if die_props is None:
        die_props = {'line_type': Qt.SolidLine,
                     'line_color': QColor(255, 0, 0, 90),
                     'line_width': 0,
                     'is_cosmetic': True}

    scene.clear()

    graphic_item_dict = {}
    factor = 0.001

    pen = QPen(die_props['line_type'])
    pen.setWidth(die_props['line_width'])
    pen.setCosmetic(die_props['is_cosmetic'])
    pen.setColor(die_props['line_color'])

    for row_index, row in enumerate(data):
        graphic_item = RectItem(x=row[2] * factor,
                                y=row[3] * factor,
                                x_label=row[6],
                                y_label=row[7],
                                width=row[4] * factor,
                                height=row[5] * factor,
                                color=Qt.red)

        graphic_item.setPen(pen)
        item_name = str(int(row[6])) + " " + str(int(row[7]))

        tool_tip = '''<h5>Sort_DIE: ({}), ({})
                    <hr>
                    Bin Type: <hr>
                    <hr>
                    </h5>'''.format(str(int(row[6])), str(int(row[7])))
        graphic_item.setToolTip(tool_tip)
        # graphic_item.setFlags(QGraphicsRectItem.ItemIsSelectable)
        graphic_item.setCacheMode(QGraphicsRectItem.DeviceCoordinateCache)
        # set the hover signal
        # graphic_item.log.hovered.connect()
        # graphic_item.setSelected()
        scene.addItem(graphic_item)
        graphic_item_dict.update({item_name: graphic_item})

    # issue for wafer from layout
    # todo: if Pass Die show in layout, then need to set the wafer frame on top, otherwise,
    # todo: the test map too big and cannot see the wafer layout. Not a best solution so far

    if show_pass_die:
        wafer_frame = EllipseItem(x=-150, y=-150, width=300, height=300)
    else:
        wafer_frame = EllipseItem(x=-150, y=-150, width=300, height=300, bg_color=QColor(248, 249, 249))

    scene.addItem(wafer_frame)

    # text_item = TextItem(name="titleName")
    # text_item.setPlainText(wafer_info)
    # scene.addItem(text_item)

    # scene.addItem
    text_item = None

    return graphic_item_dict, text_item