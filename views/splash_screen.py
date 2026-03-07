from PyQt5.QtWidgets import QSplashScreen, QProgressBar, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer, pyqtSignal


class SplashScreen(QSplashScreen):

    finished = pyqtSignal()   # ⭐ signal to tell main app when loading ends

    def __init__(self):
        pixmap = QPixmap("assets/splashscreen.png")
        super().__init__(pixmap)

        self.setFixedSize(pixmap.size())

        # Progress Bar
        self.progress = QProgressBar(self)
        self.progress.setGeometry(50, pixmap.height() - 60, pixmap.width() - 100, 25)

        self.progress.setStyleSheet("""
            QProgressBar {
                border: 2px solid white;
                border-radius: 5px;
                background-color: rgba(0,0,0,120);
                text-align: center;
                color: white;
            }

            QProgressBar::chunk {
                background-color: #00c3ff;
            }
        """)

        # Label
        self.label = QLabel("Starting...", self)
        self.label.setGeometry(50, pixmap.height() - 90, 400, 25)

        self.label.setStyleSheet("""
            color: white;
            font-size: 14px;
            font-weight: bold;
        """)

        self.counter = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(40)   # speed of animation

    def update_progress(self):

        self.counter += 1
        self.progress.setValue(self.counter)

        messages = {
            20: "Loading Configuration...",
            40: "Connecting Database...",
            60: "Loading Modules...",
            80: "Preparing UI...",
            100: "Launching Software..."
        }

        if self.counter in messages:
            self.label.setText(messages[self.counter])

        if self.counter >= 100:
            self.timer.stop()
            self.finished.emit()   # ⭐ Tell main app splash is done
