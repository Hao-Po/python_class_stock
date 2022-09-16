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
                    return QtCore.Qt.AlignRight     
                if row % 2 == 1 and role == QtCore.Qt.BackgroundRole:
                    return QtGui.QBrush(QtGui.QColor(215, 215, 234))
                elif row % 2 == 0 and role == QtCore.Qt.BackgroundRole:
                    return QtGui.QBrush(QtGui.QColor(198, 198, 226))
                if col == 6 and float(index.data().replace("%","")) > 0 and role == QtCore.Qt.ForegroundRole:
                    return QVariant(QtGui.QColor(235, 0, 0))
                elif col == 6 and float(index.data().replace("%","")) < 0 and role == QtCore.Qt.ForegroundRole:
                    return QVariant(QtGui.QColor(0, 97, 0))
                if col == 1 and float(index.data().replace(",","")) > 0 and role == QtCore.Qt.ForegroundRole:
                    return QVariant(QtGui.QColor(235, 0, 0))
                elif col == 1 and float(index.data().replace(",","")) < 0 and role == QtCore.Qt.ForegroundRole:
                    return QVariant(QtGui.QColor(0, 97, 0))
                if col == 2 and float(index.data().replace(",","")) > 0 and role == QtCore.Qt.ForegroundRole:
                    return QVariant(QtGui.QColor(235, 0, 0))
                elif col == 2 and float(index.data().replace(",","")) < 0 and role == QtCore.Qt.ForegroundRole:
                    return QVariant(QtGui.QColor(0, 97, 0))
                if col == 3 and float(index.data().replace(",","")) > 0 and role == QtCore.Qt.ForegroundRole:
                    return QVariant(QtGui.QColor(235, 0, 0))
                elif col == 3 and float(index.data().replace(",","")) < 0 and role == QtCore.Qt.ForegroundRole:
                    return QVariant(QtGui.QColor(0, 97, 0))
                if col == 4 and float(index.data().replace(",","")) > 0 and role == QtCore.Qt.ForegroundRole:
                    return QVariant(QtGui.QColor(235, 0, 0))
                elif col == 4 and float(index.data().replace(",","")) < 0 and role == QtCore.Qt.ForegroundRole:
                    return QVariant(QtGui.QColor(0, 97, 0))
                    
        except:
            pass

        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None