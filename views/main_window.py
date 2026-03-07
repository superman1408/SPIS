from PyQt5.QtWidgets import QMainWindow, QDockWidget
from views.dashboard_view import DashboardView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pipeline Integrated Software")
        self.resize(1200, 700)

        self.dashboard = DashboardView()
        self.setCentralWidget(self.dashboard)
