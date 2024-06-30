import unittest

from chess_engine import game_state, Player
import ai_engine
class Test_AI_Evaluate(unittest.TestCase):
    def test_board_evaluate(self):
        game = game_state()
        ai = ai_engine.chess_ai()
        # trying to evaluate the board at the beginning  of the match
        # we expect evaluation equals to zero because the board is still clean
        evaluation_score = ai.evaluate_board(game, Player.PLAYER_1)
        self.assertEqual(evaluation_score, 0)
        # after deleting some of the white pieces and the AI is playing white
        # the AI should be in negative valuation
        # to be precises -80 because what I deleted here is rock and  a bishop
        game.board[0][0] = None
        game.board[0][5] = None
        evaluation_score = ai.evaluate_board(game, Player.PLAYER_1)
        self.assertLess(evaluation_score, 0)
        # deleting some of the black pieces so to check if the evaluation is done is it expected

        game.board[7][4] = None
        evaluation_score = ai.evaluate_board(game, Player.PLAYER_1)
        self.assertGreater(evaluation_score, 0)

