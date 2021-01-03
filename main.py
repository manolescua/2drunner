import pygame

pygame.init()
win = pygame.display.set_mode((700,394))
pygame.display.set_caption("first game")
bg = pygame.image.load('resources/background/bg_resized.png')
mage = pygame.image.load('resources/character/mage/walk1-R.png')
mage_r = [pygame.image.load('resources/character/mage/walk1-R.png'),
          pygame.image.load('resources/character/mage/walk2-R.png'),
          pygame.image.load('resources/character/mage/walk3-R.png'),
          pygame.image.load('resources/character/mage/walk4-R.png'),
          pygame.image.load('resources/character/mage/walk5-R.png'),
          pygame.image.load('resources/character/mage/walk6-R.png')]

mage_l = [pygame.image.load('resources/character/mage/walk1-L.png'),
          pygame.image.load('resources/character/mage/walk2-L.png'),
          pygame.image.load('resources/character/mage/walk3-L.png'),
          pygame.image.load('resources/character/mage/walk4-L.png'),
          pygame.image.load('resources/character/mage/walk5-L.png'),
          pygame.image.load('resources/character/mage/walk6-L.png')]

x = 100
y = 280
width = 40
height = 50
left = False
right = True
walkCount = 0
standing = True


run = True
vel = 5

isJump = False
jumpCount = 10


def redrawGameWindow():
    global walkCount
    win.fill((0, 0, 0))
    win.blit(bg, (0, 0))  # This will draw our background image at (0,0)
    if walkCount + 1 >= 18:
        walkCount = 0
    if not(standing):
        if left:
            win.blit(mage_l[walkCount//3], (x,y))
            walkCount = walkCount + 1
        elif right:
            win.blit(mage_r[walkCount // 3], (x,y))
            walkCount = walkCount + 1
    else:
        if left:
            win.blit(mage_l[0], (x, y))
        elif right:
            win.blit(mage_r[0], (x, y))

    pygame.display.update()

while run:
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and x < 660:
        x = x + vel
        left = False
        right = True
        standing = False
    elif keys[pygame.K_LEFT] and x > 0:
        x = x - vel
        left = True
        right = False
        standing = False
    else:
        standing = True
        walkCount = 0

    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    redrawGameWindow()
pygame.quit()
