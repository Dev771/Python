import pygame
pygame.init()
screenwidth = 500
screenheight = 500
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("New Box")
WalkRight = [pygame.image.load('C:\\Users\\User\\Desktop\\Game\\R1.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\R2.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\R3.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\R4.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\R5.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\R6.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\R7.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\R8.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\R9.png')]
WalkLeft = [pygame.image.load('C:\\Users\\User\\Desktop\\Game\\L1.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\L2.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\L3.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\L4.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\L5.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\L6.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\L7.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\L8.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\L9.png')]
bg = pygame.image.load('C:\\Users\\User\\Desktop\\Game\\bg.jpg')
char = pygame.image.load('C:\\Users\\User\\Desktop\\Game\\standing.png')
clock = pygame.time.Clock()
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = height
        self.height = width
        self.vel = 5
        self.is_jump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(WalkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(WalkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(WalkRight[0], (self.x, self.y))
            else:
                win.blit(WalkLeft[0], (self.x, self.y))


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 10 * facing

    def draw(self, win):
       pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class enemy(object):
    WalkRight = [pygame.image.load('C:\\Users\\User\\Desktop\\Game\\R1E.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\R2E.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\R3E.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\R4E.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\R5E.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\R6E.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\R7E.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\R8E.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\R9E.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\R10E.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\R11E.png')]
    WalkLeft = [pygame.image.load('C:\\Users\\User\\Desktop\\Game\\L1E.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\L2E.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\L3E.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\L4E.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\L5E.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\L6E.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\L7E.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\L8E.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\L9E.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\L10E.png'), pygame.image.load('C:\\Users\\User\\Desktop\\Game\\L11E.png')]
    def __init__(self, x, y, height, width, end):
        self.x = x
        self.y = y
        self.vel = 3
        self.height = height
        self.end = end
        self.width = width
        self.path = [self.x, self.end]
        self.walkcount = 0
    def draw(self, win):
        self.move()
        if self.walkcount + 1 >= 33:
            walkcount = 0

        #pass
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkcount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkcount = 0
def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()
#mainloop
man = player(200, 410, 64, 64)
bullets = []
run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))
    if keys[pygame.K_LEFT] and man.x > 0:
        man.x -= man.vel
        man.right = False
        man.left = True
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < screenwidth-50:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
    if not(man.is_jump):
        if keys[pygame.K_UP]:
            man.is_jump = True
            man.left = False
            man.right = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.is_jump = False
            man.jumpCount = 10
    redrawGameWindow()




pygame.quit()