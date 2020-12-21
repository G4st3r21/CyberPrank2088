import os
import sys
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('sprites/', name)

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


def mouse_regarding_Hero(mouse, hero):
    if mouse.sprite.rect.x > hero.Man_Go_R.rect.x:
        hero.LastPose = 'R'
    elif mouse.sprite.rect.x < hero.Man_Go_R.rect.x:
        hero.LastPose = 'L'
