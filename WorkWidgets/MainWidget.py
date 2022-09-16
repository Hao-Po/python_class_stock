from PyQt5 import QtWidgets
from WorkWidgets.WidgetComponents import ButtonComponent
from WorkWidgets.SearchWidget import SearchWidget
from WorkWidgets.ProfileWidget import ProfileWidget
from WorkWidgets.AnalysisWidget import AnalysisWidget
from WorkWidgets.TradingWidget import TradingWidget
from WorkWidgets.DividendWidget import DividendWidget
from WorkWidgets.OptionalWidget import OptionalWidget

class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("main_widget")
        window_title = "StockInfo"
        self.setWindowTitle(window_title)
        layout = QtWidgets.QVBoxLayout()
        search_widget = SearchWidget()
        info_widget = InfoWidget(search_widget)
        menu_widget = MenuStockWidget(info_widget.update_widget)

        layout.addWidget(search_widget, stretch=1)
        layout.addWidget(menu_widget, stretch=1)
        layout.addWidget(info_widget, stretch=98)

        self.setLayout(layout)

class MenuStockWidget(QtWidgets.QWidget):
    def __init__(self, update_widget_callback):
        super().__init__()
        self.setObjectName("menu_widget")
        self.update_widget_callback = update_widget_callback

        layout = QtWidgets.QHBoxLayout()
        self.button_optional = ButtonComponent("自選股票")
        self.button_optional.clicked.connect(lambda: self.update_widget_callback("optional"))
        self.button_profile = ButtonComponent("基本資料")
        self.button_profile.clicked.connect(lambda: self.update_widget_callback("profile"))
        self.button_analysis = ButtonComponent("技術分析")
        self.button_analysis.clicked.connect(lambda: self.update_widget_callback("analysis"))
        self.button_trading = ButtonComponent("法人買賣")
        self.button_trading.clicked.connect(lambda: self.update_widget_callback("trading"))
        self.button_dividend = ButtonComponent("歷年股利")
        self.button_dividend.clicked.connect(lambda: self.update_widget_callback("dividend"))

        layout.addWidget(self.button_optional, stretch=1)
        layout.addWidget(self.button_profile, stretch=1)
        layout.addWidget(self.button_analysis, stretch=1)
        layout.addWidget(self.button_trading, stretch=1)
        layout.addWidget(self.button_dividend, stretch=1)

        self.setLayout(layout)

class InfoWidget(QtWidgets.QStackedWidget):
    def __init__(self, search_widget):
        super().__init__()
        self.widget_dict = {
            "optional": self.addWidget(OptionalWidget(search_widget)), 
            "profile": self.addWidget(ProfileWidget(search_widget)),
            "analysis": self.addWidget(AnalysisWidget(search_widget)),
            "trading": self.addWidget(TradingWidget(search_widget)),            
            "dividend": self.addWidget(DividendWidget(search_widget))
        }
        self.update_widget("optional")
    
    def update_widget(self, name):
        self.setCurrentIndex(self.widget_dict[name])
        current_widget = self.currentWidget()
        current_widget.load()
