# from PyQt5.QtCore import
from PyQt5.QtWidgets import QGraphicsScene


class Scene(QGraphicsScene):

    def __init__(self):
        super(Scene, self).__init__()
        self.graphics_item_dict = {}
        self.polygon_selector_exist = False
