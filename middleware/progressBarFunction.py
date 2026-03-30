from PyQt5.QtCore import QThread, pyqtSignal
import time
from calculations import (
    lateralStability_installation,
    lateralStability_operationContentFilled,
    verticalStability_installationEmpty,
    verticalStability_operationContentFilled,
    verticalStability_operationShutDown
)

class CalculationProcess(QThread):
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
            result = None  # ✅ ensure defined

            for i in range(1, 101):
                time.sleep(0.02)
                self.progress.emit(i)

                # Run calculation once
                if i == 50 and result is None:

                    # ----------- LATERAL STABILITY -----------
                    if self.analysis_type == "Lateral Stability":
                        if self.selected_case == "Installation-Empty":
                            result = lateralStability_installation(self.frontendData)

                        elif self.selected_case == "Operation-Content Filled":
                            result = lateralStability_operationContentFilled(self.frontendData)

                        else:
                            raise Exception("Invalid lateral case")

                    # ----------- VERTICAL STABILITY -----------
                    elif self.analysis_type == "Vertical Stability":
                        if self.selected_case == "Installation-Empty":
                            result = verticalStability_installationEmpty(self.frontendData)

                        elif self.selected_case == "Operation-Content Filled":
                            result = verticalStability_operationContentFilled(self.frontendData)

                        elif self.selected_case == "Operation-Shutdown-Empty":
                            result = verticalStability_operationShutDown(self.frontendData)

                        else:
                            raise Exception("Invalid vertical case")

                    else:
                        raise Exception("Invalid analysis type")

            # ✅ Safety check
            if result is None:
                raise Exception("Calculation did not execute")

            self.finished.emit(result, self.analysis_type)

        except Exception as e:
            self.error.emit(str(e))