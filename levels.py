import os
import pygame

pygame.init()

fps = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0))


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


WIDTH = 1440
HEIGHT = 1080

screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Levels(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('all_rooms.png'), (1024, 1024))

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Levels.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)


all_sprites = pygame.sprite.Group()
level = Levels()
running = True

screen.fill((0, 0, 0))
all_sprites.draw(screen)
all_sprites.update()
pygame.display.flip()
clock.tick(fps)

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()
pygame.quit()
