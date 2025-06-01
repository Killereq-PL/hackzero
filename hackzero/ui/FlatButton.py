from PyQt5.QtWidgets import QPushButton

class FlatButton(QPushButton):
    def __init__(self, text, *args, **kwargs):
        super().__init__(text, *args, **kwargs)
        self.setStyleSheet("""
            QPushButton {
                background-color: #ff8000;
                color: white;
                border: none;
                padding: 80px 10px;
                font-size: 52px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #ff9428;
            }
            QPushButton:pressed {
                background-color: #b95c00;
            }
        """)