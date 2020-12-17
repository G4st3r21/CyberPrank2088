import os
import sys
import pygame
from animated_sprite import AnimatedSprite


def load_image(name, colorkey=None):
    fullname = os.path.join('sprites\Космонавт', name)

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


pygame.init()
size = width, height = 1440, 720
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Player moving')
clock = pygame.time.Clock()
FPS = 60

left_sprites = pygame.sprite.Group()
right_sprites = pygame.sprite.Group()
stand_sprites = pygame.sprite.Group()

Man_stand = AnimatedSprite(load_image(
    'Космонавт Синий\Космонавт_stand_R_ALL.png'), 8, 1, 50, 50, stand_sprites)
Man_Go_R = AnimatedSprite(load_image(
    'Космонавт Синий\Космонавт_run_R_ALL.png'), 8, 1, 50, 50, right_sprites)
Man_Go_L = AnimatedSprite(load_image(
    'Космонавт Синий\Космонавт_run_L_ALL.png'), 8, 1, 50, 50, left_sprites)
All_sprites = [Man_stand, Man_Go_R, Man_Go_L]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        for i in All_sprites:
            i.rect.y -= 5
        stand_sprites.draw(screen)
        stand_sprites.update()
    elif pressed_key[pygame.K_s]:
        for i in All_sprites:
            i.rect.y += 5
        stand_sprites.draw(screen)
        stand_sprites.update()
    elif pressed_key[pygame.K_a]:
        for i in All_sprites:
            i.rect.x -= 4
        left_sprites.draw(screen)
        left_sprites.update()
    elif pressed_key[pygame.K_d]:
        for i in All_sprites:
            i.rect.x += 4
        right_sprites.draw(screen)
        right_sprites.update()
    elif not (pressed_key[pygame.K_w] or pressed_key[pygame.K_s] or
              pressed_key[pygame.K_a] or pressed_key[pygame.K_d]):
        stand_sprites.draw(screen)
        stand_sprites.update()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
