from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QTimer, Qt
import sys
import random
# binding
import ui
import msg_box_player
import msg_box_opponnent
import msg_box_draw
import splash_screen


class MsgBoxDraw(QWidget, msg_box_draw.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MsgBoxPlayer(QWidget, msg_box_player.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        
class MsgBoxOpponnent(QWidget, msg_box_opponnent.Ui_Form):
    def __init__(self):
        super().__init__() 
        self.setupUi(self)       
  

class SplashScreen(QMainWindow, splash_screen.Ui_MainWindow):
    def __init__(self):
        super().__init__() 
        self.setupUi(self)
        
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.changeValue()
    
    def changeValue(self):   
        self.timer = QTimer()                                   
        self.timer.timeout.connect(self.changeValue)            
        self.timer.start(56)                                    
        self.progress_bar.setValue(self.progress_bar.value()+1)   
        
        if self.progress_bar.value() == 100:
            self.timer.stop()
            self.timer.singleShot(1600, lambda: self.close())
            self.main_window = MainWindow()
            self.main_window.show()


class MainWindow(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()
        
    def main(self):
        self.blocks = [
            [self.left_top_block, self.top_middle_block, self.top_right_block],            # Row 1
            [self.middle_left_block, self.middle_middle_block, self.middle_right_block],   # Row 2
            [self.bot_left_block, self.bot_middle_block, self.bot_right_block]             # Row 3
        ]
        self.release_events = [
            [lambda e: self.blocks[0][0].setText('X'), lambda e: self.blocks[0][1].setText('X'), lambda e: self.blocks[0][2].setText('X')],
            [lambda e: self.blocks[1][0].setText('X'), lambda e: self.blocks[1][1].setText('X'), lambda e: self.blocks[1][2].setText('X')], 
            [lambda e: self.blocks[2][0].setText('X'), lambda e: self.blocks[2][1].setText('X'), lambda e: self.blocks[2][2].setText('X')]
        ]
        self.locations = []
        for x in range(3):
            for y in range(3):
                self.locations.append((x, y))
        
        for tuple in self.locations:
            target = self.blocks[tuple[0]][tuple[1]]
            target.setReadOnly(True)
            target.mouseReleaseEvent = self.release_events[tuple[0]][tuple[1]]
            target.textChanged.connect(self.opponnent)
            target.textChanged.connect(self.winning_reactions)
            
# "Coordination" is meaning locations of the marks that appearing in the board.
        self.coordination = lambda: [[i.text() for i in self.blocks[0]], [i.text() for i in self.blocks[1]], [i.text() for i in self.blocks[2]]] 
    
    def winning_reactions(self):
        # Horizontal Win
        if self.coordination()[0] == ['O', 'O', 'O']:
            print('O HAS WON AS HORIZONTAL')
            
        elif self.coordination()[1] == ['O', 'O', 'O']:
            print('O HAS WON AS HORIZONTAL')
            
        elif self.coordination()[2] == ['O', 'O', 'O']:
            print('O HAS WON AS HORIZONTAL')
            
        # Vertical Win
        elif self.coordination()[0][0] == 'O' and self.coordination()[1][0] == 'O' and self.coordination()[2][0] == 'O':
            print('O HAS WON AS VERTICAL')
            
        elif self.coordination()[0][1] == 'O' and self.coordination()[1][1] == 'O' and self.coordination()[2][1] == 'O':
            print('O HAS WON AS VERTICAL')
            
        elif self.coordination()[0][2] == 'O' and self.coordination()[1][2] == 'O' and self.coordination()[2][2] == 'O':
            print('O HAS WON AS VERTICAL')
        # Cross Win
        elif self.coordination()[0][0] == 'O' and self.coordination()[1][1] == 'O' and self.coordination()[2][2] == 'O':
            print('O HAS WON AS CROSS')
        
        elif self.coordination()[0][2] == 'O' and self.coordination()[1][1] == 'O' and self.coordination()[2][0] == 'O':
            print('O HAS WON AS CROSS')
        # Draw 
        elif all(self.coordination()[0]) and all(self.coordination()[1]) and all(self.coordination()[2]):
            print('DRAW')
    
    def opponnent(self):
        print(self.coordination()[0], self.coordination()[1], self.coordination()[2], sep="\n", end=f"\n {10*'-'} \n")
        print(self.coordination())
        
        if self.coordination() != [['', '', ''], ['', 'X', ''], ['', '', '']]:
            self.blocks[1][1].setText('O')
        
        if self.coordination() == [['X', 'X', ''], ['', 'O', ''], ['', '', '']]:
            self.blocks[0][2].setText('O')
            
        if self.coordination() == [['X', 'X', 'O'], ['X', 'O', ''], ['', '', '']] or self.coordination() == [['X', 'X', 'O'], ['', 'O', 'X'], ['', '', '']] or self.coordination() == [['X', 'X', 'O'], ['', 'O', ''], ['', 'X', '']] or self.coordination() == [['X', 'X', 'O'], ['', 'O', ''], ['', '', 'X']]:
            self.blocks[2][0].setText('O')
            
        if self.coordination() == [['X', 'X', 'O'], ['', 'O', ''], ['X', '', '']]:
            self.blocks[1][0].setText('O')
            
        if self.coordination() == [['X', 'X', 'O'], ['O', 'O', ''], ['X', 'X', '']] or self.coordination() == [['X', 'X', 'O'], ['O', 'O', ''], ['X', '', 'X']]:
            self.blocks[1][2].setText('O')
            
        if self.coordination() == [['X', 'X', 'O'], ['O', 'O', 'X'], ['X', '', '']]:
            random.choice([self.blocks[2][1], self.blocks[2][2]]).setText('O')
        # Varyant Bitti
        
        if self.coordination() == [['X', '', 'X'], ['', 'O', ''], ['', '', '']]:
            self.blocks[0][1].setText('O')
        
        if self.coordination() == [['X', 'O', 'X'], ['X', 'O', ''], ['', '', '']] or self.coordination() == [['X', 'O', 'X'], ['', 'O', 'X'], ['', '', '']] or self.coordination() == [['X', 'O', 'X'], ['', 'O', ''], ['X', '', '']] or self.coordination() == [['X', 'O', 'X'], ['', 'O', ''], ['', '', 'X']]:
            self.blocks[2][1].setText('O')
            
        if self.coordination() == [['X', 'O', 'X'], ['', 'O', ''], ['', 'X', '']]:
            random.choice([self.blocks[1][0], self.blocks[1][2], self.blocks[2][0], self.blocks[2][2]]).setText('O')
            
        if self.coordination() == [['X', 'O', 'X'], ['X', 'O', 'O'], ['', 'X', '']]:
            self.blocks[2][0].setText('O')
            
        if self.coordination() == [['X', 'O', 'X'], ['O', 'O', 'X'], ['', 'X', '']]:
            self.blocks[2][2].setText('O')
            
        if self.coordination() == [['X', 'O', 'X'], ['X', 'O', ''], ['O', 'X', '']]:
            random.choice([self.blocks[1][2], self.blocks[2][2]]).setText('O')
            
        if self.coordination() == [['X', 'O', 'X'], ['', 'O', 'X'], ['O', 'X', '']]:
            self.blocks[2][2].setText('O')
            
        if self.coordination() == [['X', 'O', 'X'], ['', 'O', ''], ['O', 'X', 'X']]:
            self.blocks[1][2].setText('O')
            
        if self.coordination() == [['X', 'O', 'X'], ['X', 'O', ''], ['', 'X', 'O']]:
            self.blocks[2][0].setText('O')
            
        if self.coordination() == [['X', 'O', 'X'], ['', 'O', 'X'], ['', 'X', 'O']]:
            random.choice([self.blocks[1][0], self.blocks[2][0]]).setText('O')
        
        if self.coordination() == [['X', 'O', 'X'], ['', 'O', ''], ['X', 'X', 'O']]:
            self.blocks[1][0].setText('O')
        
        if self.coordination() == [['X', 'O', 'X'], ['', 'O', 'O'], ['X', 'X', '']]:
            self.blocks[1][0].setText('O')
            
        if self.coordination() == [['X', 'O', 'X'], ['', 'O', 'O'], ['', 'X', 'X']]:
            self.blocks[1][0].setText('O')
            
        if self.coordination() == [['X', 'O', 'X'], ['O', 'O', ''], ['X', 'X', '']]:
            self.blocks[1][2].setText('O')
            
        if self.coordination() == [['X', 'O', 'X'], ['O', 'O', ''], ['', 'X', 'X']]:
            self.blocks[1][2].setText('O')
            
        # varyant bitti ([0][1])
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    splashScreen = MainWindow()
    splashScreen.setWindowTitle("Tic Tac Toe")
    splashScreen.setWindowIcon(QIcon("indir.png"))
    splashScreen.show()
    sys.exit(app.exec_())
        
    
    