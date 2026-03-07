import os
import fitz  # Import PyMuPDF
from PyQt5.QtCore import Qt, QEventLoop
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel


def render_pdf(pdf_label):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    pdf_path = os.path.join(script_dir, "..", "assets", "License_File.pdf")

    try:
        doc = fitz.open(pdf_path)
        pix = doc[0].get_pixmap()
        image = QPixmap()
        image.loadFromData(pix.tobytes())
        pdf_label.setPixmap(image)
        pdf_label.setAlignment(Qt.AlignCenter)
        print("PDF rendered successfully.")
    except Exception as e:
        print("Error rendering PDF:", e)


class PDFViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Document")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.pdf_label = QLabel()
        self.layout.addWidget(self.pdf_label)

        # self.button_open_pdf = QPushButton("Open PDF", self)
        # self.button_open_pdf.clicked.connect(self.open_pdf)
        # self.layout.addWidget(self.button_open_pdf)
        self.open_pdf()

    def open_pdf(self):
        render_pdf(self.pdf_label)


def run_pdf_viewer():
    window = PDFViewer()
    window.show()

    # Create a QEventLoop and start it to keep the application running
    loop = QEventLoop()
    loop.exec_()
