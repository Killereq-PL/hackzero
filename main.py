import os, sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QStackedLayout, QScrollArea
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from hackzero.ui.FlatButton import FlatButton
from hackzero.ui.ListButtonView import ListButtonView

class Main(QWidget):
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
    
    def create_load_app_menu(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(5)
        lbv_data = [
            {
            'title': 'Example1',
            'icon': 'icon128.png',
            'description': 'First Example',
            'category': 'Examples',
            },
            {
            'title': 'Example2',
            'icon': 'icon128.png',
            'description': 'Second Example',
            'category': 'Examples',
            },
            {
            'title': 'Example3',
            'icon': 'icon128.png',
            'description': 'Third Example',
            'category': 'Examples',
            },
            {
            'title': 'Example4',
            'icon': 'icon128.png',
            'description': 'Fourth Example',
            'category': 'Examples',
            },
            {
            'title': 'Test1',
            'icon': 'icon128.png',
            'description': 'First Test',
            'category': 'Tests',
            },
            {
            'title': 'Test2',
            'icon': 'icon128.png',
            'description': 'Second Test',
            'category': 'Tests'
            },
            {
            'title': 'Test3',
            'icon': 'icon128.png',
            'description': 'Third Test',
            'category': 'Tests',
            },
            {
            'title': 'Test4',
            'icon': 'icon128.png',
            'description': 'Fourth Test',
            'category': 'Tests'
            }
        ]
        lbv_settings = {
            'categories': {
                'Examples': {
                    'columns': {
                        'title': {'width': 200},
                        'description': {'width': 400}
                    },
                    'shown': True
                },
                'Tests': {
                    'columns': {
                        'title': {'width': 200},
                        'description': {'width': 400}
                    },
                    'shown': True
                }
            },
        }
        
        lbv = ListButtonView(lbv_data, True, lbv_settings)
        lbv.setContentsMargins(0, 0, 0, 0)
        lbv.refresh_items()
        layout.addWidget(lbv, 5)
        buttons_layout = QHBoxLayout()
        buttons_layout.setContentsMargins(0, 0, 0, 0)
        back = FlatButton("Back")
        back.clicked.connect(lambda: self.open_menu("main"))
        buttons_layout.addWidget(back)
        back.setMaximumHeight(100)
        layout.addLayout(buttons_layout)
        i = self.add_to_stack(layout)
        self.menus["load_app"] = i
    
    def create_install_app_menu(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(5)
        install_button = FlatButton("Install App(s)")
        install_button.clicked.connect(self.install_apps)
        layout.addWidget(install_button)
        back = FlatButton("Back")
        back.clicked.connect(lambda: self.open_menu("main"))
        layout.addWidget(back)
        i = self.add_to_stack(layout)
        self.menus["install_app"] = i
    
    def create_settings_menu(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(5)
        scroll_area = QScrollArea()
        layout1 = QVBoxLayout()
        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(5)
        setting1 = FlatButton("Setting 1")
        setting1.clicked.connect(lambda: print("Setting 1 clicked"))
        layout1.addWidget(setting1)
        back = FlatButton("Back")
        back.clicked.connect(lambda: self.open_menu("main"))
        scroll_area.setLayout(layout1)
        scroll_area.setWidgetResizable(False)
        layout.addWidget(scroll_area)
        layout.addWidget(back)
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
        callbacks = [lambda: self.open_menu("load_app"), lambda: self.open_menu("settings"), lambda: self.open_menu("install_app"), lambda: self.open_menu("exit")]
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
        self.create_load_app_menu()
        self.create_install_app_menu()
        self.create_settings_menu()
        self.create_exit_menu()
    
    def __init__(self, width: int, height: int):
        super().__init__()
        self.setWindowTitle("HackZero")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setGeometry(10, 10, width, height)
        if "--fullscreen" in sys.argv:
            self.showFullScreen()
        
        self.main_layout = QStackedLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        self.menus = {}
        self.create_menus()
        
        self.setLayout(self.main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main(720, 480)
    main.show()
    sys.exit(app.exec_())