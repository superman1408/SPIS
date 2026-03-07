from PyQt5.QtWidgets import QMainWindow
from modules.PipelineWallThickness.app import Ui_MainWindow

old_window = None   # keeps window alive

def open_old_module():
    global old_window
    old_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(old_window)
    old_window.show()


# import subprocess
# import sys
# import os


# def open_old_module():
#     old_app_path = os.path.join(
#         os.path.dirname(__file__),
#         "app.py"
#     )

#     subprocess.Popen([ r"modules\PipelineWallThickness\app.py"
#     ], shell=True)
