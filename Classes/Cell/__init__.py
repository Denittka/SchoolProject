class Cell:
    """
    Класс клетки -- живого существа, живущего по собственному генному коду.
    """
    def __init__(self, board, x, y):
        """
        Принимает на вход изначальную доску, чтобы взаимодейсвтует с миром.
        :param board: изначальная доска
        """
        self.x = x
        self.y = y
        self.board = board
        self.code = [1, 1, 1, 1, 2, 2, 2, 2, 1]  # TODO написать
        self.step = 0

    def move(self, direction):
        if direction == "UP":
            if self.y > 0:
                if self.board[self.y - 1][self.x] is None:
                    self.board[self.y - 1][self.x] = self
                    self.board[self.y][self.x] = None
                    self.y -= 1
        if direction == "RIGHT":
            if self.x < len(self.board[0]) - 1:
                if self.board[self.y][self.x + 1] is None:
                    self.board[self.y][self.x + 1] = self
                    self.board[self.y][self.x] = None
                    self.x += 1
        if direction == "DOWN":
            if self.y < len(self.board) - 1:
                if self.board[self.y + 1][self.x] is None:
                    self.board[self.y + 1][self.x] = self
                    self.board[self.y][self.x] = None
                    self.y += 1
        if direction == "LEFT":
            if self.x > 0:
                if self.board[self.y][self.x - 1] is None:
                    self.board[self.y][self.x - 1] = self
                    self.board[self.y][self.x] = None
                    self.x -= 1

    def do(self, command):
        if command == "MOVE UP":
            self.move("UP")
        if command == "MOVE LEFT":
            self.move("LEFT")
        if command == "MOVE DOWN":
            self.move("DOWN")
        if command == "MOVE RIGHT":
            self.move("RIGHT")

    def get(self, num):
        if num == 1:
            return "MOVE UP"
        if num == 2:
            return "MOVE RIGHT"
        if num == 3:
            return "MOVE DOWN"
        if num == 4:
            return "MOVE LEFT"

    def update(self):
        self.do(self.get(self.code[self.step]))
        self.step = (self.step + 1) % len(self.code)
