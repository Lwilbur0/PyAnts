import pygame
import random
import math
from tkinter import *
from tkinter import messagebox
#commit to add run away feature
size = 5
speed = 1

class Ant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = random.randint(0, 360)
    def update(self, mousePos):
        dx = mousePos[0] - self.x
        dy = mousePos[1] - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if random.random() < 0.05:
            self.direction = random.randint(0, 360)
        # if distance away from mouse is within 50, then reverse the angle to run away from the mouse
        if distance < 50:
            angle = math.atan2(dy, dx)
            angle += math.pi
            self.x -= speed * math.cos(angle) * (50 - distance) / 50
            self.y -= speed * math.sin(angle) * (50 - distance) / 50
        else:
            self.x += speed * math.cos(math.radians(self.direction))
            self.y += speed * math.sin(math.radians(self.direction))

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (int(self.x), int(self.y)), size)


def helloCallBack():
   msg=messagebox.showinfo( "Hello Python", "Hello World")
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Ant Colony Simulator")
    clock = pygame.time.Clock()

    ants = []
    for x in range(50):
        ant = Ant(random.randint(0, 600), random.randint(0, 800))
        ants.append(ant)

    B = Button(screen, text ="Hello", command = helloCallBack)
    B.place(x=50,y=50)
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        for ant in ants:
            ant.update(mouse_pos)
            ant.draw(screen)

        # makes changes visible to screen
        pygame.display.flip()
        # framerate
        clock.tick(60)
    
    pygame.quit()
if __name__ == "__main__":
    main()