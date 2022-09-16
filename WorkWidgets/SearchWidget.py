from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from pandas import DataFrame
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent
from Source.StockInfo import StockInfo
import pandas as pd

class SearchWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("search_widget")

        self.stock_profile = DataFrame()
        self.stock_analysis = DataFrame()
        self.stock_trading = DataFrame()
        self.stock_dividend = DataFrame()

        layout = QtWidgets.QGridLayout()

        self.header_label = LabelComponent(22, "三梅‧股海冥燈")
        self.header_label.setAlignment(Qt.AlignCenter)

        self.editor_label_search = LineEditComponent("")
        self.editor_label_search.mousePressEvent = self.editor_content_clear

        self.button_search = ButtonComponent("search")
        self.button_search.clicked.connect(self.confirm_action_search)

        layout.addWidget(self.editor_label_search, 0, 0, 1, 1)
        layout.addWidget(self.button_search, 0, 1, 1, 1)
        layout.addWidget(self.header_label, 0, 2, 1, 1)
        
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 8)
 
        self.setLayout(layout)

    def editor_content_clear(self, event):
        self.editor_label_search.clear()

    def confirm_action_search(self):
        stock = StockInfo(self.editor_label_search.text(), self)
        self.stock_profile = stock.get_profile()
        self.stock_analysis = stock.get_technical_analysis()
        self.stock_trading = stock.get_institutional_trading()
        self.stock_dividend = stock.get_dividend()
        print("search_number = {}".format(self.editor_label_search.text()))
