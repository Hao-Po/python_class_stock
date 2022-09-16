from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *

class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        QtCore.QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=QtCore.Qt.DisplayRole):
        row = index.row()
        col = index.column()

        try: 
            if index.isValid():
                if role == QtCore.Qt.DisplayRole:
                    return str(self._data.iloc[row, col])
                if role == QtCore.Qt.TextAlignmentRole:
                    return QtCore.Qt.AlignLeft
        except:
            pass

        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None