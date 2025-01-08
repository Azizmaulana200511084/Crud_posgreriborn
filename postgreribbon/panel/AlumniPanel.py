from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from forms.frmAlumni import WindowAlumni

def alumni_panel(self):
        dock = QtWidgets.QDockWidget(self)
        alumni_widget = WindowAlumni()
        alumni_widget.select_data()
        self.centralwidget = alumni_widget
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)

        dock.setWidget(self.centralwidget)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)
        self.centralWidget()
        