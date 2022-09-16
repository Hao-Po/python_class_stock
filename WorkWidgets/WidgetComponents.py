from PyQt5 import QtWidgets, QtCore, QtGui

class LabelComponent(QtWidgets.QLabel):
    def __init__(self, font_size, content):
        super().__init__()
        self.setWordWrap(True)
        self.setAlignment(QtCore.Qt.AlignLeft)
        self.setStyleSheet("color: #32435F; border: 2px solid #32435F; border-radius: 10px")
        self.setFont(QtGui.QFont("微軟正黑體", font_size, QtGui.QFont.Bold))
        self.setText(content)

class LineEditComponent(QtWidgets.QLineEdit):
    def __init__(self, default_content="", length=10, width=200, font_size=14):
        super().__init__()
        self.setMaxLength(length)
        self.setText(default_content)
        self.setStyleSheet("background-color: #FFFFFF; color : black;")
        self.setMinimumHeight(30)
        self.setMaximumWidth(width)
        self.setFont(QtGui.QFont("微軟正黑體", font_size))

class ButtonComponent(QtWidgets.QPushButton):
    def __init__(self, text, font_size=14):
        super().__init__()
        self.setText(text)
        self.setStyleSheet("QPushButton{background:#A5B7C1; max-width:200px ; padding: 5px; border-radius:4px; border-color: 2px solid #408080; color: black;}\
                            QPushButton:hover{background:#81C0C0; border: 2px solid #336666;}\
                            QPushButton:pressed{background: #A3D1D1; border: 2px solid #81C0C0; color: #408080;}")

        self.setFont(QtGui.QFont("微軟正黑體", font_size))

class ButtonTWComponent(QtWidgets.QPushButton):
    def __init__(self, text, font_size=14):
        super().__init__()
        self.setText(text)
        self.setStyleSheet("QPushButton{background:#A5B7C1; padding: 5px; border-radius:4px; border-color: 2px solid #408080; color: black;}\
                            QPushButton::hover{background:#81C0C0; border: 2px solid #336666;}\
                            QPushButton::pressed{background: #A3D1D1; border: 2px solid #81C0C0; color: #408080;}")

        self.setFont(QtGui.QFont("微軟正黑體", font_size))


class TableViewComponent(QtWidgets.QTableView):
    def __init__(self, font_size=12):
        super().__init__()
        self.setAutoFillBackground(True)
        self.setStyleSheet("QHeaderView::section { background-color: gray; color: white; border-color: 2px solid white;}, \
                            QTableView::section:focus{ selection-background-color: #B8B8DC;}")

        stylesheet = "::section { font: 微軟正黑體; font-size: 18px; background-color: #ADADAD; color: black;}"
        self.horizontalHeader().setStyleSheet(stylesheet)
        self.verticalHeader().setStyleSheet(stylesheet)
        self.setFont(QtGui.QFont("微軟正黑體", font_size, QtGui.QFont.Bold))

class TableWidgetComponent(QtWidgets.QTableWidget): 
    def __init__(self, font_size=14):
        super().__init__()
        stylesheet = "::section { font: 微軟正黑體; font-size: 20px; background-color: #9D9D9D; color: black;}"
        self.horizontalHeader().setStyleSheet(stylesheet)
        self.verticalHeader().setStyleSheet(stylesheet)        
        self.setStyleSheet("QTableView::item { border: 1px solid gray;},\
                            QHeaderView::section{ background-color: gray; color: white;}")

        self.setFont(QtGui.QFont("微軟正黑體", font_size, QtGui.QFont.Bold))
        