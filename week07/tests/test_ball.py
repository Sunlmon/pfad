"""Small checks for the optional two-object trace."""

import unittest

from week07.ball import Ball


class BallTests(unittest.TestCase):
    def test_only_the_updated_ball_moves(self):
        red = Ball(position=2, velocity=3)
        blue = Ball(position=10, velocity=-1)
        red.update(1)
        self.assertEqual((red.position, blue.position), (5, 10))
        blue.update(1)
        self.assertEqual((red.position, blue.position), (5, 9))

    def test_zero_seconds_does_not_move(self):
        ball = Ball(position=2, velocity=3)
        ball.update(0)
        self.assertEqual(ball.position, 2)


if __name__ == "__main__":
    unittest.main()
