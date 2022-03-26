import os
import sys
from time import sleep

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox


class GameBoard():
    def __init__(self):
        self.table = [['-1' for _ in range(3)] for _ in range(3)]
        self.turn = 0
    
    def __repr__(self):
        res = ''
        for line in self.table:
            res += ''.join(map(str, line)) + '\n'
        return res

    def change_cell(self, id):
        # print(self.table[id%3][id//3])
        if self.table[id // 3][id % 3] == '-1':
            self.table[id // 3][id % 3] = "X" if self.turn == 0 else "O"
            self.turn = 1 if self.turn == 0 else 0
            return 1
        # print(self.turn)
        return 0

    def check_victory(self):
        for line in self.table:
            if len(set(line)) == 1 and set(line) != set(["-1"]):
                print("1", set(line), set('-1'))
                return True
            else:
                print(set(line))

        column = set()
        for i in range(3):
            for j in range(3):
                column.add(self.table[j][i])
            if len(column) == 1 and column != set(["-1"]):
                print("2")
                return True

        column = set()
        for i in range(3):
            column.add(self.table[i][i])
        if len(column) == 1 and column != set(["-1"]):
            print("3")
            return True
        
        column = set()
        for i in range(3):
            column.add(self.table[i][2-i])
        if len(column) == 1 and column != set(["-1"]):
            print("4")
            return True
        
        return False    



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
    
        self.setWindowTitle("amogus")
        self.setGeometry(700, 300, 500, 500)
        self.gb = GameBoard()
        self.buttons = []
        for i in range(9):
            new_button = QtWidgets.QPushButton(self)
            new_button.move(70 + 120 * (i % 3), 70 + 120 * (i // 3))
            new_button.setFixedSize(120, 120)
            new_button.clicked.connect(lambda checked, i=i: self.change_box(i))
            self.buttons.append(new_button)
        

    def change_box(self, id):
        res = self.gb.change_cell(id)
        if res:
            self.buttons[id].setText(str(self.gb.table[id//3][id%3]))
            if self.gb.check_victory() == True:
                won = "X" if self.gb.turn else "O"
                v = VictoryWindow(won)
                v.show()
                v.exec_()
                self.close()
            else:
                print("thinking")
        else:
            print("wtf")
        


class VictoryWindow(QMessageBox):
    def __init__(self, won="X"):
        super(VictoryWindow, self).__init__()
        self.setFixedSize(250, 200)
        self.setWindowTitle("congrats")
        self.setText(won + " won. good.")


def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
