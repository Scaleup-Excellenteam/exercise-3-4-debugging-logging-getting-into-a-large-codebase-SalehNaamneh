import unittest
import Piece
from chess_engine import game_state, Player

class TestKnightMoves(unittest.TestCase):

    def test_knight_moves(self):
        game = game_state()
        # Create and place a knight at (4, 3)
        self.knight = Piece.Knight('knight', 4, 3, Player.PLAYER_1)
        game.board[4][3] = self.knight

        # Create and place a pawn at (2, 4)
        pawn = Piece.Pawn('pawn1', 2, 4, Player.PLAYER_1)
        game.board[2][4] = pawn

        # Get valid moves for the knight
        valid_moves = self.knight.get_valid_piece_moves(game)

        # Expected moves for a knight at position (4, 3) with pawn at (2, 4)
        expected_moves = [
            (2, 2), (3, 1), (3, 5), (5, 1),
            (5, 5), (6, 4), (6, 2)
        ]

        # Convert to set for unordered comparison
        self.assertEqual(set(valid_moves), set(expected_moves))

    def test_knight_moves2(self):
        self.game_state = game_state()

        # Create and place a knight at (5, 5)
        knight = Piece.Knight('knight', 5, 5, Player.PLAYER_1)
        self.game_state.board[5][5] = knight

        # Create and place pawns
        pawn1 = Piece.Pawn('pawn1', 6, 3, Player.PLAYER_2)
        pawn2 = Piece.Pawn('pawn2', 7, 4, Player.PLAYER_2)

        # moving the pawn in this way to reduce the amount of code and actually move the pawn not playing the game
        self.game_state.board[6][3] = pawn1
        self.game_state.board[7][4] = pawn2

        valid_moves = knight.get_valid_piece_moves(self.game_state)

        expected_moves = [
            (3, 4), (3, 6), (4, 3), (4, 7), (6, 3), (6, 7), (7, 6), (7, 4)
        ]

        # Convert to set for unordered comparison
        self.assertEqual(set(valid_moves), set(expected_moves))

    def test_knight_moves3(self):
        self.game_state = game_state()

        knight = Piece.Knight('knight', 7, 1, Player.PLAYER_2)
        self.game_state.board[7][1] = knight

        # Get valid moves for the knight
        valid_moves = knight.get_valid_piece_moves(self.game_state)

        expected_moves = [
            (5, 0), (5, 2)
        ]

        # Convert to set for unordered comparison
        self.assertEqual(set(valid_moves), set(expected_moves))
    def test_knight_peaceful_moves(self):
        game = game_state()

        # Place the knight on the board
        knight = Piece.Knight('knight', 2, 2, Player.PLAYER_1)
        game.board[2][2] = knight

        # Create and place pawns
        pawn1 = Piece.Pawn('pawn', 1, 0, Player.PLAYER_1)
        pawn2 = Piece.Pawn('pawn1', 1, 4, Player.PLAYER_1)
        pawn3 = Piece.Pawn('pawn2', 3, 0, Player.PLAYER_2)
        pawn4 = Piece.Pawn('pawn3', 4, 1, Player.PLAYER_2)
        pawn5 = Piece.Pawn('pawn4', 4, 3, Player.PLAYER_2)
        pawn6 = Piece.Pawn('pawn5', 3, 4, Player.PLAYER_2)
        king = Piece.King('king', 3, 0, Player.PLAYER_1)

        # Set original positions to None
        game.board[1][0] = None
        game.board[1][4] = None
        game.board[3][0] = None
        game.board[4][1] = None
        game.board[4][3] = None
        game.board[3][4] = None
        game.board[0][1] = None

        # Place pawns on the board
        game.board[1][0] = pawn1
        game.board[1][4] = pawn2
        game.board[3][0] = pawn3
        game.board[4][1] = pawn4
        game.board[4][3] = pawn5
        game.board[3][4] = pawn6

        # Move all the pieces to their new positions
        game.move_piece((1, 0), (0, 1), is_ai=False)
        game.move_piece((1, 4), (0, 5), is_ai=False)
        game.move_piece((3, 0), (2, 1), is_ai=False)
        game.move_piece((4, 1), (5, 2), is_ai=False)
        game.move_piece((4, 3), (5, 4), is_ai=False)
        game.move_piece((3, 4), (2, 5), is_ai=False)
        game.move_piece((2, 2), (0, 1), is_ai=False)  # Move the knight last

        # Check the valid moves of the knight
        valid_moves = knight.get_valid_peaceful_moves(game)
        expected_moves = [(0, 1)]
        self.assertEqual(expected_moves, valid_moves)
    def test_knight_peaceful_moves2(self):
        game = game_state()

        # Place the knight on the board
        knight = Piece.Knight('knight', 4, 3, Player.PLAYER_1)
        game.board[4][3] = knight
        game.board[0][1] = None
        peacefulMoves = knight.get_valid_peaceful_moves(game)
        expected_moves = [(2, 2), (2, 4), (3, 1), (3, 5), (5, 1), (5, 5)]
        self.assertEqual(set(expected_moves), set(peacefulMoves))

    def test_knight_peaceful_moves3(self):
        game = game_state()

        # Place the knight on the board
        knight = Piece.Knight('knight', 5, 5, Player.PLAYER_1)
        game.board[5][5] = knight

        # Create and place pawns to block some of the knight's moves
        pawn1 = Piece.Pawn('pawn1', 4, 3, Player.PLAYER_1)
        pawn2 = Piece.Pawn('pawn2', 6, 3, Player.PLAYER_1)
        pawn3 = Piece.Pawn('pawn3', 7, 6, Player.PLAYER_1)
        game.board[4][3] = pawn1
        game.board[6][3] = pawn2
        game.board[7][6] = pawn3

        # Clear the positions where the knight can move
        game.board[3][4] = None
        game.board[3][6] = None
        game.board[4][7] = None
        game.board[6][7] = None
        game.board[7][4] = None

        # Get peaceful moves for the knight
        peacefulMoves = knight.get_valid_peaceful_moves(game)

        # Expected moves for the knight at position (5, 5) with pawns blocking some moves
        expected_moves = [(3, 4), (3, 6), (4, 7), (6, 7), (7, 4)]

        self.assertEqual(set(expected_moves), set(peacefulMoves))






if __name__ == '__main__':
    unittest.main()

