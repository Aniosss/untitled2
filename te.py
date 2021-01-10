import os
import sys
import pygame

pygame.init()
size = width, height = 600, 95
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
pygame.mouse.set_visible(True)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


right = True


def update():
    global right
    if right:
        if mx + sprite.rect.x + move < 600:
            sprite.rect.x += move
        else:
            sprite.image = pygame.transform.flip(sprite.image, True, False)
            right = False
    else:
        if sprite.rect.x - move > 0:
            sprite.rect.x -= move
        else:
            sprite.image = pygame.transform.flip(sprite.image, True, False)
            right = True


sprite.image = load_image("car2.png")
sprite.rect = sprite.image.get_rect()
mx = sprite.image.get_size()[0]
all_sprites.add(sprite)
clock = pygame.time.Clock()
tickrate = 60
move = 3
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    update()
    screen.fill("white")
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(tickrate)
