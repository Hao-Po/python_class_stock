from PyQt5 import QtWidgets
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonTWComponent, TableWidgetComponent
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton
from Source.DBController.OptionalStockInfoTable import OptionalStockInfoTable
from Source.StockInfo import StockInfo

class OptionalWidget(QtWidgets.QWidget):
    def __init__(self, search_widget):
        super().__init__()
        self.setObjectName("optional_wigdet")
        self.search_widget = search_widget

        self.optional_stock_info_table = OptionalStockInfoTable()

        layout = QtWidgets.QGridLayout()

        self.editor_label_add = LineEditComponent("")
        self.editor_label_add.mousePressEvent = self.editor_content_clear

        self.button_add = ButtonTWComponent("新增自選")
        self.button_add.clicked.connect(self.confirm_action_add)

        self.table_widget = TableWidgetComponent()
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        layout.addWidget(self.editor_label_add, 0, 0, 1, 1)
        layout.addWidget(self.button_add, 0, 1, 1, 1)
        layout.addWidget(self.table_widget, 1, 0, 1, 8)
        
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 5)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 9)

        self.setLayout(layout)

    def load(self):
        self.table_widget.clear()
        stock_list = self.optional_stock_info_table.database_info()[0]
        self.table_widget.setColumnCount(4)
        self.table_widget.setRowCount(0)
        self.table_widget.setHorizontalHeaderLabels(['ID', 'Name', '', ''])
        self.table_widget.show()
        for index, (key, value) in enumerate(stock_list.items()):
            self.add_new_row(index, key, value)    

    def editor_content_clear(self, event):
        self.editor_label_add.clear()

    def add_new_row(self, index, key, value):
        self.table_widget.insertRow(index)
        aline_key = QTableWidgetItem(str(key))
        aline_key.setTextAlignment(Qt.AlignCenter)
        value = QTableWidgetItem(str(value))
        value.setTextAlignment(Qt.AlignCenter)
        self.table_widget.setItem(index, 0, aline_key)
        self.table_widget.setItem(index, 1, value)
        search_button = ButtonTWComponent("search")
        search_button.setObjectName("search_{}".format(key))
        search_button.clicked.connect(self.search_button_click)
        delete_button = ButtonTWComponent("delete")
        delete_button.setObjectName("delete_{}".format(key))
        delete_button.clicked.connect(lambda: self.delete_button_click(self.table_widget.currentRow()))
        self.table_widget.setCellWidget(index, 2, search_button)
        self.table_widget.setCellWidget(index, 3, delete_button)
    
    def confirm_action_add(self):
        add_stock_id, add_stock_name = StockInfo(stock_number = self.editor_label_add.text()).get_stock_name()
        if add_stock_id:
            if add_stock_id not in self.optional_stock_info_table.database_info()[0].keys():
                self.optional_stock_info_table.insert_new_stock(add_stock_id, add_stock_name)
                rows = self.table_widget.rowCount()
                self.add_new_row(rows, add_stock_id, add_stock_name)
        else:
             QMessageBox.warning(self,"警告","股票代號不存在", QMessageBox.Ok)
    
    def search_button_click(self):
        sender = self.sender()
        pushButton = self.findChild(QtWidgets.QPushButton, sender.objectName())
        stock_id = pushButton.objectName().replace("search_", "")
        self.search_widget.editor_label_search.setText(stock_id)
        self.search_widget.confirm_action_search()

    def delete_button_click(self, row=None):
        sender = self.sender()
        pushButton = self.findChild(QtWidgets.QPushButton, sender.objectName())
        if row is not None:
            self.table_widget.removeRow(row)
            stock_id = pushButton.objectName().replace("delete_", "")
            self.optional_stock_info_table.delete_stock(stock_id)

