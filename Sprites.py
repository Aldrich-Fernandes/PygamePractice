import pygame, sys, random

class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\PygamePractice\Assets\Misc\Crosshair1.png")
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\PygamePractice\Assets\Audios\Magnum.wav")

    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\PygamePractice\Assets\Misc\Drone.png")
        self.rect = self.image.get_rect()
        self.rect.center = [posX, posY]

#General setup
pygame.init()
clock = pygame.time.Clock()

#Background music
pygame.mixer.init()
bgMusic = pygame.mixer.Sound(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\PygamePractice\Assets\Audios\Fiberitron Loop.wav")
bgMusic.set_volume(0.7)
bgMusic.play(10)

#Game Screen
screenWidth = 1000
screenHight = 750
screen = pygame.display.set_mode((screenWidth, screenHight))
background = pygame.image.load(r"C:\Users\Aldrich Fernandes\Python\Scripts\Projects\PygamePractice\Assets\Misc\CityscapeBG.png") 
pygame.mouse.set_visible(False)

#Crosshair
crosshair = Crosshair()
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

#target
target_group = pygame.sprite.Group()
def DrawTargets(target_group):
    TargetLocations = []
    count = 0
    while count != 10:
        posX = random.randrange(20, screenWidth-20)
        posY = random.randrange(20, screenHight-20)
        Location = posX, posY
        if Location not in TargetLocations:
            TargetLocations.append(Location)
            new_target = Target(posX, posY)
            target_group.add(new_target)
            count += 1

    TargetLocations.clear()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()
            
    if len(target_group) < 1:
        DrawTargets(target_group)

    pygame.display.flip()
    screen.blit(background, (0,0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)