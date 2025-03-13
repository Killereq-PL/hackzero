import os, sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class FlatButton(QPushButton):
    def __init__(self, text, *args, **kwargs):
        super().__init__(text, *args, **kwargs)
        # Button style
        self.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                padding: 30px 20px;
                font-size: 24px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton:pressed {
                background-color: #114e8a;
            }
        """)

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
    
    def exit_to_shell(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        btn1 = FlatButton(f"Exit")
        btn1.setFont(QFont("Arial", 14))
        btn1.clicked.connect(exit)
        btn2 = FlatButton(f"Shut Down")
        btn2.setFont(QFont("Arial", 14))
        #btn2.clicked.connect()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
    
    def __init__(self):
        super().__init__()
        
        # Window setup
        self.setWindowTitle("HackZero")
        self.setGeometry(0, 0, 480, 360)
        
        # Layout setup
        self.glayout = QGridLayout()
        self.glayout.setContentsMargins(20, 20, 20, 20)
        self.glayout.setSpacing(5)
        
        buttons = ["Load App", "Settings", "Install App(s)", "Exit/Power"]
        callbacks = [self.load_app, self.settings, self.install_apps, self.exit_to_shell]
        rows = 2
        # Create buttons
        for i in range(len(buttons)):
            btn = FlatButton(f"{buttons[i]}")
            btn.setFont(QFont("Arial", 14))
            btn.clicked.connect(callbacks[i])
            col = 0 if i < rows else 1
            row = i if i < rows else i - rows
            self.glayout.addWidget(btn, row, col)
        
        self.setLayout(self.glayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())