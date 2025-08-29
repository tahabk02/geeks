class Cell:
    def __init__(self, alive=False):
        self.alive = alive

    def __repr__(self):
        return "█" if self.alive else " "
