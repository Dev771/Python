import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake")
x = 300
y = 300
i = 0
j = 0
vel = 100
length = 1
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
snake = []
run = True
while run:
    pygame.time.delay(150)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    elif keys[pygame.K_RIGHT] and x < 400:
        x += vel
    elif keys[pygame.K_UP] and y > 0:
        y -= vel
    elif keys[pygame.K_DOWN] and y < 500:
        y += vel
    win.fill((205, 250, 250))
    pygame.draw.rect(win, (50, 205, 50), (x, y, 100, 100))
    pygame.draw.rect(win , (0, 0, 0), (0, 0, 100, 100))
    if y == 400 and keys[pygame.K_DOWN]:
        while not(keys[pygame.K_ESCAPE]):
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render('Game Over', True, green, blue)
            textRect = text.get_rect()
            textRect.center = (300, 300)
            win.blit(text, textRect)
        break
#    if x == 0 and y == 0:
#        if keys[pygame.K_LEFT]:
#            snake.append("l")
#        elif keys[pygame.K_RIGHT]:
#            snake.append("r")
#        if keys[pygame.K_UP]:
#            snake.append("u")
#        elif keys[pygame.K_DOWN]:
#            snake.append("d")
#        if snake[0] == "l":
#            pygame.draw.rect(win, (250, 205, 52), (x + 100, y, 100, 100))
    print(snake)
    pygame.display.update()
pygame.quit()