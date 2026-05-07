from PyQt5 import QtWidgets, QtCore

class DocumentationScreenFreeSpan(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Documentation")
        self.resize(500, 300)

        # Central widget
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        layout = QtWidgets.QVBoxLayout(central_widget)

        # Title
        title = QtWidgets.QLabel("Subsea Pipelines (DNV Guidelines)")
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setStyleSheet("font-size: 22px; font-weight: bold;")
        layout.addWidget(title)

        # Text area (scrollable)
        self.text_area = QtWidgets.QTextEdit()
        self.text_area.setReadOnly(True)
        layout.addWidget(self.text_area)

        # Sample content
        self.text_area.setText(
           "\t\tFreeSpan Analysis\n\n"

            "Introduction:\n"
            "       Free span analysis evaluates the structural behavior of submarine pipelines\n"
            "       when unsupported sections occur between seabed contact points.\n"
            "       Free spans may develop due to uneven seabed conditions, scour, or installation effects,\n"
            "       leading to increased stresses, fatigue damage, and vortex-induced vibrations (VIV).\n"
            "       Proper assessment of free spans is essential to ensure pipeline integrity,\n"
            "       operational safety, and long-term reliability.\n\n"

            "Reference Standard:\n"
            "       This section follows DNV-RP-F105\n"
            "       (Free Spanning Pipelines),\n"
            "       which provides recommended practices for evaluating static behavior,\n"
            "       dynamic response, vortex-induced vibration (VIV), and allowable span limits\n"
            "       for submarine pipelines.\n\n"
        )
        
        # self.text_area.setText(
        #     "\t\tOn-Bottom Stability\n\n"
        #     "1. Lateral Stability Module\n"
        #     "   -Used for installation analysis\n\n"
        #     "2. Vertical Stability Module\n"
        #     "   -Used for operational conditions\n\n"
        #     "3. Pipeline Calculations\n"
        #     "   -Supports multiple engineering cases\n\n"
        #     "More content can be added here..."
        # )

        # Close button
        btn_close = QtWidgets.QPushButton("Close")
        btn_close.clicked.connect(self.close)
        layout.addWidget(btn_close)

        print("Documentation screen loaded")
        
        
# if __name__ == "__main__":
#     import sys

#     app = QtWidgets.QApplication(sys.argv)

#     window = DocumentationScreen()
#     window.show()

#     sys.exit(app.exec_())