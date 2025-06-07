from PyQt5.QtWidgets import QScrollArea, QApplication, QVBoxLayout
#from hackzero.ui.ListButtonViewItem import ListButtonViewItem
from ListButtonViewItem import ListButtonViewItem
import sys

class ListButtonView(QScrollArea):
    def __init__(self, data: list[dict[str, str]] = [], has_icon = False, has_extra_data = False, has_categories = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.has_icon = has_icon
        self.has_extra_data = has_extra_data
        self.has_categories = has_categories
        self._data : list[dict] = data
        self.buttons = []
        self.box_layout = QVBoxLayout()
        self.box_layout.setSpacing(5)
        self.setLayout(self.box_layout)
        self.setWidgetResizable(False)
        if has_categories:
            self.bgroups : dict[str, list[dict]] = {}
            for x in self._data:
                if 'category' in x.keys():
                    if x['category'] in self.bgroups.keys():
                        self.bgroups[x['category']].append(x)
                    else:
                        self.bgroups[x['category']] = []
                else:
                    continue
        else:
            pass
    
    def clear(self):
        while self.box_layout.count():
            child = self.box_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    
    def refresh_items(self):
        self.clear()
        self.buttons.clear()
        for x in self._data:
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
    
    @property
    def item_index(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    lbv_data = [
        {
        'title': 'Example1',
        'icon': '../../icon48.png',
        'description': 'First Example',
        'category': 'Examples',
        },
        {
        'title': 'Example2',
        'icon': '../../icon48.png',
        'description': 'Second Example',
        'category': 'Examples',
        },
        {
        'title': 'Test1',
        'icon': '../../icon48.png',
        'description': 'First Test',
        'category': 'Tests',
        },
        {
        'title': 'Test2',
        'icon': '../../icon48.png',
        'description': 'Second Test',
        'category': 'Tests'
        }
    ]
    main = ListButtonView(lbv_data, True, True, True)
    main.setGeometry(100, 100, 848, 480)
    main.setContentsMargins(20, 20, 20, 20)
    main.refresh_items()
    main.show()
    sys.exit(app.exec_())