from PyQt5.QtWidgets import QPushButton, QHBoxLayout
from PyQt5.QtGui import QImage

class ListButtonViewItem(QPushButton):
    def __init__(self, data: list[dict], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._data = data
        self.hlayout = QHBoxLayout()
        self.hlayout.setContentsMargins(0, 0, 0, 0)
        self.hlayout.setSpacing(5)
        self.setLayout(self.hlayout)
        self.create_data_view()        
        self.setStyleSheet("""
            QPushButton {
                background-color: #ffffff;
                color: #000000;
                border: solid 1px #ff8000;
                padding: 50px 10px;
                font-size: 22px;
                margin: 0px;
            }
            QPushButton:hover {
                background-color: #ff9428;
            }
            QPushButton:pressed {
                background-color: #b95c00;
            }
        """)
    
    def create_data_view(self):
        for key, value in self._data.items():
            if key == 'icon':
                icon = value
                if isinstance(icon, str):
                    icon = QImage(icon)
            elif key == 'category':
                category = value
            else:
                text = value
                self.setText(text)