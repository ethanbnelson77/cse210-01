
global game
game = True
spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]



def board():
    print(f'\n{spaces[0]}|{spaces[1]}|{spaces[2]}\n-+-+-\n{spaces[3]}|{spaces[4]}|{spaces[5]}\n-+-+-\n{spaces[6]}|{spaces[7]}|{spaces[8]}\n')



def game_check(winner):
    global game
    if spaces[0] == spaces[1] == spaces[2] or spaces[3] == spaces[4] == spaces[5] or spaces[6] == spaces[7] == spaces[8] or spaces[0] == spaces[3] == spaces[6] or spaces[1] == spaces[4] == spaces[7] or spaces[2] == spaces[5] == spaces[8] or spaces[0] == spaces[4] == spaces[8] or spaces[2] == spaces[4] == spaces[6]:
        game = False
        print(f'Good game! {winner} wins.')
    else:
        pass
    


def main():

    global game
    board()

    while game == True:
        
        replace_x = int(input("x's turn to choose a square (1-9): "))
        spaces[replace_x-1] = 'x'

        board()
        winner = 'x'
        game_check(winner)

        if game == True:

            replace_o = int(input("o's turn to choose a square (1-9): "))
            spaces[replace_o-1] = 'o'

            board()
            winner = 'o'
            game_check(winner)
        else:
            pass

    
main()