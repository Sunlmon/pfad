# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Two independent objects for the optional Week 7 tutorial."""


class Ball:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def update(self, seconds):
        self.position = self.position + self.velocity * seconds


def main():
    red = Ball(position=2, velocity=3)
    blue = Ball(position=10, velocity=-1)

    print(f"Before: red={red.position}, blue={blue.position}")
    red.update(1)
    print(f"After red.update(1): red={red.position}, blue={blue.position}")
    blue.update(1)
    print(f"After blue.update(1): red={red.position}, blue={blue.position}")


if __name__ == "__main__":
    main()
