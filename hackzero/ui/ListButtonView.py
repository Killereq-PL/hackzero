from PyQt5.QtWidgets import QScrollArea, QApplication, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

from hackzero.ui.ListButtonViewItem import ListButtonViewItem
from hackzero.ui.ListButtonViewCategory import ListButtonViewCategory

import sys

class ListButtonView(QScrollArea):
    def __init__(self, data : list = [], has_categories = False, settings : dict = {}, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setFrameShape(QScrollArea.Shape.NoFrame)
        self._current_item = None
        self.settings = settings
        self.has_categories = has_categories
        if has_categories:
            self._data : list[dict] = sorted(data, key=lambda x: x['category'])
        else:
            self._data : list[dict] = data
        self.buttons = []
        self.box_layout = QVBoxLayout()
        self.box_layout.setContentsMargins(0, 0, 0, 0)
        self.box_layout.setSpacing(0)
        self.container = QWidget()
        self.container.setLayout(self.box_layout)
        self.setWidget(self.container)
        self.setWidgetResizable(True)
        self.box_layout.setStretch(0, 0)
        self.box_layout.setStretch(1, 0)
        if has_categories:
            self.bgroups : dict[str, list[dict]] = {}
            for x in self._data:
                if 'category' in x.keys():
                    if x['category'] in self.bgroups.keys():
                        self.bgroups[x['category']].append(x)
                    else:
                        self.bgroups[x['category']] = []
                        self.bgroups[x['category']].append(x)
                else:
                    continue
        else:
            self.bgroups = self._data
    
    def clear(self):
        while self.box_layout.count():
            child = self.box_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    
    def refresh_items(self):
        self.clear()
        self.buttons.clear()
        if self.has_categories:
            for key, value in self.bgroups.items():
                category = ListButtonViewCategory(key)
                for x in value:
                    button = ListButtonViewItem(x)
                    category.add_button(button)
                    self.buttons.append(button)
                self.box_layout.addWidget(category)
        else:
            for x in self.bgroups:
                button = ListButtonViewItem(x)
                self.box_layout.addWidget(button)
                self.buttons.append(button)
    
    def add_item(self, item_data):
        self._data.append(item_data)
    
    def remove_item(self, item_data):
        self._data.remove(item_data)
    
    def update_item(self, item_data, new_item_data):
        if item_data in self._data:
            self._data[self._data.index(item_data)] = new_item_data
        else:
            self._data.append(new_item_data)
    
    def _btncallback(self, callback, button):
        self._current_item = button
        callback(button)
    
    def set_button_callback(self, callback):
        for button in self.buttons:
            button.clicked.connect(lambda: self._btncallback(callback, button))