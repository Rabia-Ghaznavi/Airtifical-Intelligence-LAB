class NQueens:
    def _init_(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]

    def is_attack(self, row, col):
        for i in range(self.n):
            if self.board[row][i] == 1 or self.board[i][col] == 1:
                return True
        for i in range(self.n):
            for j in range(self.n):
                if i + j == row + col or i - j == row - col:
                    if self.board[i][j] == 1:
                        return True
        return False

    def n_queens(self, n):
        if n == 0:
            return True
        for i in range(self.n):
            for j in range(self.n):
                if not self.is_attack(i, j) and self.board[i][j] != 1:
                    self.board[i][j] = 1
                    if self.n_queens(n - 1):
                        return True
                    self.board[i][j] = 0
        return False

    def solve(self):
        if not self.n_queens(self.n):
            print("No solution exists.")
            return False
        print("Solution:")
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=' ')
            print()
        return True


n = int(input("Enter the value of n: "))
queens = NQueens(n)
queens.solve()
                