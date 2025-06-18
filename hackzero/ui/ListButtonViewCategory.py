from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLabel
from PyQt5.QtCore import Qt

class ListButtonViewCategory(QWidget):
    def __init__(self, category: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.category = category
        self.header = QPushButton(category)
        arrow_layout = QHBoxLayout()
        arrow_layout.setContentsMargins(0, 0, 0, 0)
        arrow_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.arrows = ["⮝", "⮟"]
        self.arrow = QLabel(self.arrows[1])
        self.arrow.setStyleSheet('font-size: 32px; font-weight: bold; padding: 10px; color: white;')
        arrow_layout.addWidget(self.arrow)
        self.header.setLayout(arrow_layout)
        self.header.setStyleSheet('''
        QPushButton {
            font-size: 32px;
            font-weight: bold;
            padding: 10px;
            background-color: #ff8000;
            color: white;
            border: none;
            margin: 5px 0px;
        }
        QPushButton:hover {
            background-color: #ff9428;
        }
        QPushButton:pressed {
            background-color: #b95c00;
        }
        ''')
        self.header.setEnabled(True)
        self.header.setMinimumHeight(65)
        self.header.setMaximumHeight(65)
        self.vlayout = QVBoxLayout()
        self.vlayout.setContentsMargins(0, 0, 0, 0)
        self.vlayout.setSpacing(5)
        self.vlayout.addWidget(self.header)
        self.hcategory_names_layout = QHBoxLayout()
        self.hcategory_names_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.vlayout)
        self.shown = True
        self.header.clicked.connect(self.toggle_category)
        self.buttons = []
        self.set_shown(True)
    
    def toggle_category(self):
        set_shown = not self.shown
        self.set_shown(set_shown)
    
    def add_button(self, button):
        self.vlayout.addWidget(button)
        self.buttons.append(button)
        self.set_shown(self.shown)
    
    def set_shown(self, value: bool):
        for x in self.buttons:
            if value:
                x.show()
            else:
                x.hide()
            x.setEnabled(value)
        self.hcategory_names_layout.setEnabled(value)
        self.arrow.setText(self.arrows[1 if value else 0])
        self.shown = value