import sys
from PySide6.QtWidgets import QWidget,QApplication,QMainWindow,QVBoxLayout,QHBoxLayout,QGridLayout, QStackedLayout
from PySide6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        
        self.setWindowTitle("My App")
        
        layout = QStackedLayout()

        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("yellow"))

        layout.setCurrentIndex(1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
       
        
        
        
        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)
        
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)   
           
 
 
       
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()