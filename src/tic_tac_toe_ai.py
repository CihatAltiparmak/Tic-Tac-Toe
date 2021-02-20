from math import inf

class player:
  you = 'X'
  computer = 'O'
  
class move:
  x = -1
  y = -1
  val = -inf
  
def control(board):
    # horizontal control
    for i in range(3):
        if(board[i][0] == '_'):
            continue
        if(board[i][0] == board[i][1] and board[i][1] == board[i][2]):
            if(board[i][0] == player.you):
                return -1
            else:
                return 1
         
    # vertical control
    for i in range(3):
        if(board[0][i] == '_'):
            continue
        if(board[0][i] == board[1][i] and board[1][i] == board[2][i]):
            if(board[0][i] == player.you):
                return -1
            else:
                return 1
     
    # cross control
    if(board[0][0] != '_' and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        if(board[0][0] == player.you):
            return -1
        else:
            return 1
  
    if(board[0][2] != '_' and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        if(board[2][0] == player.you):
            return -1
        else:
            return 1 

    return 0

  
def minimax(board, p, depth, alpha, beta):
    score = control(board)
    best = move()
    
    if(depth == 0 or score != 0):
        best.val = score
        return best

    if(p == player.you):
        best.val = inf
        
    for i in range(3):
        for j in range(3):
            if(board[i][j] != "_"):
                continue

            if(p == player.computer):
                board[i][j] = player.computer
                move_val = minimax(board, player.you, depth - 1, alpha, beta).val
                    
                if(move_val > best.val):
                    best.val = move_val
                    best.x = i
                    best.y = j
                    
                alpha = max(alpha, move_val)
                if(alpha >= beta):
                    board[i][j] = '_'
                    return best
                    
            else:
                board[i][j] = player.you
                move_val = minimax(board, player.computer, depth - 1, alpha, beta).val
                
                if(move_val < best.val):
                    best.val = move_val
                    best.x = i
                    best.y = j
                    
                beta = min(beta, move_val)
                if(alpha >= beta):
                    board[i][j] = '_'
                    return best
                    
            board[i][j] = '_'
            
    return best


board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]   


def test(board, n, m):
    for i in range(3):
        for j in range(3):
            if(board[i][j] != '_'):
                continue
      
            board[i][j] = 'X'
            m.append((i, j))
            if(n > 1):
                ai_move = minimax(board, player.computer, n - 1, -inf, inf)
                board[ai_move.x][ai_move.y] = 'O'
                m.append((ai_move.x, ai_move.y))
            if(control(board) == -1):
                for k in board:
                    print(k)
                print(m)
                print("Computer lost.")
                print("Mission failed.")
                exit()
            test(board, n - 2, m)
            board[i][j] = '_'


if __name__ == '__main__':
    test(board, 9, [])
    print("Computer didn't lose.")
    print("Mission succesful.")
