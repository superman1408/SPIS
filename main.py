# from PyQt5.QtWidgets import QSplashScreen, QProgressBar, QLabel
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtCore import Qt, QTimer


# class SplashScreen(QSplashScreen):
#     def __init__(self):
#         pixmap = QPixmap("assets/splash.png")
#         super().__init__(pixmap)

#         self.setFixedSize(pixmap.size())

#         # Progress Bar
#         self.progress = QProgressBar(self)
#         self.progress.setGeometry(50, pixmap.height() - 50, pixmap.width() - 100, 20)
#         self.progress.setStyleSheet("""
#             QProgressBar {
#                 border: 1px solid white;
#                 text-align: center;
#                 color: white;
#             }
#             QProgressBar::chunk {
#                 background-color: #00c3ff;
#             }
#         """)

#         # Loading Label
#         self.label = QLabel("Starting...", self)
#         self.label.setGeometry(50, pixmap.height() - 80, 300, 20)
#         self.label.setStyleSheet("color: white;")

#         self.counter = 0
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.update_progress)
#         self.timer.start(40)

#     def update_progress(self):
#         self.counter += 1
#         self.progress.setValue(self.counter)

#         messages = {
#             20: "Loading Configuration...",
#             40: "Connecting Database...",
#             60: "Loading Modules...",
#             80: "Preparing UI...",
#             100: "Launching Software..."
#         }

#         if self.counter in messages:
#             self.label.setText(messages[self.counter])

#         if self.counter > 100:
#             self.timer.stop()


# import sys
# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtCore import QTimer

# from views.splash_screen import SplashScreen 
# from controllers.app_controller import AppController


# def main():
#     app = QApplication(sys.argv)

#     splash = SplashScreen()
#     splash.show()

#     controller = AppController()

#     def launch():
#         controller.show_main_window()
#         splash.finish(controller.window)

#     QTimer.singleShot(4000, launch)

#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()




import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton

from modules.PipelineWallThickness.app import PipelineWindow
from modules.PipelineCrossingCalculation.ui_design.main_app import PipelineSimulationApp 


class MainSoftware(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Software")
        self.setGeometry(200, 200, 600, 400)

        # Button to open pipeline module
        self.openBtn = QPushButton("Open Pipeline Module", self)
        self.openBtn.setGeometry(150, 150, 250, 60)

        self.openBtn.clicked.connect(self.open_pipeline)

        # Button 2
        self.openBtn1 = QPushButton("Open Pipeline Crossing Module", self)
        self.openBtn1.setGeometry(150, 250, 250, 60)
        self.openBtn1.clicked.connect(self.open_pipelineCrossing)

    def open_pipeline(self):
        self.pipeline = PipelineWindow()
        self.pipeline.show()

        

    def open_pipelineCrossing(self):
        self.pipelineC = PipelineSimulationApp()
        self.pipelineC.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainSoftware()
    window.show()
    sys.exit(app.exec_())
