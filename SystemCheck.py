from chess_engine import game_state, Player
import unittest
class TestChessSystem(unittest.TestCase):

    def test_system(self):
        game = game_state()
        # make a move for the white piece by moving the pawn from B2 D2
        game.move_piece((1, 1), (3, 1), False)
        # open a move for the black queen for moving in diagonal way by moving G4 to E4/F4
        game.move_piece((6, 3), (4, 3), False)
        # clear empty space in front of white king  a gap diagonal by moving move pawn B3 to C3
        game.move_piece((1, 2), (2, 2), False)
        # now move black queen from F5 to D1 and now it's check mate
        game.move_piece((7, 4), (3, 0), False)
        # compare if the white player now have a checkmate
        self.assertTrue(game.check_for_check((0, 3), Player.PLAYER_1))
