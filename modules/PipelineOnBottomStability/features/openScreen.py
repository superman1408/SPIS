from PyQt5 import QtWidgets

def open_screen(screen_class, *args, **kwargs):
    try:
        screen = screen_class(*args, **kwargs)
        screen.show()
        return screen
    except Exception as e:
        print(f"Error opening screen: {e}")
        return None
    
    
