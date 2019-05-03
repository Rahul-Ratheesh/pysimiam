from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal

class LogDock(QtWidgets.QDockWidget):
    closed = pyqtSignal(bool)
    def __init__(self, parent):
        """Construct a new dockwindow with the log """
        
        QtWidgets.QDockWidget.__init__(self, "Message log", parent)
        self.setAllowedAreas(Qt.TopDockWidgetArea | Qt.BottomDockWidgetArea)

        self.table = QtWidgets.QTableWidget(0,2,self)
        self.table.setHorizontalHeaderLabels(["Sender","Message"])

        self.table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        hhdrs = self.table.horizontalHeader()       
        hhdrs.setSectionResizeMode (0,QtWidgets.QHeaderView.ResizeToContents)
        hhdrs.setSectionResizeMode (1,QtWidgets.QHeaderView.Stretch)

        self.setWidget(self.table)

    def append(self,message,name,color):
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row,0,QtWidgets.QTableWidgetItem(name))
        self.table.setItem(row,1,QtWidgets.QTableWidgetItem(message))
        clr = QtWidgets.QTableWidgetItem(" ")
        self.table.setVerticalHeaderItem(row,clr)
        if color is not None:
            clr.setBackground(QtGui.QColor(color))

    def closeEvent(self,event):
        super(LogDock,self).closeEvent(event)
        if event.isAccepted():
            print('closed')
            self.closed.emit(True)