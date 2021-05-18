__Author__ = """By: Ethan Jian Qiu Email: Ethan.qiujian@gmail.com"""
__Copyright__ = "Copyright (c) 2021 Ethan Jian Qiu"
__Version__ = "Version 1.0"

import sys
import pandas as pd
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
# from PySide2.QtWidgets import QMainWindow, QApplication
from UI.MainWindow import Ui_MainWindow
from Utils import convert_data_to_dict, SortMap
from Dialog import ShowWaferItemDialog, ShowWaferSettingDialog

class myApp(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.resize(600, 600)

        # define the Bin Information
        self.bin_info_dict = {}
        # define the Sort bin map
        self.bin_map_dict = {}
        # define bin data
        self.bin_data = pd.DataFrame()
        # define the ucs map and initial the map and ucs_info
        self.ucs_map = pd.DataFrame()
        self.ucs_info = pd.DataFrame()

        # Initialize scene and graphicView setting
        self.scene = QGraphicsScene()
        self.scene_text_item = None
        self.graphicsView.setScene(self.scene)
        # self.graphicsView.scale(1.5, 1.5)
        # self.scene.setSceneRect(-200, -200, 400, 400)

        # self.graphicsView.setScene(self.scene)
        self.graphicsView_save_path = os.path.abspath(".")

        # define the graphic item dictionary to store each plot item data
        self.graphics_item_dict = {}
        self.scene_text_item = None

        # create the dialog for wafer setting
        self.wafer_setting_dialog = ShowWaferSettingDialog()
        self.wafer_setting_dialog.wafer_layout_changed.connect(self.updateWaferLayoutSetting)
        self.wafer_setting_dialog.wafer_title_changed.connect(self.updateWaferTitleSetting)
        self.wafer_setting_dialog.die_props_changed.connect(self.updateDieSetting)

        # create the dialog for wafer selection
        self.wafer_select_dialog = ShowWaferItemDialog()
        self.wafer_select_dialog.select_item.connect(self.updateWaferSortMap)
        # self.wafer_select_dialog.select_bin.connect(self.updateWaferSortMap)

        # initial ink off setting in QGraphic View
        # self.graphicsView.ink_off_color = QColor(self.comboBox_inkoff_color.currentText())
        # self.die_edge_color = QColor(0, 0, 0, 90)

        # action button
        self.action_Map_Setting.triggered.connect(self.showWaferSettingDialog)
        self.action_Lot_Dialog.triggered.connect(self.showWaferSelectDialog)
        self.action_Zoom_In.triggered.connect(lambda : self.graphicsView.zoomMap(factor=1.1))
        self.action_Zoom_Out.triggered.connect(lambda : self.graphicsView.zoomMap(factor=0.9))
        self.action_Rotation_Left.triggered.connect(lambda : self.graphicsView.rotateMap(angle=-15))
        self.action_Rotation_Right.triggered.connect(lambda : self.graphicsView.rotateMap(angle=15))

        # create the sort map class
        self.sort_map = SortMap(ucs_map_df=self.ucs_map, scene=self.scene)

        self.testGraphicPlot()

        self.testLotTableWidget()

    def showWaferSettingDialog(self):
        """
        show dialog for wafer layout setting
        :return:
        """
        self.wafer_setting_dialog.show()

    def showWaferSelectDialog(self):
        """
        show dialog
        :return:
        """
        if self.action_Lot_Dialog.isChecked():
            self.wafer_select_dialog.show()
        else:
            self.wafer_select_dialog.hide()

    # def updatewaferSortMap

    def updateWaferLayoutSetting(self, setting_props):
        """
        update the wafer map based on the Setting Dialog Emit dictionary
        :param setting_props: dictionary with both layout and die
        {
            "layout_props": dict,
            "die_props": dict
        }
        :return:
        """
        self.sort_map.layout_props = setting_props['layout_props']
        self.sort_map.die_props = setting_props['die_props']
        self.sort_map.createWaferSortMap()
        # self.sort_map.updateDieProps()

    def updateDieSetting(self, die_props):
        self.sort_map.die_props = die_props
        self.sort_map.updateDieProps()

    def updateWaferTitleSetting(self, title_props):
        """
        update the wafer title based on the setting dialog emit dictionary
        :param title_props:
        :return:
        """
        self.sort_map.title_props = title_props
        self.sort_map.updateWaferTitle()

    def updateWaferSortMap(self, wafer_info):
        """
        update the wafer map based on select item
        :param wafer_info: list type, ('lot_id_1', 'wafer_alias_1'), use to filter the bin data

        :return:
        """
        # filter by click info
        if self.bin_data.empty:
            return
        else:
            self.current_wafer_df = self.bin_data[self.bin_data['LOT_ID'].isin(wafer_info['LOT_ID']) & self.bin_data['VENDOR_SCRIBE'].isin(wafer_info['VENDOR_SCRIBE']) & self.bin_data['BIN_NUMBER'].isin(wafer_info['BIN_NUMBER'])]
            self.sort_map.updateWaferMap(bin_data=self.current_wafer_df)


    def testGraphicPlot(self):
        # todo: create a funtion to detect if data column names contians the names required
        # todo: create a fake UCS data for later test
        df = pd.read_csv(r"/Users/JianQiu/Dropbox/pythonprojects/SortMap/SampleData/ucs_data.csv")
        df.loc[:, "DIE_ORIGIN_X"] = df["DIE_ORIGIN_X"].apply(lambda x: x*0.001)
        df.loc[:, "DIE_ORIGIN_Y"] = df["DIE_ORIGIN_Y"].apply(lambda y: y*0.001)
        df.loc[:, "DIE_SIZE_X"] = df["DIE_SIZE_X"].apply(lambda x: x*0.001)
        df.loc[:, "DIE_SIZE_Y"] = df["DIE_SIZE_Y"].apply(lambda y: y*0.001)

        # self.ucs_map = df[["DIE_X","DIE_Y","DIE_ORIGIN_X","DIE_ORIGIN_Y","DIE_SIZE_X","DIE_SIZE_Y","SORT_DIE_X","SORT_DIE_Y", "TEST_FLAG"]]
        # print(self.ucs_map)

        # die_props = {'line_type': Qt.SolidLine,
        #              'line_color': QColor(0, 0, 0, 90),
        #              'line_width': 0,
        #              'is_cosmetic': True}

        # self.graphics_item_dict, self.scene_text_item = create_wafer_map(ucs_map_df=self.ucs_map,
        #                                                                  graphicView=self.graphicsView,
        #                                                                  scene=self.scene,
        #                                                                  wafer_info="Wafer",
        #                                                                  show_pass_die=False,
        #                                                                  die_props=die_props)
        self.sort_map.ucs_map_df = df[["DIE_ORIGIN_X","DIE_ORIGIN_Y","DIE_SIZE_X","DIE_SIZE_Y","SORT_DIE_X","SORT_DIE_Y", "FLASH_X", "FLASH_Y", "TEST_FLAG"]]
        # self.sort_map.layout_props = die_props
        self.sort_map.createWaferSortMap()


        # print(self.graphics_item_dict)


    def testLotTableWidget(self):
        # todo: create function to detect if import data contians the columns name
        df = pd.read_csv(r"/Users/JianQiu/Dropbox/pythonprojects/SortMap/SampleData/bin_data.csv")
        df_bin_group = pd.read_csv(r"/Users/JianQiu/Dropbox/pythonprojects/SortMap/SampleData/bin_group.csv")
        data_dict = convert_data_to_dict(data=df, groupby_list=['LOT_ID'], subset_list=["VENDOR_SCRIBE",
                                                                                        "WAFER_NUMBER"])

        bin_group_data_dict = convert_data_to_dict(data=df_bin_group, groupby_list=['LAYER_ORDER', 'BIN_GROUP', 'BIN_COLOR'],
                                                   subset_list=['BIN_NUMBER', 'BIN_DESC'])
        # print(data_dict['8R05778.054'])
        # lot = list(data_dict.keys())
        # print(data_dict[lot[0]])
        self.wafer_select_dialog.lot_data = data_dict
        self.wafer_select_dialog.initializeLotTreeWidget()

        self.wafer_select_dialog.bin_group_data = bin_group_data_dict
        self.wafer_select_dialog.initializeBinTreeWidget()

        self.bin_data = df




if __name__ == "__main__":
    # from UI import StyleSheet
    import os

    app = QApplication(sys.argv)
    # app.setStyleSheet(StyleSheet)
    #### use to prevet the keranl dying everytime
    try:
        app.setStyle('Fusion')
    except Exception as e:
        print(e)
        app.setStyle('Windows')
    #
    # # get the root dir if not exit, create root dir
    # if not os.path.exists(resource_path('src')):
    #     os.mkdir(resource_path('src'))
    #
    # splash_pix = QPixmap(resource_path("UI/splash_image.jpg"))
    # splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    # splash.setEnabled(False)
    # progressBar = QProgressBar(splash)
    # progressBar.setMaximum(10)
    # progressBar.setGeometry(0, splash_pix.height() - 50, splash_pix.width(), 20)
    # splash.show()
    # splash.showMessage("<h1><font color='red'>WaferMap is opening...</font></h1>",
    #                    Qt.AlignTop | Qt.AlignTop, Qt.black)
    # for i in range(1, 2):
    #     progressBar.setValue(i)
    #     t = time.time()
    #     while time.time() < t + 0.1:
    #         app.processEvents()
    # # time.sleep(0.5)

    window = myApp()


    window.show()
    # splash.finish(window)
    sys.exit(app.exec())
