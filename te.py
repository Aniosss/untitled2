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


class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.right = True
        self.image = load_image("car2.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.y = 0
        self.size = self.image.get_size()

    def update(self):
        if self.right:
            if self.size[0] + self.rect.x + move < 600:
                self.rect.x += move
            else:
                self.image = pygame.transform.flip(self.image, True, False)
                self.right = False
        else:
            if self.rect.x - move > 0:
                self.rect.x -= move
            else:
                self.image = pygame.transform.flip(self.image, True, False)
                self.right = True

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


car = Car()
clock = pygame.time.Clock()
tickrate = 60
move = 3
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    screen.fill("white")
    car.draw(screen)
    car.update()
    pygame.display.flip()
    clock.tick(tickrate)
