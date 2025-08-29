from cell import Cell

class GameBoard:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(False) for _ in range(cols)] for _ in range(rows)]

    def set_alive(self, row, col):
        self.grid[row][col].alive = True

    def count_alive_neighbors(self, row, col):
        directions = [(-1,-1), (-1,0), (-1,1),
                      (0,-1),         (0,1),
                      (1,-1),  (1,0), (1,1)]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                if self.grid[r][c].alive:
                    count += 1
        return count

    def next_generation(self):
        new_grid = [[Cell(False) for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                alive_neighbors = self.count_alive_neighbors(r, c)
                if self.grid[r][c].alive:
                    if alive_neighbors in [2, 3]:
                        new_grid[r][c].alive = True
                else:
                    if alive_neighbors == 3:
                        new_grid[r][c].alive = True
        self.grid = new_grid

    def display(self):
        for row in self.grid:
            print("".join(str(cell) for cell in row))
        print("\n" + "-"*self.cols)
