#standard tic_tac_toe_game
gameboard = {1: ' ', 2: ' ', 3: ' ', 
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}

def printboard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])


def action():
    player = 'X'
    count = 0
    
    while (gameboard[1] == ' ' or gameboard[2] == ' ' or gameboard[3] == ' '
    or gameboard[4] == ' ' or gameboard[5] == ' ' or gameboard[6] == ' ' 
    or gameboard[7] == ' ' or gameboard[8] == ' ' or gameboard[9] == ' '):
        
        printboard(gameboard)
        print(player + '\'s turn. Go for it!')
        
        
        move = input()
        

        if move in range(1,10):
            if gameboard[move] == ' ':
                gameboard[move] = player
                count += 1
                
            else:
                print('That block has already been taken Please select a different one')
                
                continue
        else:
            print("Enter a value between 1 and 9")
            continue
            

        if count >= 5:

            if gameboard[1] == gameboard[2] == gameboard[3] != ' ':
                printboard(gameboard)
                print('Game over. ' + player + ' won')
                break

            elif gameboard[4] == gameboard[5] == gameboard[6] != ' ':
                printboard(gameboard)
                print('Game over. ' + player + ' won')
                break  
            
            elif gameboard[7] == gameboard[8] == gameboard[9] != ' ':
                printboard(gameboard)
                print('Game over. ' + player + ' won')    
                break
            

            elif gameboard[1] == gameboard[4] == gameboard[7] != ' ':
                printboard(gameboard)
                print('Game over. ' + player + ' won')
                break
            

            elif gameboard[2] == gameboard[5] == gameboard[8] != ' ':
                printboard(gameboard)
                print('Game over. ' + player + ' won')
                break
            

            elif gameboard[3] == gameboard[6] == gameboard[9] != ' ':
                printboard(gameboard)
                print('Game over. ' + player + ' won')
                break
            

            elif gameboard[1] == gameboard[5] == gameboard[9] != ' ':
                printboard(gameboard)
                print('Game over. ' + player + ' won')
                break
            

            elif gameboard[3] == gameboard[5] == gameboard[7] != ' ':
                printboard(gameboard)
                print('Game over. ' + player + ' won')
                break
            

        if (gameboard[1] != ' ' and gameboard[2] != ' ' and gameboard[3] != ' ' 
        and gameboard[4] != ' ' and gameboard[5] != ' ' and gameboard[6] != ' ' 
        and gameboard[7] != ' ' and gameboard[8] != ' ' and gameboard[9] != ' '):
            print('Game over. it\'s a tie')
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
    
    restart = input('Would you like to play again? 1 = YES 0 = NO: ')
    
    if restart == 1:
        gameboard.update({1: ' ', 2: ' ', 3: ' ', 
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '})
        action()
    else:
        print('Thank you for playing. Have an awesome day')
    
if __name__ == '__main__':
    action()

        