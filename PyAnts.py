import pygame
import random
import math
# from tkinter import *
# from tkinter import messagebox
#number counter to change how many ants are on screen
#get rid of fill to create snake simulator
#hover hand when hovering over text toggles
size = 5
speed = 1

class Ant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = random.randint(0, 360)
        self.run_away = False
    def update(self, mousePos):
        # distance of ant from mouse
        dx = mousePos[0] - self.x
        dy = mousePos[1] - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if random.random() < 0.05:
            self.direction = random.randint(0, 360)
        # if distance away from mouse is within 50, then reverse the angle to run away from the mouse
        if distance < 100:
            angle = math.atan2(dy, dx)
            angle += math.pi
            # either directs ants to mouse or opposite of mouse
            if self.run_away:
                self.x += speed * 3 * math.cos(angle) * (50 - distance) / 50
                self.y += speed * 3 * math.sin(angle) * (50 - distance) / 50
            else:
                self.x -= speed * 2 * math.cos(angle) * (50 - distance) / 50
                self.y -= speed * 2 * math.sin(angle) * (50 - distance) / 50
        else:
            # adds x or y value based on the horizontal and vertical speed of a directional vector
            self.x += speed * math.cos(math.radians(self.direction))
            self.y += speed * math.sin(math.radians(self.direction))

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (int(self.x), int(self.y)), size)
    
    def toggle_run_away(self):
        self.run_away = not self.run_away



pygame.font.init()
toggle_button_run = pygame.Rect(30, 10, 80, 30)
toggle_button_snake = pygame.Rect(30, 50, 80, 30)
toggle_button_counter = pygame.Rect(30, 90, 80, 30)
toggle_button_font = pygame.font.Font(None, 24)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Ant Colony Simulator")
    clock = pygame.time.Clock()
    pygame.draw.rect(screen, (120, 200, 200), (0, 0, 200, 100))  # (x, y, width, height)

    ants = []
    for x in range(50):
        ant = Ant(random.randint(0, 600), random.randint(0, 800))
        ants.append(ant)

    running = True
    snake = False
    while running:
        mouse_pos = pygame.mouse.get_pos()
        # proper closing (from the internet)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click is inside the toggle button
                if toggle_button_run.collidepoint(event.pos):
                    for ant in ants:
                        ant.toggle_run_away()
                if toggle_button_snake.collidepoint(event.pos):
                    snake = not snake
                if toggle_button_counter.collidepoint(event.pos):
                    snake = not snake
        
        if not snake:
            #draws over previous ants
            screen.fill((255, 255, 255))

        pygame.draw.rect(screen, (200, 200, 200), toggle_button_run)
        pygame.draw.rect(screen, (200, 200, 200), toggle_button_snake)
        pygame.draw.rect(screen, (200, 200, 200), toggle_button_counter)
        if ants[0].run_away:
            color = (120, 100, 255)
        else:
            color = (0, 0, 0) 
        if snake:
            color2 = (120, 100, 255)
        else:
            color2 = (0, 0, 0)

        toggle_button_surface = toggle_button_font.render("Run", True, color)
        toggle_button_run_center = toggle_button_surface.get_rect(center=toggle_button_run.center)
        screen.blit(toggle_button_surface, toggle_button_run_center)
        toggle_button_surface2 = toggle_button_font.render("Snake", True, color2)
        toggle_button_snake_center = toggle_button_surface2.get_rect(center=toggle_button_snake.center)
        screen.blit(toggle_button_surface2, toggle_button_snake_center)
        toggle_button_surface3 = toggle_button_font.render("ant", True, (0, 0, 0))
        toggle_button_counter_center = toggle_button_surface3.get_rect(center=toggle_button_counter.center)
        screen.blit(toggle_button_surface3, toggle_button_counter_center)

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