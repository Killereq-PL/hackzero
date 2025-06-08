from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ListButtonViewItem(QPushButton):
    def __init__(self, data: list[dict], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._data = data
        self.hlayout = QHBoxLayout()
        self.hlayout.setContentsMargins(0, 0, 0, 0)
        self.hlayout.setSpacing(5)
        self.setLayout(self.hlayout)
        self.create_data_view()
        self.setMinimumHeight(134)
        self.setMaximumHeight(134)
        self.setStyleSheet('''
            QPushButton {
                background-color: #e1e1e1;
                color: #000000;
                padding: 50px 10px;
                font-size: 22px;
            }
            QPushButton:hover {
                background-color: #ff9428;
            }
            QPushButton:pressed {
                background-color: #b95c00;
            }
        ''')
    
    def create_data_view(self):
        if 'icon' in self._data:
            icon = self._data['icon']
            if isinstance(icon, str):
                icon = QPixmap(icon)
                icon_label = QLabel()
                icon_label.setPixmap(icon.scaledToHeight(128, mode=Qt.TransformationMode.FastTransformation))
                self.hlayout.addWidget(icon_label)
        for key, value in self._data.items():
            if key == 'icon':
                continue
            elif key == 'category':
                continue
            else:
                text = value
                label = QLabel(text)
                label.setStyleSheet("font-size: 18px; color: #000000;")
                self.hlayout.addWidget(label)