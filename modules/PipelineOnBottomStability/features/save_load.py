import json
from PyQt5 import QtWidgets

def save_inputs(input_fields, file_path):
    import json
    from PyQt5 import QtWidgets

    data = {}
    for key, widget in input_fields.items():
        try:
            # Check widget exists and is a QLineEdit
            if widget is not None and isinstance(widget, QtWidgets.QLineEdit):
                data[key] = widget.text()
            else:
                print(f"⚠ Warning: '{key}' is not a valid QLineEdit")
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
    import json
    from PyQt5 import QtWidgets

    try:
        with open(json_file, "r") as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Failed to read JSON: {e}")
        return False

    for key, widget in mapping.items():
        try:
            if widget is not None and isinstance(widget, QtWidgets.QLineEdit):
                widget.blockSignals(True)
                widget.setText(str(data.get(key, "")))
                widget.blockSignals(False)
        except Exception as e:
            print(f"Error setting {key}: {e}")

    return True