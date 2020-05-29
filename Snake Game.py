import pygame
pygame.init()
win = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("The Snake Game")
clock = pygame.time.Clock()
class snake(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 50
        self.color = color
        self.left = False
        self.right = False
        self.up = False
        self.down = False

    def draw(self, win):
       pygame.draw.rect(win, (250, 0, 0), (100, 20, 25, 25))

#class food(object):
#    def __init__(self, x, y, radius, color):
#        self.x = x
#        self.y = y
#        self.color = color
#        self.radius = radius

#    def draw(self, win):
#        for i in range(0, 1000):
#            for j in range(0, 800):
#                pygame.draw.circle(win, (250, 0, 0), (i, j), 15)
#def redrawGameWindow():
#    snake.draw(player, win)
 #   for food in fruit:
#       food.draw(win)

player = snake(100, 20, 25, 25, (250, 0, 0))
#fruit = []
run = True
while run:
    clock.tick(27)
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#    if len(fruit) < 1:
#        for i in range(0, 1000):
#            for j in range(0, 800):
#                fruit.append(food(i, j, 15, (250, 0, 0)))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= player.vel
        player.up = True
        player.down = False
        player.right = False
        player.left = False

    elif keys[pygame.K_DOWN]:
        player.y += player.vel
        player.up = False
        player.down = True
        player.right = False
        player.left = False

    elif keys[pygame.K_RIGHT]:
        player.x += player.vel
        player.up = False
        player.down = False
        player.right = True
        player.left = False

    elif keys[pygame.K_LEFT]:
        player.x -= player.vel
        player.up = False
        player.down = False
        player.right = False
        player.left = True

    snake.draw(player, win)
    pygame.draw.rect(win,(250, 0, 0), (100, 20, 25, 25))
    pygame.display.update()

#    redrawGameWindow()


pygame.quit()

