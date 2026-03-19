import csv
import pandas as pd
from tkinter import filedialog
import random
from PyQt5.QtWidgets import QMessageBox



# --- Action Button Handlers ---
def new_file(self):
    """Resets all inputs for a new simulation."""
    print("Action: New File")
    self.reset_all_inputs()
    QtWidgets.QMessageBox.information(self, "New File", "All inputs have been reset for a new simulation.")

def open_file(self):
    """Opens an existing simulation file."""
    print("Action: Open File")
    file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Simulation", "", "Simulation Files (*.sim);;All Files (*)")
    if file_path:
        print(f"Opening file: {file_path}")
        QtWidgets.QMessageBox.information(self, "Open File", f"Attempting to open: {file_path}\n(File loading logic not implemented yet)")
        # TODO: Implement actual file loading logic here.
        # You would read the content of the file (e.g., JSON or CSV)
        # and populate the UI fields accordingly.
    else:
        print("File open cancelled.")

def save_file_as(self):
    """Saves the current simulation data to a new file."""
    print("Action: Save File As")
    file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Simulation As", "", "Simulation Files (*.sim);;All Files (*)")
    if file_path:
        print(f"Saving file as: {file_path}")
        QtWidgets.QMessageBox.information(self, "Save File As", f"Attempting to save to: {file_path}\n(File saving logic not implemented yet)")
        # TODO: Implement actual file saving logic here.
        # You would gather all current input and output values from the UI
        # and write them to the specified file (e.g., in JSON format).
    else:
        print("File save cancelled.")

def generate_report(self):
    """Generates a detailed report of the simulation."""
    print("Action: Generate Report")
    QtWidgets.QMessageBox.information(self, "Generate Report", "Generating simulation report... (Placeholder)")
    # TODO: Implement report generation. This would typically involve:
    # 1. Re-running calculations to ensure results are fresh.
    # 2. Formatting all inputs and outputs into a printable format (e.g., PDF, HTML).
    # 3. Saving or displaying the report.

def show_whats_new(self):
    """Displays information about new features."""
    print("Action: What's New?")
    QtWidgets.QMessageBox.information(self, "What's New?",
                                    "Version 1.0.1\n\n"
                                    "- Implemented combobox selection logic.\n"
                                    "- Added action button functionality.\n"
                                    "- Console output for all inputs.\n"
                                    "- Corrected Barlow Stress calculation formula.")

def show_documentation(self):
    """Displays application documentation."""
    print("Action: Documentation")
    QtWidgets.QMessageBox.information(self, "Documentation",
                                    "Detailed documentation will be available here.\n"
                                    "For now, please refer to the input labels for guidance. (Placeholder)")
    # You could open a local PDF/HTML file or an online link here
    # Example: QtGui.QDesktopServices.openUrl(QtCore.QUrl("file:///path/to/your/documentation.pdf"))
    


def reset_all_inputs(self):
    """Resets all input fields, comboboxes, and radio buttons to their default states."""
    print("Resetting all inputs...")
    # Clear all line edits
    for line_edit in self.findChildren(QtWidgets.QLineEdit):
        line_edit.blockSignal(True)
        line_edit.clear()
        line_edit.blockSignal(False)

    # Reset comboboxes to default index (0)
    # for combo_box in self.findChildren(QtWidgets.QComboBox):
        # combo_box.setCurrentIndex(0)

    # Uncheck all radio buttons
    # self._uncheck_all_radio_buttons()

    # Re-initialize default numerical values (which now clears them)
    # self.initialize_default_input_values()
    print("All inputs have been reset.")
    
    

def saveAs(saveData):
    print(f"\n\tSaving file....!!!")
    try:
            
            filepath = filedialog.asksaveasfilename(
            # os.getenv('home'),
                    initialdir= "C:/Users/DELL/Desktop",
                    title= "Save As",
                    defaultextension= "*.csv",
                    filetypes=(
                            ("csv file","*.csv"),
                            ("HTML file","*.html"),
                            ("text file","*.txt"),
                            ("All file","*.*")
                    )
            )
    except:
            print(f"error code:{random.random()}>>>>>>Error in saving file while opening to write..$$%%^^&&&")
    try:
            if filepath is None:
                    return
            else:
                    with open(filepath, 'w'):
                            df = pd.DataFrame({"SL no" : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], "INPUTS": saveData.keys(), "Values": saveData.values()})
                            df.to_csv(filepath)
    except:
        print(f"error code:{random.random()}>>>>>>ERROR in saving your file...!!")
        QMessageBox.warning(None, "Warning", 'File is not saved..!!!!')
        


