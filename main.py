import os, sys
from PyQt5.QtWidgets import QApplication, QWidget, QStackedLayout
from PyQt5.QtCore import Qt
from hackzero import menus

class Main(QWidget):
    def exit(self):
        print("Exiting...")
        sys.exit(0)
    
    def shutdown(self):
        print("Shutting down...")
        if os.name == "nt":
            sys.exit(0)
        else:
            os.system("sudo shutdown -h now")
    
    def open_menu(self, menu) -> None:
        if menu in self.menus:
            self.main_layout.setCurrentIndex(self.menus[menu])
    
    def add_to_stack(self, layout) -> int:
        new_widget = QWidget()
        new_widget.setLayout(layout)
        self.main_layout.addWidget(new_widget)
        return self.main_layout.indexOf(new_widget)
    
    def create_menus(self) -> None:
        for menu in menus.ALL:
            menu.create(self)
    
    def __init__(self, width: int, height: int, screen_geometry, *args, **kwargs):
        super().__init__()
        self.setWindowTitle("HackZero")
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setGeometry(100, 100, width, height)
        
        if "--fullscreen" in sys.argv:
            self.showFullScreen()
            self.setGeometry(screen_geometry)
        
        self.main_layout = QStackedLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        self.menus = {}
        self.create_menus()
        
        self.setLayout(self.main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main(640, 340, app.desktop().screenGeometry())
    main.show()
    sys.exit(app.exec_())