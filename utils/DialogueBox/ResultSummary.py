from PyQt5 import QtWidgets, QtCore, QtGui


class ResultSummary(QtWidgets.QMainWindow):

    def __init__(self, result):
        super().__init__()

        self.result = result

        self.setWindowTitle("Analysis Summary")

         # Add Window Icon
        self.setWindowIcon(QtGui.QIcon("../SPIS/assets/OnBottomRoughness.png"))

        self.resize(550, 400)

        # Main window modern styling
        self.setStyleSheet("""
            QMainWindow {
                background-color: qlineargradient(spread:pad, x1:0.028, y1:0.0455909, x2:0.841, y2:0.966364, stop:0 rgba(169, 237, 255, 107), stop:0.994318 rgba(253, 255, 218, 255));
            }

            QLabel {
                color: #222;
            }

            QPushButton {
                background-color: #1f6feb;
                color: white;
                border-radius: 10px;
                padding: 5px;
                font-size: 12px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #1158c7;
            }

            QListWidget {
                background-color: transparent;
                border: none;
                padding: 4px;
            }

            QListWidget::item {
                border-radius: 14px;
                padding: 5px;
                margin: 3px;
            }
        """)

        # Central Widget
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        # Main Layout
        layout = QtWidgets.QVBoxLayout(central_widget)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        # ================= TITLE =================

        title = QtWidgets.QLabel("Free Span Analysis Summary")
        title.setAlignment(QtCore.Qt.AlignCenter)

        title.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
            color: #1f2937;
            padding: 5px;
        """)

        layout.addWidget(title)

        # ================= SUBTITLE =================

        subtitle = QtWidgets.QLabel("Structural Integrity & Hydrodynamic Assessment")
        subtitle.setAlignment(QtCore.Qt.AlignCenter)

        subtitle.setStyleSheet("""
            font-size: 12px;
            color: #6b7280;
            margin-bottom: 10px;
        """)

        layout.addWidget(subtitle)

        # ================= LIST =================

        self.list_widget = QtWidgets.QListWidget()

        self.list_widget.setSpacing(4)

        layout.addWidget(self.list_widget)

        # ================= RESULT DATA =================

        L_D_Status = self.result.get("LD_Check")
        deflectionStatus = self.result.get("Deflection_status")
        bendingStatus = self.result.get("BendingStress_status")
        # flowregimeStatus = self.result.get("Flow_Regime_status")
        VIVStatus = self.result.get("VIV_Status")
        fatigueStatus = self.result.get("Fatigue_status")
        ULSStatus = self.result.get("ULS_status")

        # ================= STATUS ITEMS =================

        status_data = [
            ("L/D Check", L_D_Status),
            ("Deflection", deflectionStatus),
            ("Bending Stress", bendingStatus),
            # ("Flow Regime", flowregimeStatus),
            ("VIV", VIVStatus),
            ("Fatigue", fatigueStatus),
            ("ULS", ULSStatus),
        ]

        for label, status in status_data:

            item = QtWidgets.QListWidgetItem()

            # Default Styling
            bg_color = "#ffffff"
            text_color = "#1f2937"
            icon = ""

            status_upper = str(status).upper()

            # ================= RED =================

            if any(word in status_upper for word in ["FAIL", "UNSAFE", "SEVERE"]):
                bg_color = "#fee2e2"
                text_color = "#991b1b"
                icon = "❌"

            # ================= GREEN =================

            elif any(word in status_upper for word in ["PASS", "SAFE", "NO VIV"]):
                bg_color = "#dcfce7"
                text_color = "#166534"
                icon = "✅"
            # ================= YELLOW =================

            elif any(word in status_upper for word in ["INLINE", "CROSS FLOW"]):
                bg_color = "#fef3c7"
                text_color = "#92400e"
                icon = "⚠️"

            # ================= BLUE =================

            elif any(word in status_upper for word in ["MIXED"]):
                bg_color = "#dbeafe"
                text_color = "#1e40af"
                icon = "🔄"

            elif any(word in status_upper for word in ["WAVE"]):
                bg_color = "#dbeafe"
                text_color = "#1e40af"
                icon = "🌊"

            elif any(word in status_upper for word in ["CURRENT"]):
                bg_color = "#dbeafe"
                text_color = "#1e40af"
                icon = "⇢"

            item.setText(f"{icon}   {label} : {status}")

            item.setBackground(QtGui.QColor(bg_color))
            item.setForeground(QtGui.QColor(text_color))

            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)

            item.setFont(font)

            self.list_widget.addItem(item)

        # ================= CLOSE BUTTON =================

        btn_close = QtWidgets.QPushButton("Close")
        btn_close.setFixedHeight(20)

        btn_close.clicked.connect(self.close)

        layout.addWidget(btn_close)

        print("Result summary loaded")