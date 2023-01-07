import unittest
import connect
import numpy as np

class TestBoardMethods(unittest.TestCase):

    def test_horizontal_winner(self):
        b = connect.Connect4Board()
        b.board[0,0] = 1
        b.board[0,1] = 1
        b.board[0,2] = 1
        b.board[0,3] = 1
        self.assertEqual(b.check_win(), 1)

    def test_vertical_winner(self):
        b = connect.Connect4Board()
        b.board[0,0] = 2
        b.board[1,0] = 2
        b.board[2,0] = 2
        b.board[3,0] = 2
        self.assertEqual(b.check_win(), 2)

    def test_diag_1(self):
        b = connect.Connect4Board()
        b.board[0,0] = 2
        b.board[1,1] = 2
        b.board[2,2] = 2
        b.board[3,3] = 2
        self.assertEqual(b.check_win(), 2)

    def test_diag_2(self):
        b = connect.Connect4Board()
        b.board[3,1] = 2
        b.board[2,2] = 2
        b.board[1,3] = 2
        b.board[0,4] = 2
        self.assertEqual(b.check_win(), 2)

    def test_random_game(self):
        
        b = connect.Connect4Board()
        b.board = np.array(
            [[0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 1., 0., 0., 0.],
            [0., 0., 2., 1., 1., 0., 0.],
            [0., 1., 1., 2., 2., 1., 2.],
            [2., 1., 1., 1., 2., 2., 2.]])
        self.assertEqual(b.check_win(), 0)



if __name__ == 'main':
    unittest.main()