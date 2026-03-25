import json
from PyQt5 import QtWidgets

def save_inputs(input_fields, file_path):  
    data = {}
    for key, widget in input_fields.items():
        try:
            # Check widget exists and is a QLineEdit
            if widget is not None and isinstance(widget, QtWidgets.QLineEdit):
                data[key] = widget.text()
            elif isinstance(widget, QtWidgets.QComboBox):
                data[key] = widget.currentText()

            else:
                print(f"Warning: '{key}' is not a valid QLineEdit")
                data[key] = ""
        except Exception as e:
            print(f"Error saving '{key}': {e}")
            data[key] = ""

    try:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        print(f"Error writing file: {e}")
        return False


def load_inputs_mapped(json_file, mapping):
    try:
        with open(json_file, "r") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Failed to read JSON: {e}")
        return False

    for key, widget in mapping.items():
        try:
            if widget is not None and isinstance(widget, QtWidgets.QLineEdit):
                widget.blockSignals(True)
                
            # QLineEdit
            if isinstance(widget, QtWidgets.QLineEdit):
                widget.setText(str(data.get(key, "")))

            # ✅ QComboBox (THIS IS WHAT YOU NEED)
            elif isinstance(widget, QtWidgets.QComboBox):
                value = data.get(key, "")

                index = widget.findText(value)
                if index != -1:
                    widget.setCurrentIndex(index)
                else:
                    print(f"Warning: '{value}' not found in ComboBox '{key}'")
                widget.blockSignals(False)
        except Exception as e:
            print(f"Error setting {key}: {e}")

    return True