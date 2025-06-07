from PyQt5.QtWidgets import QAbstractButton
from PyQt5.QtCore import QSize, QRect, QPoint, Qt
from PyQt5.QtGui import QPainter, QTextOption, QImage

class ListButtonViewItem(QAbstractButton):
    def __init__(self, data: list[dict], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._data = data
        self.setCheckable(True)
    
    def sizeHint(self):
        return QSize(100, 100)

    def paintEvent(self, event):
        if not self.isVisible():
            return
        painter = QPainter(self)
        if self.isChecked():
            self.rect().adjust(2, 2, -2, -2)
        painter.fillRect(self.rect(), self.palette().button())
        painter.setPen(self.palette().buttonText().color())
        painter.setFont(self.font())
        counter = 0
        for x in self._data.items():
            if x[0] == "icon":
                painter.drawImage(self.rect(), QImage(x[1]))
            else:
                rect = QRect(QPoint(counter * 150, 0), QSize(self.width(), 50))
                painter.drawText(rect, 0, x[1])
                counter += 1
        painter.end()