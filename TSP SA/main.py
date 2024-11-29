import sys
from PyQt6.QtWidgets import QApplication
from ui import TSPWindow

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = TSPWindow()
        window.show()
        sys.exit(app.exec())
    except KeyboardInterrupt:
        print("Chương trình đã được dừng bằng phím tắt.")
