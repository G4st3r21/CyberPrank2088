import pygame
import os
import Fuctions
from random import choice
from moviepy.editor import VideoFileClip
import Heroes_class as hc
import Guns_class as gc
import Settings as st

# ------------------------GAME INITIALIZATION------------------------- #

pygame.init()
size = st.Change_Resolution()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

player = hc.Players_Hero('Синий', screen, 0, 1, 0)

zombie1 = hc.Zombie(screen, (choice(range(300, 900)), choice(range(300, 900))))
zombie2 = hc.Zombie(screen, (choice(range(300, 900)), choice(range(300, 900))))
zombie3 = hc.Zombie(screen, (choice(range(300, 900)), choice(range(300, 900))))

mouse = gc.Mouse('Arrows/Arrow6.png', 'Arrows/Arrow6.1.png', screen)
pistol = gc.Pistol(screen, player, mouse)

# -----------------------------GAME INTRO----------------------------- #

clip = VideoFileClip('static/video/Intro.mp4', target_resolution=size[::-1])
clip.set_fps(st.FPS)
clip.preview()

# -----------------------------GAME MUSIC----------------------------- #

All_Gameplay_Music = [i for i in os.listdir('static/audio/fighting')]
print(All_Gameplay_Music)
sound = pygame.mixer.music.load('/'.join(['static/audio/fighting',
                                          choice(All_Gameplay_Music)]))
pygame.mixer.music.play()
pygame.mixer.music.set_volume(st.Volume)

# ----------------------------GAME WORKING---------------------------- #

running = True
fire = 0
Firing = 0
DEV_MODE = 1
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
            print('ЛКМ')
        elif event.type == pygame.MOUSEBUTTONUP:
            fire = 0
            Firing = 0
            print('Отпустил')

    # -----------------------DEV MODE------------------------- #
    if pressed_key[pygame.K_LSHIFT] and pressed_key[pygame.K_p] and DEV_MODE:
        DEV_MODE = 0
        print('DEV MODE OFF')
    elif pressed_key[pygame.K_LSHIFT] and \
            pressed_key[pygame.K_p] and not DEV_MODE:
        DEV_MODE = 1
        print('DEV MODE ON')

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

    # ---------------------TESTING ZOMBIE------------------------ #

    player.Damage(zombie1)
    zombie1.find_Hero(player.Man_stand_R.rect)
    # zombie2.find_Hero(player.Man_stand_R.rect)
    # zombie3.find_Hero(player.Man_stand_R.rect)

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

    # -----------------------SETTINGS-------------------------- #

    if pressed_key[pygame.K_z]:
        st.Change_Volume(0.3)
    elif pressed_key[pygame.K_x]:
        st.Change_Volume(0.7)
    elif pressed_key[pygame.K_c]:
        size = st.Change_Resolution('HD+')
        screen = pygame.display.set_mode(size)
    elif pressed_key[pygame.K_v]:
        size = st.Change_Resolution('HD')
        screen = pygame.display.set_mode(size)
    elif pressed_key[pygame.K_b]:  # BACK TO DEFAULT SETTINGS
        st.Change_Volume()
        size = st.Change_Resolution()
        screen = pygame.display.set_mode(size)

    # ----------------------MOUSE ARROW and FIRING------------------------- #

    if pygame.mouse.get_focused():
        if fire:
            mSprite = mouse.mouse_spritesGet2()
            mSprite.draw(screen)
            Firing = pistol.FireAnimOn()
        else:
            mSprite = mouse.mouse_spritesGet1()
            mSprite.draw(screen)
            pistol.drawPistol()

    gc.bullets.draw(screen)
    gc.bullets.update()

    if DEV_MODE:
        Fuctions.Dev_mode(screen, player, pistol, zombie1)

    Fuctions.mouse_regarding_Hero(mouse, player)
    pygame.display.flip()

    clock.tick(st.FPS)

pygame.quit()
