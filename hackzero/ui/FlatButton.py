from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt

class FlatButton(QPushButton):
    def __init__(self, text: str = "Button", *args, **kwargs):
        super().__init__(text, *args, **kwargs)
        self.setStyleSheet("""
            QPushButton {
                background-color: #ff8000;
                color: white;
                border: none;
                padding: 30% 20%;
                font-size: 48px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #ff9428;
            }
            QPushButton:pressed {
                background-color: #b95c00;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
            QPushButton:focus {
                outline: none;
                background-color: #c46200;
            }
        """)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)