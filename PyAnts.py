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
        self.run_away = False
    def update(self, mousePos):
        # distance of ant from mouse
        dx = mousePos[0] - self.x
        dy = mousePos[1] - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if random.random() < 0.05:
            self.direction = random.randint(0, 360)
        # if distance away from mouse is within 50, then reverse the angle to run away from the mouse
        if distance < 50:
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
        pygame.draw.circle(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (int(self.x), int(self.y)), size)
    
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
    pygame.display.set_caption("Gay Ant Colony Simulator")
    clock = pygame.time.Clock()

    # Create plus and minus button rectangles
    plus_button_rect = pygame.Rect(75, 90, 30, 30)
    minus_button_rect = pygame.Rect(30, 90, 30, 30)
    ants = []
    for x in range(150):
        ant = Ant(random.randint(0, 600), random.randint(0, 800))
        ants.append(ant)

    running = True
    snake = False
    antCounter = 50
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
                if plus_button_rect.collidepoint(event.pos):
                    if (antCounter < 150):
                        antCounter += 1
                if minus_button_rect.collidepoint(event.pos):
                    antCounter -= 1
        
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

        # Draw plus button
        pygame.draw.rect(screen, (200, 200, 200), plus_button_rect)
        plus_button_center = plus_button_rect.center
        plus_button_half_length = 7
        pygame.draw.line(screen, (0, 0, 0), (plus_button_center[0] - plus_button_half_length, plus_button_center[1]), (plus_button_center[0] + plus_button_half_length, plus_button_center[1]), 3)
        pygame.draw.line(screen, (0, 0, 0), (plus_button_center[0], plus_button_center[1] - plus_button_half_length), (plus_button_center[0], plus_button_center[1] + plus_button_half_length), 3)
        
        # Draw minus button
        pygame.draw.rect(screen, (200, 200, 200), minus_button_rect)
        minus_button_center = minus_button_rect.center
        minus_button_half_length = 7
        pygame.draw.line(screen, (0, 0, 0), (minus_button_center[0] - minus_button_half_length, minus_button_center[1]), (minus_button_center[0] + minus_button_half_length, minus_button_center[1]), 3)

        # Render run, snake, and counter buttons
        toggle_button_surface = toggle_button_font.render("Run", True, color)
        toggle_button_run_center = toggle_button_surface.get_rect(center=toggle_button_run.center)
        screen.blit(toggle_button_surface, toggle_button_run_center)
        toggle_button_surface2 = toggle_button_font.render("Snake", True, color2)
        toggle_button_snake_center = toggle_button_surface2.get_rect(center=toggle_button_snake.center)
        screen.blit(toggle_button_surface2, toggle_button_snake_center)
        toggle_button_surface3 = toggle_button_font.render(str(antCounter), True, (0, 0, 0))
        toggle_button_counter_center = toggle_button_surface3.get_rect(center=toggle_button_counter.center)
        screen.blit(toggle_button_surface3, toggle_button_counter_center)
        
        # draw new ant based on updated x and y info
        for x in range(antCounter):
            ants[x].update(mouse_pos)
            ants[x].draw(screen)

        # makes changes visible to screen
        pygame.display.flip()
        # framerate
        clock.tick(60)
    
    pygame.quit()
if __name__ == "__main__":
    main()
