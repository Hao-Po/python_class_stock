from WorkWidgets.MainWidget import MainWidget
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication([])
main_window = MainWidget()
main_window.setFixedSize(1200, 900)
main_window.setStyleSheet( "color: black;" 
                        "background-color: #DBDBE5;"
                        "border-radius: 2px;"
                        )
main_window.show()
QApplication.processEvents()


sys.exit(app.exec_())
