from PyQt5 import QtWidgets, QtCore

class WhatsNewScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("What's New")
        self.resize(500, 300)

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        layout = QtWidgets.QVBoxLayout(central_widget)

        # Title
        title = QtWidgets.QLabel("What's New")
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)

        # List of updates
        self.list_widget = QtWidgets.QListWidget()
        layout.addWidget(self.list_widget)

        # Add updates
        updates = [
            "Version 0.0.1 Released",
            "Added Lateral Stability Module",
            "Added Vertical Stability Module",
            "Improved Calculation Engine",
            "Bug fixes and performance improvements"
        ]

        self.list_widget.addItems(updates)

        # Close button
        btn_close = QtWidgets.QPushButton("Close")
        btn_close.clicked.connect(self.close)
        layout.addWidget(btn_close)

        print("What's New screen loaded")
        
        
# if __name__ == "__main__":
#     import sys

#     app = QtWidgets.QApplication(sys.argv)

#     window = WhatsNewScreen()
#     window.show()

#     sys.exit(app.exec_())