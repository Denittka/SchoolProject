from random import randint


class Cell:
    """
    Класс клетки -- живого существа, живущего по собственному генному коду.
    """

    def __init__(self, board, x, y, count):
        """
        Принимает на вход изначальную доску, чтобы взаимодейсвтует с миром.
        :param board: изначальная доска
        """
        self.dead_inside = False
        self.x = x
        self.y = y
        self.board = board
        self.code = [1, 1, 5]
        self.step = 0
        self.count = count
        self.energy = 50

    def move(self, direction):
        if direction == "UP":
            if self.y > 0:
                if self.board.board[self.y - 1][self.x] is None:
                    self.board.board[self.y - 1][self.x] = self
                    self.board.board[self.y][self.x] = None
                    self.y -= 1
        if direction == "RIGHT":
            if self.x < len(self.board.board[0]) - 1:
                if self.board.board[self.y][self.x + 1] is None:
                    self.board.board[self.y][self.x + 1] = self
                    self.board.board[self.y][self.x] = None
                    self.x += 1
        if direction == "DOWN":
            if self.y < len(self.board.board) - 1:
                if self.board.board[self.y + 1][self.x] is None:
                    self.board.board[self.y + 1][self.x] = self
                    self.board.board[self.y][self.x] = None
                    self.y += 1
        if direction == "LEFT":
            if self.x > 0:
                if self.board.board[self.y][self.x - 1] is None:
                    self.board.board[self.y][self.x - 1] = self
                    self.board.board[self.y][self.x] = None
                    self.x -= 1
        if direction == "TLEFT":
            for i in range(len(self.code)):
                if self.code[i] in {1, 2, 3, 4}:
                    if self.code[i] != 1:
                        self.code[i] -= 1
                    else:
                        self.code[i] = 4
        if direction == "TRIGHT":
            for i in range(len(self.code)):
                if self.code[i] in {1, 2, 3, 4}:
                    if self.code[i] != 4:
                        self.code[i] += 1
                    else:
                        self.code[i] = 1

    def do(self, command):
        if command == "MOVE UP":
            self.move("UP")
        if command == "MOVE LEFT":
            self.move("LEFT")
        if command == "MOVE DOWN":
            self.move("DOWN")
        if command == "MOVE RIGHT":
            self.move("RIGHT")
        if command == "TURN TO LEFT":
            self.move("TLEFT")
        if command == "TURN TO RIGHT":
            self.move("TRIGHT")
        if command == "PHOTOSYNTHESIS":
            self.photosynthesis()

    def get(self, num):
        if num == 1:
            return "MOVE UP"
        if num == 2:
            return "MOVE RIGHT"
        if num == 3:
            return "MOVE DOWN"
        if num == 4:
            return "MOVE LEFT"
        if num == 5:
            return "TURN TO LEFT"
        if num == 6:
            return "TURN TO RIGHT"
        if num == 7:
            return "PHOTOSYNTHESIS"

    def mutize(self, cell_coords):
        mutized = False
        for i in range(64):
            mut
            self.board.board[cell_coords[1]][cell_coords[0]]

    def double(self):
        if self.y > 0:
            if self.board.board[self.y - 1][self.x] is None:
                self.board.board[self.y - 1][self.x] = self
                self.bpard.board[self.y - 1][self.x]
                self.board.board[self.y - 1][self.x].energy = 50
                self.board.board[self.y][self.x],energy = 50
                doubled = True
            else:
                doubled = False
        else:
            doubled = False
        if not doubled:
            if self.x < len(self.board.board[0]) - 1:
                if self.board.board[self.y][self.x + 1] is None:
                    self.board.board[self.y][self.x + 1] = self
                    self.board.board[self.y][self.x + 1].energy = 50
                    self.board.board[self.y][self.x].energy = 50
                    doubled = True
                else:
                    doubled = False
            else:
                doubled = False
            if not doubled:
                if self.y < len(self.board.board) - 1:
                    if self.board.board[self.y + 1][self.x] is None:
                        self.board.board[self.y + 1][self.x] = self
                        self.board.board[self.y + 1][self.x].energy = 50
                        self.board.board[self.y][self.x].energy = 50
                        doubled = True
                    else:
                        doubled = False
                else:
                    doubled = False
                if not doubled:
                    if self.x > 0:
                        if self.board.board[self.y][self.x - 1] is None:
                            self.board.board[self.y][self.x - 1] = self
                            self.board.board[self.y][self.x - 1].energy = 50
                            self.board.board[self.y][self.x].energy = 50
                            doubled = True
                        else:
                            doubled = False
                    else:
                        doubled = False
                    if not dobled:
                        self.energy = 105

    def photosynthesis(self):
        self.energy += 15

    def DIE(self):
        self.dead_inside = True

    def update(self):
        if self.energy == 100:
            self.double()
        if not self.dead_inside:
            self.energy -= 5
            self.do(self.get(self.code[self.step]))
            self.step = (self.step + 1) % len(self.code)
            if self.energy == 0:
                self.DIE()
