import os
import sys
import pygame

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
pygame.mouse.set_visible(False)


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

sprite.image = load_image("arrow.png")
sprite.rect = sprite.image.get_rect()
all_sprites.add(sprite)
clock = pygame.time.Clock()
tickrate = 60
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    if pygame.mouse.get_focused():
        pos = pygame.mouse.get_pos()
        sprite.rect.x, sprite.rect.y = pos[0], pos[1]
    screen.fill("black")
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(tickrate)