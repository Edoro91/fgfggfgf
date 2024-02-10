import pygame


a = float(input("Enter int1: "))
b = float(input("Enter int2: "))
res = a + b

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
FPS = 60
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
imp = pygame.image.load("C:\\Users\\Think Admin\\Downloads\\python.png").convert()

pygame.init()
font = pygame.font.SysFont(None, 100)
text = font.render(f'{res}', True, "black")
imp = pygame.transform(imp)


clock = pygame.time.Clock()
color = (255, 255, 255)
window.fill(color)
# window.blit(imp, (0, 0))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    window.blit(text, (100, 100))
    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)