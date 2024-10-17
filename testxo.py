def show_table(game):
    print('\n'.join([' '.join(map(str, game[i:i+3])) for i in range(0, 9, 3)]))

def check_winner(game, player):
    channels = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    return any(all(game[i] == player for i in ch) for ch in channels)

def play():
    game = list(range(9))
    for turn in range(9):
        show_table(game)
        player = 'X' if turn % 2 == 0 else 'O'
        move = int(input(f"{player}'s move (0-8): "))
        if game[move] in 'XO': print("Invalid move, try again!"); continue
        game[move] = player
        if check_winner(game, player): show_table(game); print(f"{player} wins!"); return
    show_table(game); print("It's a tie!")

play()
