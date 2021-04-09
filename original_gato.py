# Sacado del libro: Artificial intelligence with Python.  Alberto Artasanchez and Prateek Joshi. 2da edición, 2020, Pack. Capítulo 13.
# Packages to import
from easyAI import TwoPlayersGame, AI_Player, Negamax
from easyAI.Player import Human_Player
import random


# Class that contains all methods to play the game
class GameController(TwoPlayersGame):
    def __init__(self, players):
        # Define the players
        self.players = players
        # Define who starts the game
        self.nplayer = 1
        # Define the board
        self.board = [[0 for x in range(9)] for y in range(9)]

        self.actualBoard = -1

        self.closedBoards = []

        self.IAWonBoards = []

        self.PlayerWonBoards = []

    # Define possible moves
    def possible_moves(self):
        # Initial [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # actualBoard is -1 when the player or IA can choose any board, but for this game that would be random
        if self.actualBoard != -1:
            moves = [a + 1 for a, b in enumerate(self.board[self.actualBoard]) if b == 0]
            if not moves:
                self.closedBoards.append(self.actualBoard)
                if len(self.closedBoards) < 9:
                    self.actualBoard = random.randint(0, 8)
                    while not self.closedBoards.__contains__(self.actualBoard):
                        self.actualBoard = random.randint(0, 8)
                    return [a + 1 for a, b in enumerate(self.board[self.actualBoard]) if b == 0]
                else:
                    return []
            else:
                return moves
        else:
            self.actualBoard = random.randint(0, 8)
            while self.closedBoards.__contains__(self.actualBoard):
                self.actualBoard = random.randint(0, 8)
            return [a + 1 for a, b in enumerate(self.board[self.actualBoard]) if b == 0]
        print('Playing on board ' + str(self.actualBoard))

    # Update the board after making a move
    def make_move(self, move):
        self.board[self.actualBoard][int(move) - 1] = self.nplayer
        self.actualBoard = int(move) - 1

    # Does the opponent have three in line?
    def loss_condition(self):
        horizontales = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        verticales = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        diagonales = [[1, 5, 9], [3, 5, 7]]
        possible_combinations = horizontales + verticales + diagonales

        return any(
            [all([(self.board[self.actualBoard][i - 1] == self.nopponent) for i in combination]) for combination in
             possible_combinations])

    def checkWinIA(self):
        horizontales = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        verticales = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        diagonales = [[1, 5, 9], [3, 5, 7]]
        possible_combinations = horizontales + verticales + diagonales

        for i in range(len(possible_combinations)):
            won = True
            for j in range(len(possible_combinations[i])):
                if not self.IAWonBoards.__contains__(possible_combinations[i][j]):
                    won = False
                    break
            if won == 1:
                return True

        return False

    def checkWinPlayer(self):
        horizontales = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        verticales = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        diagonales = [[1, 5, 9], [3, 5, 7]]
        possible_combinations = horizontales + verticales + diagonales

        for i in range(len(possible_combinations)):
            won = True
            for j in range(len(possible_combinations[i])):
                if not self.PlayerWonBoards.__contains__(possible_combinations[i][j]):
                    won = False
                    break
            if won == 1:
                return True

        return False

    # Check if game is over
    def is_over(self):
        return (len(self.closedBoards) == 9) or self.checkWinIA() or self.checkWinPlayer()

    # Show current position
    def show(self):
        for h in range(3):
            print('\n' + '\n'.join(
                [' '.join([['.', 'O', 'X'][self.board[k + h * 3][3 * j + i]] for k in range(3) for i in range(3)]) for j
                 in
                 range(3)]))

    # Compute the score
    def scoring(self):

        if self.checkWinPlayer():
            return 1
        elif self.checkWinIA():
            return -1
        else:
            return -100


if __name__ == "__main__":
    # Define the algorithm
    algorithm = Negamax(7)
    # Start the game
    GameController([Human_Player(), AI_Player(algorithm)]).play()
