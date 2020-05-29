import pygame
pygame.init()
win = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Flappy Bird")


class Bird:
    def __init__(self, x, y, i, j, color):
        self.x = x
        self.y = y
        self.i = i
        self.j = j
        self.color = color

    def default_move(self, y):
        x = 200
        y += 10
        if y == 0 or y == 420:
            print("Game Over")
        else:
            pygame.draw.rect(win, (250, 50, 205), (200, y, 80, 80))

    def up_move(self, y):
        y -= 10
        pygame.draw.rect(win, (250, 50, 205), (200, y, 80, 80))

class Blocks:
    def __init__(self, x, y, color, i, j, u):
        self.x = x
        self.y = y
        self.color = color
        self.i = i
        self.j = j
        self.u = u

    def top(self, x, u):
        pygame.draw.rect(win, (250, 250, 250), (x, 0, 50, u))

import random
Flappy = Bird(200, 250, 80, 80, (250, 50, 205))
v = 250
u = random.randint(0, 2) * 100
k = 1000
run = True
while run:
    pygame.time.delay(150)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if not(keys[pygame.K_UP]):
        win.fill((0, 0, 0))
        Bird.default_move(win, v)
        v += 10
    else:
        for index in range(5):
            win.fill((0, 0, 0))
            Bird.up_move(win, v)
            v -= 10
    if v == 0 or v == 420:
        run = False
    import random
    if k == Flappy.y:
        print("g")
        break
    Blocks.top(win, k, u)
    k -= 10
    while k == 0:
        u = random.randint(0.5, 2) * 100
    pygame.display.update()
pygame.quit()