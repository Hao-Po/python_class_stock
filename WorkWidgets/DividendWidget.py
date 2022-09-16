from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from Source.PandasModelForDividend import PandasModel
import pandas as pd

from WorkWidgets.WidgetComponents import TableViewComponent

class DividendWidget(QtWidgets.QWidget):
    def __init__(self, search_widget):
        super().__init__()
        self.setObjectName("dividend_wigdet")
        self.search_widget = search_widget

        layout = QtWidgets.QGridLayout()

        self.tableView = TableViewComponent()
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        layout.addWidget(self.tableView, 0, 0, 1, 1)

        self.setLayout(layout)

    def load(self):
        data = self.search_widget.stock_dividend
        if type(data) is pd.DataFrame:
            if data.empty:
                QMessageBox.warning(self,"警告","股票代號不存在", QMessageBox.Ok)
                return
            else:
                model = PandasModel(data)
                self.tableView.setModel(model)
        else:
            QMessageBox.warning(self,"警告","股票代號不存在", QMessageBox.Ok)