import pygame, sys, random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.posX = 35
        self.posY = 350

        self.isAnimating = False
        self.sprites = []
        self.sprites.append(pygame.image.load(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\PygamePractice\Assets\FlappyBird\Transparent PNG\frame-1.png"))
        self.sprites.append(pygame.image.load(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\PygamePractice\Assets\FlappyBird\Transparent PNG\frame-2.png"))

        self.currentSprite = 0
        self.image = self.sprites[self.currentSprite]
        self.size = self.image.get_size()
        pygame.transform.scale(self.image, (self.size[0]*1.5, self.size[1]*1.5))

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.posX, self.posY]

    def jump(self):
        self.isAnimating = True

        if self.posY - 10 >= 0:
            self.newY = 10
        else:
            self.newY = 0

    def gravity(self):
        self.posY += 5

    def gameOver(self):
        gets_hit = pygame.sprite.spritecollide(Player, Pipes, False)
        if self.posY >= 700 or gets_hit != []:
            pygame.quit()
            sys.exit()


    def update(self):
        if self.isAnimating == True:
            self.currentSprite += 0.2
            self.posY -= self.newY

            if self.currentSprite  >= len(self.sprites):
                self.isAnimating = False
                self.currentSprite = 0

            self.image = self.sprites[int(self.currentSprite)]

        self.rect.topleft = [self.posX, self.posY]
   
class TopPipe(pygame.sprite.Sprite):
    def __init__(self, diff):
        super().__init__()
        self.posX = 1100
        self.posY = 0 + diff

        self.image = pygame.image.load(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\PygamePractice\Assets\FlappyBirdPipes\topPipe.png")
        self.rect = self.image.get_rect()
        self.rect.center = [self.posX, self.posY]
        
    def update(self):
        self.posX -= 7.5
        self.rect.center = [self.posX, self.posY]

class BottomPipe(pygame.sprite.Sprite):
    def __init__(self, diff):
        super().__init__()
        self.posX = 1100
        self.posY = 700 + diff

        self.image = pygame.image.load(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\PygamePractice\Assets\FlappyBirdPipes\bottomPipe.png")
        self.rect = self.image.get_rect()
        self.rect.center = [self.posX, self.posY]

    def update(self):
        self.posX -= 7.5
        self.rect.center = [self.posX, self.posY]

pygame.init()
clock = pygame.time.Clock()

screenWidth = 1200
screenHight = 700
screen = pygame.display.set_mode((screenWidth,screenHight))
background = pygame.image.load(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\PygamePractice\Assets\Misc\HorizonBG.png")
pygame.display.set_caption("Flappy Bird")

pygame.mixer.init()
bgMusic = pygame.mixer.Sound(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\PygamePractice\Assets\Audios\choco birds run.wav")
bgMusic.set_volume(0.7)
bgMusic.play(10)

playerGroup = pygame.sprite.Group()
Player = Player()
playerGroup.add(Player)

Pipes = pygame.sprite.Group()
def makePipes(Pipes):
    diff = random.randrange(-200, 200, 20)
    newTopPipe = TopPipe(diff)
    newBottomPipe = BottomPipe(diff)
    Pipes.add(newTopPipe, newBottomPipe)

count = 75
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            Player.jump()

    if count == 75:
        count = 0
        makePipes(Pipes)
    count += 1

    screen.blit(background, (0,0))
    playerGroup.draw(screen)
    playerGroup.update()

    Pipes.draw(screen)
    Pipes.update()

    Player.gravity()
    Player.gameOver()
    
    pygame.display.flip()
    clock.tick(60)
    