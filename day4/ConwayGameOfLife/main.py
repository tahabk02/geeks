import time
from gameboard import GameBoard

board = GameBoard(5, 5)
board.set_alive(1, 2)
board.set_alive(2, 2)
board.set_alive(3, 2)

for _ in range(10):
    board.display()
    board.next_generation()
    time.sleep(1)
