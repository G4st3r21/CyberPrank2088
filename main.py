import pygame
import os
import Fuctions
from random import choice
from moviepy.editor import VideoFileClip
from Heroes_class import Players_Hero, Mouse, Zombie


Resolutions = {
    'FHD': (1920, 1080),
    'HD+': (1440, 1080),
    'HD': (1080, 720),
    'HQ': (800, 600)
}

# ------------------------GAME INITIALIZATION------------------------- #

pygame.init()
size = Resolutions['HQ']
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 60

player = Players_Hero('Синий', screen)

zombie1 = Zombie(screen, (choice(range(300, 900)), choice(range(300, 900))))
zombie2 = Zombie(screen, (choice(range(300, 900)), choice(range(300, 900))))
zombie3 = Zombie(screen, (choice(range(300, 900)), choice(range(300, 900))))

mouse = Mouse('Arrow6.png', 'Arrow6.1.png', screen)

# -----------------------------GAME INTRO----------------------------- #

clip = VideoFileClip('static/video/Intro.mp4', target_resolution=size[::-1])
clip.set_fps(60)
clip.preview()

# -----------------------------GAME MUSIC----------------------------- #

All_Gameplay_Music = [i for i in os.listdir('static/audio/fighting')]
print(All_Gameplay_Music)
sound = pygame.mixer.music.load('/'.join(['static/audio/fighting',
                                          choice(All_Gameplay_Music)]))
pygame.mixer.music.play()

# ----------------------------GAME WORKING---------------------------- #

running = True
fire = 0
Color = 'White'
while running:

    screen.fill(pygame.Color(Color))
    pressed_key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            mouse.DrawArrow(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            fire = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            fire = 0

    # ------------------------Moving-------------------------- #

    player.Cycle_moving(size)

    if pressed_key[pygame.K_w] and pressed_key[pygame.K_a]:
        player.Move_UL()
    elif pressed_key[pygame.K_w] and pressed_key[pygame.K_d]:
        player.Move_UR()
    elif pressed_key[pygame.K_s] and pressed_key[pygame.K_a]:
        player.Move_DL()
    elif pressed_key[pygame.K_s] and pressed_key[pygame.K_d]:
        player.Move_DR()
    elif pressed_key[pygame.K_w]:
        player.Move_Up()
    elif pressed_key[pygame.K_s]:
        player.Move_Down()
    elif pressed_key[pygame.K_a]:
        player.Move_Left()
    elif pressed_key[pygame.K_d]:
        player.Move_Right()
    elif not (pressed_key[pygame.K_w] or pressed_key[pygame.K_s] or
              pressed_key[pygame.K_a] or pressed_key[pygame.K_d]):
        player.Stand()

    # -------------TESTING SPRITES ABOVE COLORS--------------- #

    if pressed_key[pygame.K_1]:
        Color = 'Black'
    elif pressed_key[pygame.K_2]:
        Color = 'White'
    elif pressed_key[pygame.K_3]:
        Color = 'Blue'
    elif pressed_key[pygame.K_4]:
        Color = 'Red'
    elif pressed_key[pygame.K_5]:
        Color = 'Green'

    # ----------------------MOUSE ARROW------------------------- #

    if pygame.mouse.get_focused():
        if fire:
            mSprite = mouse.mouse_spritesGet2()
            mSprite.draw(screen)
        else:
            mSprite = mouse.mouse_spritesGet1()
            mSprite.draw(screen)

    # ---------------------TESTING ZOMBIE------------------------ #

    player.Damage(zombie1)
    zombie1.find_Hero(player.Man_stand_R.rect)
    # zombie2.find_Hero(player.Man_stand_R.rect)
    # zombie3.find_Hero(player.Man_stand_R.rect)

    Fuctions.mouse_regarding_Hero(mouse, player)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
