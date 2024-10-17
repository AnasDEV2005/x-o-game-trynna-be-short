def show_table(game):
    s=''
    for i in range(len(game)):
        s+=str(game[i])+'  '
        if len(s)==9: 
            print(s)
            s=''

def check_winner(game):
    combins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    x=0
    o=0
    X=[]
    O=[]
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
        x=0
        o=0

def play(game):
    print('new game')
    win=False

    while win==False:
        show_table(game)
        X = int(input('Where will you put X?_ '))
        game[X]='X'
        show_table(game)

        if check_winner(game)=='Xwin': 
            print('X has won'),
            win=True
            play([0,1,2,3,4,5,6,7,8])

        O = int(input('Where will you put O?_ '))
        game[O]='O'
        show_table(game)

        if check_winner(game)=='Owin': 
            print('O has won')
            win=True
            play([0,1,2,3,4,5,6,7,8])
        print('next round')            
    play([0,1,2,3,4,5,6,7,8])
   
play([0,1,2,3,4,5,6,7,8])

# meth
# tried to make something short and easy to read with less conditionals
