from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, \
                            QMainWindow, QDialog
from PyQt5.QtCore import Qt

from math import inf

# binding
from ui import tic_tac_toe_ui, game_result_dialog, \
               move_warning_dialog
import tic_tac_toe_ai as ai


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.player = 'X'
        self.computer = 'O'
        self.move_count = 9
        
        self.scores = {
                        self.computer : 0,
                        self.player : 0
                      }
        self.board = [
                       ['_', '_', '_'],
                       ['_', '_', '_'],
                       ['_', '_', '_']
                     ]
        
        self.init_ui()
        
    def init_ui(self):
        self.app_ui = tic_tac_toe_ui.Ui_MainWindow()
        self.app_ui.setupUi(self)
        self.game_places =  [ [self.app_ui.xy11, self.app_ui.xy12, self.app_ui.xy13],
                              [self.app_ui.xy21, self.app_ui.xy22, self.app_ui.xy23],
                              [self.app_ui.xy31, self.app_ui.xy32, self.app_ui.xy33]
                            ]

        for i in range(3):
            for j in range(3):
                self.game_places[i][j].mouseReleaseEvent = self.map_func(i, j)

        self.result_dialog = QDialog()
        self.result_dialog.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.notification = game_result_dialog.Ui_Dialog()
        self.notification.setupUi(self.result_dialog)
        self.notification.new_game_button.clicked.connect(self.create_new_game)
        self.notification.exit_button.clicked.connect(self.exit_game)

        self.warning_dialog = QDialog()
        self.warning_ui = move_warning_dialog.Ui_Dialog()
        self.warning_ui.setupUi(self.warning_dialog)
        self.warning_ui.ok_button.clicked.connect(self.warning_dialog.close)

    def map_func(self, i, j):
        def wrapper(event):
            if(self.board[i][j] != '_'):
                self.warning_dialog.show()
                self.warning_dialog.exec_()
                return
            self.board[i][j] = self.player
            self.game_places[i][j].setText(self.player)

            self.move_count -= 1

            if(self.move_count > 0):
                
                ai_move = ai.minimax(self.board, 'O', self.move_count, -inf, inf)
                x, y = ai_move.x, ai_move.y
                self.board[x][y] = self.computer
                self.game_places[x][y].setText(self.computer)
                self.move_count -= 1
          
            score = ai.control(self.board)
            if(score == 1):
                self.scores[self.computer] += 3
                self.app_ui.player2_label.setText("Computer: " + str(self.scores[self.computer]))
                self.create_result_notification("Computer won.")
            elif(score == -1):
                self.scores[self.player] += 3
                self.app_ui.player1_label.setText("You: " + str(self.scores[self.player]))
                self.create_result_notification("You won.")
            elif(self.move_count == 0):
                self.scores[self.computer] += 1
                self.scores[self.player] += 1
                self.app_ui.player2_label.setText("Computer: " + str(self.scores[self.computer]))
                self.app_ui.player1_label.setText("You: " + str(self.scores[self.player]))
                self.create_result_notification("Draw.")
                
        return wrapper

    def create_result_notification(self, message):
        self.notification.result_label.setText(message)
        self.result_dialog.show()
        self.result_dialog.exec_()

    def create_new_game(self):
        self.player = 'X'
        self.computer = 'O'
        self.move_count = 9
        self.board = [
                       ['_', '_', '_'],
                       ['_', '_', '_'],
                       ['_', '_', '_']
                     ]
        for i in range(3):
            for j in range(3):
                self.game_places[i][j].setText("")
        self.result_dialog.close()

    def exit_game(self):
        self.result_dialog.close()
        self.close()
    
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    splashScreen = MainWindow()
    # splashScreen.setWindowIcon(QIcon("indir.png"))
    splashScreen.show()
    sys.exit(app.exec_())
