import os
import sys
import pygame
from animated_sprite import AnimatedSprite
from moviepy.editor import VideoFileClip


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

clip = VideoFileClip('static/video/Intro.mp4', target_resolution=size[::-1])
clip.set_fps(60)
clip.preview()

left_sprites = pygame.sprite.Group()
right_sprites = pygame.sprite.Group()
stand_sprites_R = pygame.sprite.Group()
stand_sprites_L = pygame.sprite.Group()

Man_stand_R = AnimatedSprite(load_image(
    'Космонавт Синий\Космонавт_stand_R_ALL.png'), 8, 1, 50, 50, stand_sprites_R)
Man_stand_L = AnimatedSprite(load_image(
    'Космонавт Синий\Космонавт_stand_L_ALL.png'), 8, 1, 50, 50, stand_sprites_L, 1)
Man_Go_R = AnimatedSprite(load_image(
    'Космонавт Синий\Космонавт_run_R_ALL.png'), 8, 1, 50, 50, right_sprites)
Man_Go_L = AnimatedSprite(load_image(
    'Космонавт Синий\Космонавт_run_L_ALL.png'), 8, 1, 50, 50, left_sprites, 1)
All_sprites = [Man_stand_R, Man_stand_L, Man_Go_R, Man_Go_L]


sound = pygame.mixer.music.load("static/audio/Tehcno fight.mp3")
pygame.mixer.music.play()

LastPose = 'R'
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w] and pressed_key[pygame.K_a]:
        for i in All_sprites:
            i.rect.y -= 3
            i.rect.x -= 3
        left_sprites.draw(screen)
        left_sprites.update()
    elif pressed_key[pygame.K_w] and pressed_key[pygame.K_d]:
        for i in All_sprites:
            i.rect.y -= 3
            i.rect.x += 3
        right_sprites.draw(screen)
        right_sprites.update()
    elif pressed_key[pygame.K_s] and pressed_key[pygame.K_a]:
        for i in All_sprites:
            i.rect.y += 3
            i.rect.x -= 3
        left_sprites.draw(screen)
        left_sprites.update()
    elif pressed_key[pygame.K_s] and pressed_key[pygame.K_d]:
        for i in All_sprites:
            i.rect.y += 3
            i.rect.x += 3
        right_sprites.draw(screen)
        right_sprites.update()
    elif pressed_key[pygame.K_w]:
        for i in All_sprites:
            i.rect.y -= 5
        if LastPose == "L":
            left_sprites.draw(screen)
            left_sprites.update()
        else:
            right_sprites.draw(screen)
            right_sprites.update()
    elif pressed_key[pygame.K_s]:
        for i in All_sprites:
            i.rect.y += 5
        if LastPose == "L":
            left_sprites.draw(screen)
            left_sprites.update()
        else:
            right_sprites.draw(screen)
            right_sprites.update()
    elif pressed_key[pygame.K_a]:
        for i in All_sprites:
            i.rect.x -= 4
        left_sprites.draw(screen)
        left_sprites.update()
        LastPose = "L"
    elif pressed_key[pygame.K_d]:
        for i in All_sprites:
            i.rect.x += 4
        right_sprites.draw(screen)
        right_sprites.update()
        LastPose = "R"
    elif not (pressed_key[pygame.K_w] or pressed_key[pygame.K_s] or
              pressed_key[pygame.K_a] or pressed_key[pygame.K_d]):
        if LastPose == "L":
            stand_sprites_L.draw(screen)
            stand_sprites_L.update()
        else:
            stand_sprites_R.draw(screen)
            stand_sprites_R.update()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
