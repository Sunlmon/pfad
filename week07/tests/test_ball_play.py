"""Checks for the optional terminal ball progression."""

import contextlib
import io
import subprocess
import sys
import unittest

from week07.ball import Ball
from week07.ball_play import WIDTH, lane, play, step
from week07.ball_pygame import column_at


class BallPlayTests(unittest.TestCase):
    def test_lane_and_independent_movement(self):
        red = Ball(position=2, velocity=1)
        blue = Ball(position=7, velocity=-1)
        self.assertEqual(lane(red, "R"), "..R........")
        step(red)
        self.assertEqual((red.position, blue.position), (3, 7))

    def test_wall_reverses_direction(self):
        red = Ball(position=9, velocity=1)
        step(red)
        self.assertEqual((red.position, red.velocity), (10, -1))
        step(red)
        self.assertEqual(red.position, 9)
        blue = Ball(position=1, velocity=-1)
        step(blue)
        self.assertEqual((blue.position, blue.velocity), (0, 1))

    def test_guesses_give_feedback(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            play(8)
        self.assertIn("Caught it at 8!", out.getvalue())
        self.assertIn("10  ........R..", out.getvalue())
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            play(4)
        self.assertIn("Missed: red finished at 8, not 4.", out.getvalue())

    def test_invalid_guess_is_explained(self):
        result = subprocess.run(
            [sys.executable, "-m", "week07.ball_play", "--guess", str(WIDTH)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--guess must be between 0 and 10", result.stderr)

    def test_terminal_input_and_retry(self):
        result = subprocess.run(
            [sys.executable, "-m", "week07.ball_play"],
            input="oops\n11\n8\n",
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("Enter a whole number from 0 to 10.", result.stdout)
        self.assertIn("Choose a column from 0 to 10.", result.stdout)
        self.assertIn("Caught it at 8!", result.stdout)

    def test_pygame_clicks_map_to_the_same_columns(self):
        self.assertEqual(column_at(80 + 8 * 48), 8)
        self.assertIsNone(column_at(10))
        self.assertIsNone(column_at(700))


if __name__ == "__main__":
    unittest.main()
