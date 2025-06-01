import os, sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QStackedLayout, QScrollArea
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class FlatButton(QPushButton):
    def __init__(self, text, *args, **kwargs):
        super().__init__(text, *args, **kwargs)
        self.setStyleSheet("""
            QPushButton {
                background-color: #ff8000;
                color: white;
                border: none;
                padding: 35px 10px;
                font-size: 36px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #ff9428;
            }
            QPushButton:pressed {
                background-color: #b95c00;
            }
        """)
        self.setFont(QFont("Arial", 14))

class Main(QWidget):
    def load_app(self):
        print("Load App")
    
    def settings(self):
        print("Settings")
    
    def install_apps(self):
        print("Install App(s)")
    
    def exit(self):
        print("Exiting...")
        sys.exit(0)
    
    def shutdown(self):
        print("Shutting down...")
        if os.name == "nt":
            sys.exit(0)
        else:
            os.system("sudo shutdown -h now")
    
    def open_menu(self, menu):
        if menu in self.menus:
            self.main_layout.setCurrentIndex(self.menus[menu])
    
    def add_to_stack(self, layout):
        new_widget = QWidget()
        new_widget.setLayout(layout)
        self.main_layout.addWidget(new_widget)
        return self.main_layout.indexOf(new_widget)
    
    def create_settings_menu(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        scroll_area = QScrollArea()
        layout1 = QVBoxLayout()
        layout1.setContentsMargins(20, 20, 20, 20)
        layout1.setSpacing(5)
        setting1 = FlatButton("Setting 1")
        setting1.clicked.connect(lambda: print("Setting 1 clicked"))
        layout1.addWidget(setting1)
        scroll_area.setLayout(layout1)
        scroll_area.setWidgetResizable(False)
        layout.addWidget(scroll_area)
        i = self.add_to_stack(layout)
        self.menus["settings"] = i
    
    def create_exit_menu(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(5)
        layout1 = QHBoxLayout()
        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(5)
        btn1 = FlatButton("Exit")
        btn1.clicked.connect(self.exit)
        btn2 = FlatButton("Shut Down")
        btn2.clicked.connect(self.shutdown)
        layout1.addWidget(btn1)
        layout1.addWidget(btn2)
        layout.addLayout(layout1)
        btn3 = FlatButton("Back")
        btn3.clicked.connect(lambda: self.open_menu("main"))
        layout.addWidget(btn3)
        i = self.add_to_stack(layout)
        self.menus["exit"] = i
    
    def create_main_menu(self):
        # Layout setup
        glayout = QGridLayout()
        glayout.setContentsMargins(20, 20, 20, 20)
        glayout.setSpacing(5)
        
        buttons = ["Load App", "Settings", "Install App(s)", "Exit/Power"]
        callbacks = [self.load_app, lambda: self.open_menu("settings"), self.install_apps, lambda: self.open_menu("exit")]
        rows = 2
        # Create buttons
        for i in range(len(buttons)):
            btn = FlatButton(f"{buttons[i]}")
            btn.clicked.connect(callbacks[i])
            col = 0 if i < rows else 1
            row = i if i < rows else i - rows
            glayout.addWidget(btn, row, col)
        i = self.add_to_stack(glayout)
        self.menus["main"] = i
    
    def create_menus(self):
        self.create_main_menu()
        self.create_settings_menu()
        self.create_exit_menu()
    
    def __init__(self, width: int, height: int):
        super().__init__()
        self.setWindowTitle("HackZero")
        self.setGeometry(0, 0, width, height)
        
        self.main_layout = QStackedLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        self.menus = {}
        self.create_menus()
        
        self.setLayout(self.main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main(848, 480)
    main.show()
    sys.exit(app.exec_())