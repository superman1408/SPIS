from views.main_window import MainWindow
from modules.PipelineWallThickness.old_module_window import open_old_module



class AppController:
    def __init__(self):
        self.window = MainWindow()

    def show_main_window(self):
        self.window.show()

    def open_old_module(self):
        open_old_module()

