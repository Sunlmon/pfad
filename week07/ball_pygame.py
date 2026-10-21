# /// script
# requires-python = ">=3.10,<3.14"
# dependencies = ["pygame==2.6.1", "watchfiles==1.3.0"]
# ///
"""Two windows, one simulation: Pygame here, ASCII in this terminal."""

if __package__:
    from .ball_live import Simulation
    from .ball_play import AsciiView
else:
    from ball_live import Simulation
    from ball_play import AsciiView

SIZE = (960, 680)
COLORS = ((255, 116, 83), (109, 208, 221))


def main():
    import pygame

    pygame.init()
    screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
    pygame.display.set_caption("Ball physics | SD5913 Week 7")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 26)
    heading = pygame.font.Font(None, 38)
    simulation = Simulation()
    ascii_view = AsciiView()
    paused = False
    running = True

    try:
        while running:
            seconds = clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        simulation.reload()
                    elif event.key == pygame.K_SPACE:
                        paused = not paused

            simulation.advance(0 if paused else seconds)
            width, height = screen.get_size()
            scale = max(0.1, min((width - 56) / simulation.model.WIDTH,
                                 (height - 150) / simulation.model.HEIGHT))
            arena = pygame.Rect(0, 0, round(simulation.model.WIDTH * scale),
                                round(simulation.model.HEIGHT * scale))
            arena.center = (width // 2, (height - 80) // 2 + 35)

            screen.fill((21, 35, 38))
            pygame.draw.rect(screen, (28, 46, 50), arena)
            pygame.draw.rect(screen, (112, 133, 128), arena, 2)
            screen.blit(heading.render("One model. Two views.", True, (242, 238, 221)), (28, 20))
            for index, ball in enumerate(simulation.balls):
                center = (round(arena.left + ball.x * scale), round(arena.top + ball.y * scale))
                radius = max(2, round(ball.radius * scale))
                pygame.draw.circle(screen, COLORS[index % len(COLORS)], center, radius)
                pygame.draw.circle(screen, (242, 238, 221),
                                   (center[0] - radius // 3, center[1] - radius // 3), max(1, radius // 5))

            controls = "Space: pause / resume   R: reset   Save ball.py: reload both views"
            screen.blit(font.render(controls, True, (242, 238, 221)), (28, height - 69))
            state = "PAUSED" if paused else "MOVING"
            status = f"{state} / frame {simulation.ticks} / revision {simulation.revision}"
            screen.blit(font.render(status, True, (255, 217, 117)), (28, height - 42))
            if "Error:" in simulation.status:
                pygame.display.set_caption("Ball physics | edit error: see terminal")
            else:
                pygame.display.set_caption("Ball physics | SD5913 Week 7")
            ascii_view.draw(simulation)
            pygame.display.flip()
    except KeyboardInterrupt:
        pass
    finally:
        simulation.close()
        ascii_view.close()
        pygame.quit()


if __name__ == "__main__":
    main()
