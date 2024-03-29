import pygame
import random
import math

size = 5
speed = 1

class Ant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = random.randint(0, 360)
    def update(self):
        self.x += speed * math.cos(math.radians(self.direction))
        self.y += speed * math.sin(math.radians(self.direction))
        if random.random() < 0.05:
            self.direction = random.randint(0, 360)
    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (int(self.x), int(self.y)), size)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Ant Colony Simulator")
    clock = pygame.time.Clock()

    ants = []
    for x in range(50):
        ant = Ant(random.randint(0, 600), random.randint(0, 800))
        ants.append(ant)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        for ant in ants:
            ant.update()
            ant.draw(screen)

        # makes changes visible to screen
        pygame.display.flip()
        # framerate
        clock.tick(60)

    pygame.quit()
if __name__ == "__main__":
    main()