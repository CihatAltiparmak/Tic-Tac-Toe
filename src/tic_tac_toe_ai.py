from math import inf
def control(board, player, computer):
  # horizontal control
  for i in range(3):
    if(board[i][0] == '_'):
      continue
    if(board[i][0] == board[i][1] and board[i][1] == board[i][2]):
      if(board[i][0] == player):
        return -1
      else:
        return 1
         
  # vertical control
  for i in range(3):
    if(board[0][i] == '_'):
      continue
    if(board[0][i] == board[1][i] and board[1][i] == board[2][i]):
      if(board[0][i] == player):
        return -1
      else:
        return 1
     
  # cross control
  if(board[0][0] != '_' and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
    if(board[0][0] == player):
      return -1
    else:
      return 1
  
  if(board[0][2] != '_' and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
    if(board[2][0] == player):
      return -1
    else:
      return 1 

  return 0


def minimax(board, isMax, depth, computer, player):
  score = control(board, player, computer)
  
  if(depth == 0 or score != 0):
    return score

  if(isMax):
    best = -inf
  else:
    best = inf
    
  for i in range(3):
    for j in range(3):
      if(board[i][j] != "_"):
        continue

      if(isMax):
        board[i][j] = computer
        best = max(best, minimax(board, False, depth - 1, computer, player))
      else:
        board[i][j] = player
        best = min(best, minimax(board, True, depth - 1, computer, player))
      board[i][j] = '_'
  return best

def find_the_best_move(board, computer, player, n):
  moves = []
  for i in range(3):
    for j in range(3):
      if(board[i][j] != '_'):
        continue
      
      board[i][j] = computer
      moves.append((minimax(board, False, n - 1, computer, player),(i, j)))
      board[i][j] = '_'
      
  return max(moves)[1]

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
        ai_move = find_the_best_move(board, 'O', 'X', n - 1)
        board[ai_move[0]][ai_move[1]] = 'O'
        m.append(ai_move)
      if(control(board, 'X', 'O') == -1):
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








  
