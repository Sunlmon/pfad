"""The same Ball objects as ball_play, now drawn in a Pygame window."""

from week07.ball_play import ROUNDS, WIDTH, feedback, starting_balls, step

CELL = 48
LEFT = 80
TOP = 130
SIZE = (640, 360)


def column_at(x):
    """Return the nearest tick, or None for a click outside the board."""
    column = round((x - LEFT) / CELL)
    if 0 <= column < WIDTH and abs(x - (LEFT + column * CELL)) <= CELL // 2:
        return column
    return None


def main():
    try:
        import pygame
    except ImportError as exc:
        raise SystemExit(
            "Pygame is optional. From the pfad root run: "
            "uv run --no-project --with pygame python -m week07.ball_pygame"
        ) from exc

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Catch the ball | SD5913 Week 7")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 26)
    red, blue = starting_balls()
    turn = 0
    guess = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    red, blue = starting_balls()
                    turn, guess = 0, None
                elif event.key == pygame.K_SPACE and turn < ROUNDS:
                    step(red)
                    step(blue)
                    turn += 1
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if turn < ROUNDS and TOP - 55 <= event.pos[1] <= TOP + 40:
                    guess = column_at(event.pos[0])

        screen.fill((21, 35, 38))
        title = font.render("Click a column to catch red. Space: step   R: reset", True, (242, 238, 221))
        screen.blit(title, (36, 30))
        for row, ball, color in ((0, red, (255, 116, 83)), (1, blue, (109, 208, 221))):
            y = TOP + row * 95
            pygame.draw.line(screen, (112, 133, 128), (LEFT, y), (LEFT + (WIDTH - 1) * CELL, y), 3)
            for index in range(WIDTH):
                x = LEFT + index * CELL
                pygame.draw.circle(screen, (112, 133, 128), (x, y), 3)
                screen.blit(font.render(str(index), True, (169, 190, 183)), (x - 6, y + 18))
            pygame.draw.circle(screen, color, (LEFT + ball.position * CELL, y), 16)

        if guess is not None:
            x = LEFT + guess * CELL
            pygame.draw.polygon(screen, (255, 217, 117), [(x, TOP - 32), (x - 10, TOP - 47), (x + 10, TOP - 47)])
        if turn == ROUNDS and guess is not None:
            status = feedback(guess, red.position)
        elif turn == ROUNDS:
            status = "Finished. Press R to try a catch."
        else:
            status = f"Move {turn}/{ROUNDS}  |  Click a column, then step with Space."
        screen.blit(font.render(status, True, (255, 217, 117)), (36, 315))
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
