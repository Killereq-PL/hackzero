import os
from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QStackedLayout, QScrollArea, QGraphicsBlurEffect
from PyQt5.QtGui import QFont
from hackzero.ui.FlatButton import FlatButton
from hackzero.ui.ListButtonView import ListButtonView
from hackzero.db.AppsDB import AppsDB

class AbstractMenu:
    id: str = ""
    def add_to_stack(self, main, layout) -> None:
        i = main.add_to_stack(layout)
        main.menus[self.id] = i
    def create(self, main: QWidget) -> None:
        pass # dummy function

class Main(AbstractMenu):
    id = "main"
    def create(self, main: QWidget) -> None:
        # Layout setup
        glayout = QGridLayout()
        glayout.setContentsMargins(20, 20, 20, 20)
        glayout.setSpacing(5)
        
        buttons = ["Load App", "Settings", "Install App(s)", "Exit/Power"]
        callbacks = [lambda: main.open_menu("load_app"), lambda: main.open_menu("settings"), lambda: main.open_menu("install_app"), lambda: main.open_menu("exit")]
        rows = 2
        # Create buttons
        for i in range(len(buttons)):
            btn = FlatButton(f"{buttons[i]}")
            btn.clicked.connect(callbacks[i])
            col = 0 if i < rows else 1
            row = i if i < rows else i - rows
            glayout.addWidget(btn, row, col)
        self.add_to_stack(main, glayout)

class LoadApp(AbstractMenu):
    id = "load_app"
    def create(self, main: QWidget) -> None:
        def load_app(self) -> None:
            print("Load App")
        stacked_layout = QStackedLayout()
        stacked_layout.setContentsMargins(0, 0, 0, 0)
        stacked_layout.setStackingMode(QStackedLayout.StackingMode.StackAll)
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(5)
        '''
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
            }
        }
        '''
        apps_db = AppsDB()
        lbv_data = []
        for x in apps_db.get_apps():
            id           = x[0]
            name         = x[1]
            description  = x[2]
            category     = x[3]
            author       = x[4]
            version      = x[5]
            icon_path    = x[6]
            path         = x[7]
            installed_at = x[8]
            updated_at   = x[9]
            
            lbv_data.append({
                'title': name,
                'description': description,
                'category': category,
                'author': author,
                'version': version,
                'icon': "icon128.png" if icon_path == None or icon_path == "" else os.path.join(path, icon_path),
            })
        lbv_settings = {
            'categories': {
                'Examples': {
                    'columns': {
                        'title': {'width': 200},
                        'description': {'width': 400}
                    },
                    'shown': True
                }
            }}
        lbv = ListButtonView(lbv_data, True, lbv_settings)
        lbv.setContentsMargins(0, 0, 0, 0)
        lbv.refresh_items()
        layout.addWidget(lbv, 5)
        buttons_layout = QHBoxLayout()
        buttons_layout.setContentsMargins(0, 0, 0, 0)
        back = FlatButton("Back")
        back.clicked.connect(lambda: main.open_menu("main"))
        buttons_layout.addWidget(back)
        back.setMaximumHeight(100)
        layout.addLayout(buttons_layout)
        widget1 = QWidget()
        widget1.setLayout(layout)
        
        popup_layout = QVBoxLayout()
        popup_layout.setContentsMargins(20, 20, 20, 20)
        button1 = FlatButton("Load App")
        button2 = FlatButton("Configure App")
        button3 = FlatButton("Cancel")
        popup_layout.addWidget(button1)
        popup_layout.addWidget(button2)
        popup_layout.addWidget(button3)
        popup_style = """
            QPushButton {
                background-color: #444;
                color: white;
                border: none;
                padding: 20% 10%;
                font-size: 36px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #555;
            }
            QPushButton:pressed {
                background-color: #333;
            }
            QPushButton:disabled {
                background-color: #333;
                color: #666666;
            }
            QPushButton:focus {
                outline: none;
                background-color: #555;
            }
        """
        button1.setStyleSheet(popup_style)
        button2.setStyleSheet(popup_style)
        button3.setStyleSheet(popup_style)
        blur = QGraphicsBlurEffect()
        blur.setBlurRadius(0)
        blur.setBlurHints(QGraphicsBlurEffect.BlurHint.QualityHint)
        widget1.setGraphicsEffect(blur)
        widget2 = QWidget()
        widget2.setLayout(popup_layout)
        widget2.setStyleSheet("background-color: rgba(0, 0, 0, 0.7);")
        widget2.hide()
        button1.clicked.connect(lambda: load_app())
        button2.clicked.connect(lambda: print("Configure App clicked"))
        def hide_popup():
            widget2.hide()
            blur.setBlurRadius(0)
        
        def show_popup(self, item):
            widget2.show()
            blur.setBlurRadius(10)
            button1.setText(f"Load {item.data['title']}")
        button3.clicked.connect(lambda: hide_popup())
        lbv.set_button_callback(lambda item: show_popup(main, item))
        
        stacked_layout.addWidget(widget1)
        stacked_layout.addWidget(widget2)
        self.add_to_stack(main, layout)

class InstallApp(AbstractMenu):
    id = "install_app"
    def create(self, main: QWidget) -> None:
        def install_apps(self) -> None:
            print("Install App(s)")
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(5)
        install_button = FlatButton("Install App(s)")
        install_button.clicked.connect(install_apps)
        layout.addWidget(install_button)
        back = FlatButton("Back")
        back.clicked.connect(lambda: main.open_menu("main"))
        layout.addWidget(back)
        self.add_to_stack(main, layout)

class Settings(AbstractMenu):
    id = "settings"
    def create(self, main: QWidget) -> None:
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(5)
        scroll_area = QScrollArea()
        container = QWidget()
        layout1 = QVBoxLayout()
        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(5)
        setting1 = FlatButton("Screen Resolution")
        setting1.clicked.connect(lambda: main.open_menu("settings_screen_adjust"))
        setting2 = FlatButton("Bluetooth Settings")
        setting2.clicked.connect(lambda: main.open_menu("settings_bluetooth"))
        layout1.addWidget(setting1)
        layout1.addWidget(setting2)
        back = FlatButton("Back")
        back.clicked.connect(lambda: main.open_menu("main"))
        container.setLayout(layout1)
        scroll_area.setWidget(container)
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area)
        layout.addWidget(back)
        self.add_to_stack(main, layout)

class Settings_ScreenAdjust(AbstractMenu):
    id = "settings_screen_adjust"
    def create(self, main: QWidget) -> None:
        # MENU 1 : SCREEN RESOLUTION ADJUST
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(5)
        grid_layout = QGridLayout()
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setSpacing(5)
        def change_resolution(resolution_label, deltax, deltay):
            main.setGeometry(main.x(), main.y(), main.width()+deltax, main.height()+deltay)
            resolution_label.setText(f"{main.width()}x{main.height()}")
        resolution_label = FlatButton(f"720x480")
        resolution_label.setEnabled(False)
        left = FlatButton("Left")
        left.clicked.connect(lambda: change_resolution(resolution_label, -10, 0))
        right = FlatButton("Right")
        right.clicked.connect(lambda: change_resolution(resolution_label, 10, 0))
        up = FlatButton("Up")
        up.clicked.connect(lambda: change_resolution(resolution_label, 0, -10))
        down = FlatButton("Down")
        down.clicked.connect(lambda: change_resolution(resolution_label, 0, 10))
        grid_layout.addWidget(left, 1, 0)
        grid_layout.addWidget(right, 1, 2)
        grid_layout.addWidget(up, 0, 1)
        grid_layout.addWidget(down, 2, 1)
        grid_layout.addWidget(resolution_label, 1, 1)
        layout.addLayout(grid_layout)
        buttons_layout = QHBoxLayout()
        buttons_layout.setContentsMargins(0, 0, 0, 0)
        back = FlatButton("Back")
        back.clicked.connect(lambda: main.open_menu("main"))
        buttons_layout.addWidget(back)
        back.setMaximumHeight(100)
        layout.addLayout(buttons_layout)
        self.add_to_stack(main, layout)

class Settings_Bluetooth(AbstractMenu):
    id = "settings_bluetooth"
    def create(self, main: QWidget) -> None:
        # MENU 2 : BLUETOOTH SETTINGS
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(5)
        bluetooth_label = FlatButton("Bluetooth Settings")
        bluetooth_label.setEnabled(False)
        bluetooth_label.setFont(QFont("Arial", 26))
        bluetooth_label.setStyleSheet("color: white; background-color: #444; padding: 10px; border-radius: 5px;")
        layout.addWidget(bluetooth_label)
        bluetooth_info = FlatButton("Bluetooth is not available on this system.")
        bluetooth_info.setEnabled(False)
        bluetooth_info.setFont(QFont("Arial", 18))
        bluetooth_info.setStyleSheet("color: white; background-color: #333; padding: 10px; border-radius: 5px;")
        layout.addWidget(bluetooth_info)
        buttons_layout = QHBoxLayout()
        buttons_layout.setContentsMargins(0, 0, 0, 0)
        buttons_layout.setSpacing(5)
        buttons_layout.addStretch()
        buttons_layout.addWidget(FlatButton("Enable Bluetooth (Not Implemented)"))
        layout.addLayout(buttons_layout)
        back = FlatButton("Back")
        back.clicked.connect(lambda: main.open_menu("main"))
        layout.addWidget(back)
        self.add_to_stack(main, layout)

class Exit(AbstractMenu):
    id = "exit"
    def create(self, main: QWidget) -> None:
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(5)
        layout1 = QHBoxLayout()
        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(5)
        btn1 = FlatButton("Exit")
        btn1.clicked.connect(main.exit)
        btn2 = FlatButton("Shut Down")
        btn2.clicked.connect(main.shutdown)
        layout1.addWidget(btn1)
        layout1.addWidget(btn2)
        layout.addLayout(layout1)
        btn3 = FlatButton("Back")
        btn3.clicked.connect(lambda: main.open_menu("main"))
        layout.addWidget(btn3)
        self.add_to_stack(main, layout)

ALL: list = [
    Main(),
    LoadApp(),
    InstallApp(),
    Settings(),
    Settings_ScreenAdjust(),
    Settings_Bluetooth(),
    Exit()
]