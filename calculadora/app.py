#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy, QLabel
from PyQt5.QtCore import Qt


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora PyQt5')
        self.setFixedSize(400,450)

        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.setCentralWidget(self.cw)

        # --- Tela da Calculadora --- #
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setDisabled(True)
        
        # --- Label para Rodapé --- #
        self.label = QLabel()
        self.grid.addWidget(self.display, 0, 0, 1, 4)
        
       
        # --- Estilizando o Display --- #
        self.display.setStyleSheet('*{background: black;color: green; font-size: 40px; font-family:DS-Digital;}')
        self.cw.setStyleSheet('*{background: grey;}')
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        
        # --- Estilizando os botões --- #
        self.botoes(QPushButton("C"), 1, 0, 1, 1,lambda:self.btn_action("C"),'background:#F3D13F; font-weight:700; font-size:20px;')
        self.botoes(QPushButton(u'\u00AB'), 1, 1, 1, 1, lambda: self.display.setText(self.display.text()[:-1]),'font-size:20px;')
        self.botoes(QPushButton('%'), 1, 2, 1, 1,self.porcento,'font-size:20px;')
        self.botoes(QPushButton('/'), 1, 3, 1, 1,'','font-size:20px;')

        self.botoes(QPushButton('7'), 2, 0, 1, 1,lambda:self.btn_action("7"),'font-size:20px; background:lightgray;')
        self.botoes(QPushButton('8'), 2, 1, 1, 1,lambda:self.btn_action("8"),'font-size:20px; background:lightgray;')
        self.botoes(QPushButton('9'), 2, 2, 1, 1,lambda:self.btn_action("9"),'font-size:20px; background:lightgray;')
        self.botoes(QPushButton('*'), 2, 3, 1, 1,'','font-size:20px;')        

        self.botoes(QPushButton('4'), 3, 0, 1, 1,lambda:self.btn_action("4"),'font-size:20px; background:lightgray;')
        self.botoes(QPushButton('5'), 3, 1, 1, 1,lambda:self.btn_action("5"),'font-size:20px; background:lightgray;')
        self.botoes(QPushButton('6'), 3, 2, 1, 1,lambda:self.btn_action("6"),'font-size:20px; background:lightgray;')
        self.botoes(QPushButton('-'), 3, 3, 1, 1,'','font-size:20px;')

        self.botoes(QPushButton('1'), 4, 0, 1, 1,lambda:self.btn_action("1"),'font-size:20px; background:lightgray;')
        self.botoes(QPushButton('2'), 4, 1, 1, 1,lambda:self.btn_action("2"),'font-size:20px; background:lightgray;')
        self.botoes(QPushButton('3'), 4, 2, 1, 1,lambda:self.btn_action("3"),'font-size:20px; background:lightgray;')
        self.botoes(QPushButton('+'), 4, 3, 1, 1,'','font-size:20px;')
        
        self.botoes(QPushButton('.'), 5, 0, 1, 1,lambda:self.ponto(),'font-size:20px;')
        self.botoes(QPushButton('0'), 5, 1, 1, 1,lambda:self.btn_action("0"),'font-size:20px; background:lightgray;')
        self.botoes(QPushButton('='), 5, 2, 1, 2,self.calcular,'font-size:20px;')
        
        # --- Estilizando o Rodapé --- #
        self.grid.addWidget(self.label, 6, 0, 1, 4)
        self.label.setText('Created by @Alex')
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.label.setStyleSheet(
            "background-color:#B0C4DE; \
             border-radius:50px; \
             font-size: 20px; \
             color: white; \
             font-weight: bold;\
             padding-left: 100px")
        
# --- DEFINE POSIÇÕES (LINHAS E COLUNAS) PARA OS BOTÕES --- #
    def botoes(self, botao,linha,coluna, rowspan, colspan,funcao=None, style=None):
        self.grid.addWidget(botao,linha,coluna,rowspan,colspan)
        if not funcao:
            botao.clicked.connect(
                lambda: self.display.setText(self.display.text() + botao.text())
            )
        else:
            botao.clicked.connect(funcao)
        if style:
            botao.setStyleSheet(style)

        botao.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

# --- Função para calcular as operações SIMPLES usando o método "eval" --- #  
    def calcular(self):

        tela = self.display.text()
        if 'ERROR' in tela:
            self.display.setText("")

        try:
            tela = self.display.text()
            outro = eval(tela)

            self.display.setText(str(outro))
            
        except Exception as error:
            self.display.setText('ERROR')

# --- Função para calcular Porcentagem --- #
    def porcento(self):
        
        tela = self.display.text()

        if 'ERROR' in tela:
            self.display.setText("")

        try:

            if "*" in tela:
                num_list = tela.split("*")
                num1 =float(num_list[0])
                num2 =float(num_list[1]) 
                porcentagem = (num1 /100) * num2
                result = porcentagem
            
            elif "/" in tela:
                num_list = tela.split("/")
                num1 =float(num_list[0])
                num2 =float(num_list[1]) 
                porcentagem = (num1 * 100) / num2
                result = porcentagem

            elif "-" in tela:
                num_list = tela.split("-")
                num1 =float(num_list[0])
                num2 =float(num_list[1]) 
                porcentagem = (num1 / 100) * num2
                result = num1 - porcentagem

            elif "+" in tela:
                num_list = tela.split("+")
                num1 =float(num_list[0])
                num2 =float(num_list[1]) 
                porcentagem = (num1 / 100) * num2
                result = num1 + porcentagem

            
            self.display.setText('{:.2f}'.format(result))
            
        except Exception as error:
            self.display.setText('ERROR')

# --- Manipulando decimais --- #        
    def ponto(self):

        tela = self.display.text()

        if 'ERROR' in tela:
            self.display.setText("")
        
        num_list = tela.split("+")
        
        if "+" in tela and "." not in num_list[-1]:
            self.display.setText(f'{tela}.')
        elif "." in tela:
            pass    
        else:
            self.display.setText(f'{tela}.')

    def btn_action(self,btn_press):
        tela = self.display.text()
        if 'ERROR' in tela:
            self.display.setText("")

        if btn_press == "C":
            self.display.setText("0")
        else:
            if self.display.text() == "0":
                self.display.setText("")
            self.display.setText(f'{self.display.text()}{btn_press}')


if __name__=='__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
