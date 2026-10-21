"""A tiny terminal ball game built on the Week 7 Ball class."""

import argparse

from week07.ball import Ball

WIDTH = 11
ROUNDS = 10


def step(ball):
    """Move one space, then turn around at either end of the lane."""
    ball.update(1)
    if ball.position == 0 or ball.position == WIDTH - 1:
        ball.velocity = -ball.velocity


def lane(ball, symbol):
    cells = ["."] * WIDTH
    cells[ball.position] = symbol
    return "".join(cells)


def starting_balls():
    return Ball(position=2, velocity=1), Ball(position=7, velocity=-1)


def feedback(guess, position):
    if guess == position:
        return f"Caught it at {position}! Try another guess or change the speed."
    return f"Missed: red finished at {position}, not {guess}. Try again."


def play(guess=None):
    red, blue = starting_balls()

    print("Guess where red will be after 10 moves (0 to 10).")
    for turn in range(ROUNDS + 1):
        print(f"{turn:2}  {lane(red, 'R')}  {lane(blue, 'B')}")
        if turn < ROUNDS:
            step(red)
            step(blue)

    if guess is not None:
        print(feedback(guess, red.position))


def ask_guess():
    while True:
        try:
            answer = input("Catch red at column 0-10? (Enter to watch): ").strip()
        except EOFError:
            return None
        if not answer:
            return None
        try:
            guess = int(answer)
        except ValueError:
            print("Enter a whole number from 0 to 10.")
            continue
        if 0 <= guess < WIDTH:
            return guess
        print("Choose a column from 0 to 10.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--guess", type=int, help="Catch red at a column from 0 to 10")
    parser.add_argument("--watch", action="store_true", help="Show the trace without a guess")
    args = parser.parse_args()
    if args.watch and args.guess is not None:
        parser.error("choose --watch or --guess, not both")
    if args.guess is not None and not 0 <= args.guess < WIDTH:
        parser.error(f"--guess must be between 0 and {WIDTH - 1}")
    play(ask_guess() if args.guess is None and not args.watch else args.guess)


if __name__ == "__main__":
    main()
