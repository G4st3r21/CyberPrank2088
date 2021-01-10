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
    if mouse.sprite.rect.centerx > hero.Man_Go_R.rect.centerx:
        hero.LastPose = 'R'
    elif mouse.sprite.rect.centerx < hero.Man_Go_R.rect.centerx:
        hero.LastPose = 'L'


def Dev_mode(screen, player, pistol, zombie, fps, angle=0):
    font = pygame.font.Font('static/fonts/19888.ttf', 20)
    player_pos = (player.Man_stand_R.rect.centerx,
                  player.Man_stand_R.rect.centery)
    pistol_pos = (pistol.Pistol_R.rect.centerx,
                  pistol.Pistol_R.rect.centery)
    zombie_pos = (zombie.Man_stand_R.rect.centerx,
                  zombie.Man_stand_R.rect.centery)
    angle = angle
    text1 = font.render(f'Players coords: {player_pos}', True, (0, 0, 255))
    text2 = font.render(f'Pistol coords: {pistol_pos}', True, (0, 0, 0))
    text3 = font.render(f'Zombie Strench: {zombie.Strench}', True, (0, 0, 0))
    text4 = font.render(f'Zombie coords: {zombie_pos}', True, (0, 255, 0))
    text5 = font.render(f'FPS: {fps}', True, (0, 0, 0))
    screen.blit(text1, (200, 870))
    screen.blit(text2, (200, 890))
    screen.blit(text3, (200, 910))
    screen.blit(text4, (200, 930))
    screen.blit(text5, (200, 950))
