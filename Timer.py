import pygame, sys

pygame.init()
screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()

currentTime = 0
buttonPresstTime = 0 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            buttonPresstTime = pygame.time.get_ticks()
            screen.fill((255,255,255))

    currentTime = pygame.time.get_ticks()

    if currentTime - buttonPresstTime > 2000:
        screen.fill((0,0,0))

    print("Current time: ", currentTime, "Button Press time: ", buttonPresstTime)
    pygame.display.flip()
    clock.tick(60)