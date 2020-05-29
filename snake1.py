from os import system
from time import sleep
import pygame
import random
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake1")
clock = pygame.time.Clock()

class food(object):
    def __init__(self, x1, y1, width1, height1, color):
        self.x1 = x1
        self.y1 = y1
        self.width1 = width1
        self.height1 = height1
        self.color = color
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x1, self.y1, self.width1, self.height1))
    def redraw(self, win):
        pygame.draw.rect(win, self.color, (self.x1, self.y1, 100, 100))

x = 300
y = 300
vel = 100
length = 1
Score = 0

win.fill((205, 250,  250))
foods = []
run = True
foods.append(food(100, 100, 100, 100, (0, 0, 0)))
while run:
    pygame.time.delay(150)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    import random
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    elif keys[pygame.K_RIGHT] and x < 400:
        x += vel
    elif keys[pygame.K_UP] and y > 0:
        y -= vel
    elif keys[pygame.K_DOWN] and y < 400:
        y += vel
    win.fill((205, 250, 250))
    pygame.draw.rect(win, (50, 205, 50), (x, y, 100, 100))
 #   pygame.draw.rect(win, (50, 205, 50), (x - 100, y, 100, 100))
    #pygame.draw.rect(win, (0, 0, 255), (random.random() * 1000, random.random() * 500, 15, 15))
    for food in foods:
        food.draw(win)
    if x == food.x1 and y == food.y1:
        Score += 100
    if x == food.x1 and y == food.y1:
        index = length
        length += 1

    if x == food.x1 and y == food.y1:
        food.x1 = (random.randint(0, 4) * 100)
        food.y1 = (random.randint(0, 4) * 100)
        food.redraw(win)
        #        pygame.draw(win, print("Score = " + Score))#print("Score :" + Score)
    #        pygame.font.init()
    #        myfont = pygame.font.SysFont('Aerial Black', 20)
    #       textsurface = myfont.render('Score =' + Score, False, (0, 0, 0))
    #        win.blit(textsurface, (590, 990))
    print(Score)
    print(length)
    pygame.display.update()
pygame.quit()