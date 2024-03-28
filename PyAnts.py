import pygame
import random

print(pygame.ver)
class Ant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = random.randint(0, 360)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Ant Colony Simulator")
    clock = pygame.time.Clock()
if __name__ == "__main__":
    main()