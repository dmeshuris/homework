import pygame

pygame.init()

background_color = (225,0,127)
screenX = 1000
screenY = 1000

screen = pygame.display.set_mode((screenX, screenY))

pygame.display.set_caption('moving square')

screen.fill(background_color)

pygame.display.flip()

x, y = 0, 0
w, h = 500, 500
v = 10

clock = pygame.time.Clock()
running = True

while running:
    clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= v
    if keys[pygame.K_RIGHT] and x < screenX - w:
        x += v
    if keys[pygame.K_UP] and y > 0:
        y -= v
    if keys[pygame.K_DOWN] and y < screenY - h:
        y += v

    screen.fill(background_color)
    pygame.draw.rect(screen, (0, 225, 225), (x, y, w, h), v)

    pygame.display.update()