from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from Source.PandasModelForAnalysis import PandasModel
from WorkWidgets.WidgetComponents import TableViewComponent
import pandas as pd

class AnalysisWidget(QtWidgets.QWidget):
    def __init__(self, search_widget):
        super().__init__()
        self.setObjectName("analysis_wigdet")
        self.search_widget = search_widget
        
        layout = QtWidgets.QGridLayout()

        self.KLineFigure = QLabel()
        self.KLineFigure.setAlignment(QtCore.Qt.AlignCenter)

        self.tableView = TableViewComponent()
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        layout.addWidget(self.KLineFigure, 0, 0, 1, 1)
        layout.addWidget(self.tableView, 1, 0, 1, 1)

        self.setLayout(layout)

    def load(self):
        data = self.search_widget.stock_analysis
        if type(data) is pd.DataFrame:
            if data.empty:
                QMessageBox.warning(self,"警告","股票代號不存在", QMessageBox.Ok)
                return
            else:
                self.KLineFigure.setPixmap(QPixmap("Figure/KLineFigure.jpg").scaled(723,520))
                model = PandasModel(data)
                self.tableView.setModel(model)
        else:
            QMessageBox.warning(self,"警告","股票代號不存在", QMessageBox.Ok)