import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy, QLabel

class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora PyQt5')
        self.setFixedSize(400,450)

        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.setCentralWidget(self.cw)

        self.display = QLineEdit()
        self.label = QLabel()
        self.grid.addWidget(self.display, 0, 0, 1, 4)
        
        self.display.setDisabled(True)
        self.display.setStyleSheet('*{background: green;color: #000; font-size: 30px;}')

        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.botoes(QPushButton('%'), 1, 0, 1, 1)
        self.botoes(QPushButton('C'), 1, 1, 1, 1)
        self.botoes(QPushButton('<-'), 1, 2, 1, 1)
        self.botoes(QPushButton('/'), 1, 3, 1, 1)



        self.botoes(QPushButton('7'), 2, 0, 1, 1)
        self.botoes(QPushButton('8'), 2, 1, 1, 1)
        self.botoes(QPushButton('9'), 2, 2, 1, 1)
        self.botoes(QPushButton('x'), 2, 3, 1, 1)
        

        self.botoes(QPushButton('4'), 3, 0, 1, 1)
        self.botoes(QPushButton('5'), 3, 1, 1, 1)
        self.botoes(QPushButton('6'), 3, 2, 1, 1)
        self.botoes(QPushButton('-'), 3, 3, 1, 1)
        

        self.botoes(QPushButton('1'), 4, 0, 1, 1)
        self.botoes(QPushButton('2'), 4, 1, 1, 1)
        self.botoes(QPushButton('3'), 4, 2, 1, 1)
        self.botoes(QPushButton('+'), 4, 3, 1, 1)
        

        self.botoes(QPushButton('+/-'), 5, 0, 1, 1)
        self.botoes(QPushButton('0'), 5, 1, 1, 1)
        self.botoes(QPushButton(','), 5, 2, 1, 1)
        self.botoes(QPushButton('='), 5, 3, 2, 1)
        
        self.grid.addWidget(self.label, 6, 0, 1, 3)
        self.label.setText('Hello Word')
        self.label.setStyleSheet("background-color:firebrick; border-radius:50px")
        
        

    def botoes(self, botao,linha,coluna, rowspan, colspan):
        self.grid.addWidget(botao,linha,coluna,rowspan,colspan)
        botao.clicked.connect(
            lambda: self.display.setText(self.display.text() + botao.text())
        )
        botao.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)




if __name__=='__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
