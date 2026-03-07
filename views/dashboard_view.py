# from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListWidget, QStackedWidget,QPushButton
# from modules.pipeline_wallthickness import PipelineWallthickness
# from modules.PipelineWallThickness.old_module_window import open_old_module

# # from modules.stress_module import StressModule
# # from modules.mto_module import MTOModule


# class DashboardView(QWidget):
#     def __init__(self):
#         super().__init__()

#         layout = QHBoxLayout(self)

#         # Sidebar
#         self.sidebar = QListWidget()
#         self.sidebar.addItems(["Piping", "Stress", "MTO"])

#         # Workspace
#         self.workspace = QStackedWidget()

#         layout.addWidget(self.sidebar, 1)
#         layout.addWidget(self.workspace, 4)

#         self.sidebar.currentRowChanged.connect(self.workspace.setCurrentIndex)

#         self.workspace.addWidget(PipelineWallthickness())
#         # self.workspace.addWidget(StressModule())
#         # self.workspace.addWidget(MTOModule())

#         self.pipeline_widget = PipelineWallthickness()
#         self.workspace.addWidget(self.pipeline_widget)

#         self.openBtn = QPushButton("Open Old Module")
#         layout.addWidget(self.openBtn)

#         # ⭐ THIS is the only thing that matters
#         self.openBtn.clicked.connect(open_old_module)

#         # self.sidebar.currentRowChanged.connect(self.open_old_module)



from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from modules.PipelineWallThickness.old_module_window import open_old_module


class DashboardView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.openBtn = QPushButton("Open Old Module")
        layout.addWidget(self.openBtn)

        self.openBtn.clicked.connect(open_old_module)
