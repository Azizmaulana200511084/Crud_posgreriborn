from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from forms.frmDosen import WindowDosen

def dosen_panel(self):
        dock = QtWidgets.QDockWidget(self)
        dosen_widget = WindowDosen()
        dosen_widget.select_data()
        self.centralwidget = dosen_widget
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)

        dock.setWidget(self.centralwidget)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)
        self.centralWidget()