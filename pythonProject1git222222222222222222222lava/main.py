import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800

pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()