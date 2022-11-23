import pygame
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.image = pygame.Surface((20,20))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = [posX, posY]

pygame.init()
clock = pygame.time.Clock()

screenWidth = 1200
screenHight = 700
screen = pygame.display.set_mode((screenWidth,screenHight))
pygame.display.set_caption("...")

playerGroup = pygame.sprite.Group()
Player = Player(600, 350)
playerGroup.add(Player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))
    playerGroup.draw(screen)
    pygame.display.flip()
    clock.tick(60)