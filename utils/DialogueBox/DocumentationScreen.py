from PyQt5 import QtWidgets, QtCore

class DocumentationScreen(QtWidgets.QMainWindow):
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
            "\t\tOn-Bottom Stability\n\n"
            "Introduction:\n"
            "       On-bottom stability refers to the ability of a sub-sea pipeline\n"
            "       to remain in place on the seabed under\n"
            "       the influence of environmental loads such as currents, waves, and operational forces. \n"
            "       Ensuring on-bottom stability is critical to prevent pipeline movement, structural damage, \n"
            "       and environmental hazards.\n\n"
            "Reference Standard:\n"
            "       This section follows DNV-RP-F105\n"
            "       (Guidelines for the Design and Installation of Submarine Pipelines),\n"
            "       which provides methodologies to evaluate the stability of pipelines on the seabed.\n\n"
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