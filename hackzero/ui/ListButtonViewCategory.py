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
        self.arrow = QLabel(self.arrows[0])
        self.arrow.setStyleSheet('font-size: 24px; font-weight: bold; padding: 10px; color: white;')
        arrow_layout.addWidget(self.arrow)
        self.header.setLayout(arrow_layout)
        self.header.setStyleSheet('''
        QPushButton {
            font-size: 24px;
            font-weight: bold;
            padding: 10px;
            background-color: #ff8000;
            color: white;
        }
        QPushButton:hover {
            background-color: #ff9428;
        }
        QPushButton:pressed {
            background-color: #b95c00;
        }
        ''')
        self.header.setEnabled(True)
        self.vlayout = QVBoxLayout()
        self.vlayout.setContentsMargins(0, 0, 0, 0)
        self.vlayout.setSpacing(5)
        self.vlayout.addWidget(self.header)
        self.setLayout(self.vlayout)
        self.shown = True
        self.header.clicked.connect(self.toggle_category)
    
    def toggle_category(self):
        set_shown = not self.shown
        self.set_shown(set_shown)
    
    def add_button(self, button):
        self.vlayout.addWidget(button)
    
    def set_shown(self, value: bool):
        for x in self.vlayout.children():
            if x != self.header:
                x.setVisible(value)
        self.arrow.setText(self.arrows[1 if value else 0])