# prints board in lines of 3
def show_table(game):
    print(game[0],' ',game[1],' ',game[2])
    print(game[3],' ',game[4],' ',game[5])
    print(game[6],' ',game[7],' ',game[8])
# iterate on all spots taken by each player, see if a winning combination exists there
def check_winner(game):
    combins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    x, o, X, O = 0, 0, [], []
    for i in range(len(game)):
        if game[i]=='X':
            X.append(i)
        if game[i]=='O':
            O.append(i)
    for i in range(8):
        for j in combins[i]:
            if j in X: x+=1
            if j in O: o+=1
        if x==3: return('Xwin')
        if o==3: return('Owin')
        x, o = 0, 0

def play(game):
    print('new game')
    tie=False
# useless loop condition but eh
    while tie==False:
        show_table(game)
        X = int(input('Where will you put X?_ '))
        game[X]='X'
        show_table(game)
# if X wins with this move, restart game
        if check_winner(game)=='Xwin': 
            print('X has won'),
            win=True
            play([0,1,2,3,4,5,6,7,8])
# O turn otherwise
        O = int(input('Where will you put O?_ '))
        game[O]='O'
        show_table(game)
# if O wins, restart, otherwise move to next round
        if check_winner(game)=='Owin': 
            print('O has won')
            win=True
            play([0,1,2,3,4,5,6,7,8])
        for i in game:
            tie=True
            if isinstance(i, int): tie=False
        print('next round')
    
    print('its a tie')          
    play([0,1,2,3,4,5,6,7,8])
    
play([0,1,2,3,4,5,6,7,8])

