import pygame
import os
import Fuctions
from random import choice
import Settings as st
import Main_menu_classes as MM
from Guns_class import Mouse


pygame.init()
size = st.Change_Resolution()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


mouse = Mouse('Arrows/Arrow1.png', 'Arrows/Arrow1.1.png', screen)

spaces = [i for i in os.listdir('sprites/Main_menu/spaces')]
print(spaces)
space = '/'.join(['Main_menu/spaces', choice(spaces)])
print(space)
BG = pygame.transform.scale(Fuctions.load_image(space), st.ResolutionInt)

Heroes = pygame.sprite.Group()
for i in range(10):
    Hero = MM.FloatingHeroes(Heroes)
    Heroes.add(Hero)

Buttons = pygame.sprite.Group()
button = MM.Button(screen, 'Play', Buttons, 350, 500)
button1 = MM.Button(screen, 'Settings', Buttons, 350, 600)
button2 = MM.Button(screen, 'Quit', Buttons, 350, 700)

all_sprites = pygame.sprite.Group()

Logo = pygame.sprite.Sprite()
Logo.image = pygame.transform.scale(
    Fuctions.load_image('Logo/logo_for_menu.png'), (850, 450))
Logo.rect = Logo.image.get_rect()
Logo.rect.x = 300
Logo.rect.y = 100

all_sprites.add(Logo)

# -----------------------------GAME MUSIC----------------------------- #

All_menu_music = [i for i in os.listdir('static/audio/main menu')]
print(All_Gameplay_Music)
music = choice(All_Gameplay_Music)
print(music)
sound = pygame.mixer.music.load('/'.join(['static/audio/main menu', music]))
pygame.mixer.music.play()
pygame.mixer.music.set_volume(st.Volume)

# ----------------------------GAME WORKING---------------------------- #

running = True
fire = 0
while running:

    screen.blit(BG, (0, 0))
    Heroes.draw(screen)
    Heroes.update()
    Buttons.draw(screen)
    Buttons.update()
    all_sprites.draw(screen)
    all_sprites.update()
    pressed_key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            mouse.DrawArrow(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            fire = 1
            print('ЛКМ')
        if event.type == pygame.MOUSEBUTTONUP:
            fire = 0

# -----------------------SETTINGS-------------------------- #

    if pressed_key[pygame.K_z]:
        st.Change_Volume(0.3)
    elif pressed_key[pygame.K_x]:
        st.Change_Volume(0.7)
    elif pressed_key[pygame.K_c]:
        size = st.Change_Resolution('HD+')
        screen = pygame.display.set_mode(size)
        BG = pygame.transform.scale(
            Fuctions.load_image(space), size)
    elif pressed_key[pygame.K_v]:
        size = st.Change_Resolution('HD')
        screen = pygame.display.set_mode(size)
        BG = pygame.transform.scale(
            Fuctions.load_image(space), size)
    elif pressed_key[pygame.K_b]:  # BACK TO DEFAULT SETTINGS
        st.Change_Volume()
        size = st.Change_Resolution()
        screen = pygame.display.set_mode(size)
        BG = pygame.transform.scale(
            Fuctions.load_image(space), size)

    if pygame.mouse.get_focused():
        if fire:
            mSprite = mouse.mouse_spritesGet2()
            mSprite.draw(screen)
        else:
            mSprite = mouse.mouse_spritesGet1()
            mSprite.draw(screen)

    pygame.display.flip()

    clock.tick(st.FPS)

pygame.quit()
