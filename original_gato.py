# Sacado del libro: Artificial intelligence with Python.  Alberto Artasanchez and Prateek Joshi. 2da edición, 2020, Pack. Capítulo 13.
# Packages to import
from easyAI import TwoPlayersGame, AI_Player, Negamax
from easyAI.Player import Human_Player


# Class that contains all methods to play the game
class GameController(TwoPlayersGame):
    def __init__(self, players):
        # Define the players
        self.players = players
        # Define who starts the game
        self.nplayer = 1
        # Define the board
        self.board = [[0 for x in range(9)] for y in range(9)]

    # Define possible moves
    def possible_moves(self):
        # Initial [1, 2, 3, 4, 5, 6, 7, 8, 9]
        return [a + 1 for a, b in enumerate(self.board[0]) if b == 0]

    # Update the board after making a move
    def make_move(self, move):
        self.board[0][int(move) - 1] = self.nplayer

    # Does the opponent have three in line?
    def loss_condition(self):
        horizontales = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        verticales = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        diagonales = [[1, 5, 9], [3, 5, 7]]
        possible_combinations = horizontales + verticales + diagonales

        return any([all([(self.board[0][i - 1] == self.nopponent) for i in combination]) for combination in
                    possible_combinations])

    # Check if game is over
    def is_over(self):
        return (self.possible_moves() == []) or self.loss_condition()

    # Show current position
    def show(self):
        for h in range(3):
            print('\n' + '\n'.join(
                [' '.join([['.', 'O', 'X'][self.board[k + h][3 * j + i]] for k in range(3) for i in range(3)]) for j in
                 range(3)]))

    # Compute the score
    def scoring(self):
        return -100 if self.loss_condition() else 0


if __name__ == "__main__":
    # Define the algorithm
    algorithm = Negamax(7)
    # Start the game
    GameController([Human_Player(), AI_Player(algorithm)]).play()
