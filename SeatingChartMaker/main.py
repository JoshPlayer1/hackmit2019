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

# class draggableRect(

if __name__ == "__main__":
        app = QtWidgets.QApplication([])
        scene = QtWidgets.QGraphicsScene(0, 0, 600, 500)
        scene.addRect(0,0,500,500)
        scene.addRect(510, 0, 100, 500)
        scene.setBackgroundBrush(QtGui.QBrush(QtGui.QColor("red")))
        scene.addRect(520, 10, 80, 50, pen=QtGui.QPen(QtGui.QColor("blue")), brush=QtGui.QBrush(QtGui.QColor("blue")))
        view = QtWidgets.QGraphicsView()
        view.setGeometry(0, 0, 650, 650)
        view.setScene(scene)
        view.show()
        sys.exit(app.exec_())
