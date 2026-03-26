# from PyQt5.QtCore import QThread, pyqtSignal
# import time

# __version__ = "0.0.1"
# print(f"Loading CalculationWorker version {__version__}...")

# class CalculationWorker(QThread):
#     progress = pyqtSignal(int)
#     finished = pyqtSignal()

#     def run(self):
#         # Simulate step-by-step calculation
#         for i in range(1, 101):
#             time.sleep(0.03)  # simulate delay (adjust as needed)
#             self.progress.emit(i)

#         self.finished.emit()


from PyQt5.QtCore import QThread, pyqtSignal
from calculations import (
    lateralStability_installation,
    lateralStability_operationContentFilled,
    verticalStability_installationEmpty,
    verticalStability_operationContentFilled,
    verticalStability_operationShutDown
)

class CalculationWorker(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(object, str)  # result + analysis_type
    error = pyqtSignal(str)

    def __init__(self, analysis_type, selected_case, frontendData):
        super().__init__()
        self.analysis_type = analysis_type
        self.selected_case = selected_case
        self.frontendData = frontendData

    def run(self):
        try:
            self.progress.emit(10)

            # ----------- LATERAL STABILITY -----------
            if self.analysis_type == "Lateral Stability":

                self.progress.emit(40)

                if self.selected_case == "Installation-Empty":
                    result = lateralStability_installation(self.frontendData)

                elif self.selected_case == "Operation-Content Filled":
                    result = lateralStability_operationContentFilled(self.frontendData)

                else:
                    raise Exception("Invalid lateral case")

                self.progress.emit(90)

            # ----------- VERTICAL STABILITY -----------
            elif self.analysis_type == "Vertical Stability":

                self.progress.emit(40)

                if self.selected_case == "Installation-Empty":
                    result = verticalStability_installationEmpty(self.frontendData)

                elif self.selected_case == "Operation-Content Filled":
                    result = verticalStability_operationContentFilled(self.frontendData)

                elif self.selected_case == "Operation-Shutdown-Empty":
                    result = verticalStability_operationShutDown(self.frontendData)

                else:
                    raise Exception("Invalid vertical case")

                self.progress.emit(90)

            else:
                raise Exception("Invalid analysis type")

            self.progress.emit(100)
            self.finished.emit(result, self.analysis_type)

        except Exception as e:
            self.error.emit(str(e))