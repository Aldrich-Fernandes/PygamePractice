import pygame
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.isAnimating = False
        self.sprites = []
        self.sprites.append(pygame.image.load(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\PygamePractice\Assets\FrogAttack\attack_1.png"))
        self.sprites.append(pygame.image.load(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\PygamePractice\Assets\FrogAttack\attack_2.png"))
        self.sprites.append(pygame.image.load(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\PygamePractice\Assets\FrogAttack\attack_3.png"))
        self.sprites.append(pygame.image.load(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\PygamePractice\Assets\FrogAttack\attack_4.png"))
        self.sprites.append(pygame.image.load(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\PygamePractice\Assets\FrogAttack\attack_5.png"))
        self.sprites.append(pygame.image.load(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\PygamePractice\Assets\FrogAttack\attack_6.png"))
        self.sprites.append(pygame.image.load(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\PygamePractice\Assets\FrogAttack\attack_7.png"))
        self.sprites.append(pygame.image.load(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\PygamePractice\Assets\FrogAttack\attack_8.png"))
        self.sprites.append(pygame.image.load(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\PygamePractice\Assets\FrogAttack\attack_9.png"))
        self.sprites.append(pygame.image.load(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\PygamePractice\Assets\FrogAttack\attack_10.png"))
        
        self.currentSprite = 0
        self.image = self.sprites[self.currentSprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [posX, posY]

    def animate(self):
        self.isAnimating = True

    def update(self):
        if self.isAnimating == True:
            self.currentSprite += 0.2

            if self.currentSprite  >= len(self.sprites):
                self.isAnimating = False
                self.currentSprite = 0

            self.image = self.sprites[int(self.currentSprite)]

pygame.init()
clock = pygame.time.Clock()

screenWidth = 400
screenHight = 400
screen = pygame.display.set_mode((screenWidth,screenHight))
pygame.display.set_caption("Sprite Animation")

playerGroup = pygame.sprite.Group()
Player = Player(100,100)
playerGroup.add(Player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            Player.animate()


    screen.fill((0,0,0))
    playerGroup.draw(screen)
    playerGroup.update()
    pygame.display.flip()
    clock.tick(60)