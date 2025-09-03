def display_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def player_input(player, board):
    while True:
        try:
            pos = int(input(f"Player {player} turn. Choose position (1-9): ")) - 1
            if pos < 0 or pos > 8:
                print("Invalid position! Choose 1-9.")
            elif board[pos] != " ":
                print("Position already taken! Try again.")
            else:
                board[pos] = player
                break
        except ValueError:
            print("Please enter a number from 1 to 9.")

def check_win(board):
    win_combinations = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    if " " not in board:
        return "Tie"
    return None

def play():
    board = [" "] * 9
    current_player = "X"
    winner = None
    display_board(board)
    
    while winner is None:
        player_input(current_player, board)
        display_board(board)
        winner = check_win(board)
        if winner is None:
            current_player = "O" if current_player == "X" else "X"
    
    if winner == "Tie":
        print("It's a tie!")
    else:
        print(f"Player {winner} wins!")

if __name__ == "__main__":
    play()
