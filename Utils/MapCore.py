from PyQt5.QtCore import *
from PyQt5.QtGui import QPen, QColor
from PyQt5.QtWidgets import QGraphicsRectItem

from Widgets import EllipseItem, RectItem


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