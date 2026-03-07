from PyQt5.QtWidgets import QMainWindow


class PipelineMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = QMainWindow()
        self.ui.setupUi(self)

        # Now ALL your logic goes here
        # Example:
        # self.ui.gradeComboBox.currentIndexChanged.connect(...)


# if __name__ == "__main__":
#     import sys
#     from PyQt5.QtWidgets import QApplication

#     app = QApplication(sys.argv)

#     window = PipelineMainWindow()
#     window.show()

#     sys.exit(app.exec_())
