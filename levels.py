import os
import pygame

pygame.init()

fps = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1920, 1080))


def load_image(name, color_key=None):
    fullname = os.path.join('sprites', name)
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


class Level(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(Level_sprites)
        super().__init__()
        image = pygame.transform.scale(
            load_image('data/all_rooms.png', -1), (4096, 4096))
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = -3050
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, player, size):
        pos = player.Cycle_moving(size)
        if pos == -1:
            return False
        elif pos == 0:
            return False
        elif pos[0] == 1:
            self.rect.x += 1024
            player.RoomIn += 1
        elif pos[1] == 1:
            self.rect.x -= 1024
            player.RoomIn += 1
        elif pos[2] == 1:
            self.rect.y += 1024
            player.RoomIn += 1
        elif pos[3] == 1:
            self.rect.y -= 1024
            player.RoomIn += 1


Level_sprites = pygame.sprite.Group()
