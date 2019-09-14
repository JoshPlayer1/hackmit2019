import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Seating Chart Maker Deluxe"
        self.top= 150
        self.left= 150
        self.width = 700
        self.height = 500
        self.InitWindow()
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

if __name__ == "__main__":
        app = QtWidgets.QApplication([])
        scene = QtWidgets.QGraphicsScene()
        scene.addText("Hello World!")
        scene.addRect(10, 10, 300, 30)
        # scene.setBackgroundBrush(QtGui.QBrush(QtGui.QColor("black")))
        view = QtWidgets.QGraphicsView(scene)
        view.show()
        sys.exit(app.exec_())
