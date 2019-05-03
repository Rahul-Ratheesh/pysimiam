#!/usr/bin/python
# QtSimiam
# Author: Tim Fuchs
# Description: This is the top-level application for QtSimiam.
from __future__ import print_function
import sys
sys.path.insert(0, './scripts')
sys.path.insert(0, './gui')
from PyQt5 import QtGui, QtWidgets

from qt_mainwindow import SimulationWidget
from coursera import Week2

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    simWidget = SimulationWidget()
    simWidget.setTestSuite(Week2)
    simWidget.superv_action.trigger()
    simWidget.show()
    simWidget.load_world("week2.xml")
    app.exec_()
