import os
import sys
import pygame
import random

pygame.init()
size = width, height = 600, 300
screen = pygame.display.set_mode(size)
screen.fill("blue")
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


class go(pygame.sprite.Sprite):
    image = load_image("gameover.png")

    def __init__(self, *group):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(*group)
        self.image = go.image
        self.rect = self.image.get_rect()
        self.rect.x = -600
        self.rect.y = 0
        self.speed = 200/60

    def update(self):
        if self.rect.x + self.speed <= 0:
            self.rect.x += self.speed
        else:
            self.rect.x = 0

go(all_sprites)
clock = pygame.time.Clock()
tickrate = 60
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    screen.fill("blue")
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(tickrate)
