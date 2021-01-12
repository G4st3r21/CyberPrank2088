import pygame
import Settings as st
import Main_menu_classes as MMC
import main_class as MC
from Fuctions import load_image


pygame.init()
size = st.Change_Resolution()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

Game_menu = MMC.Main_menu(screen, clock)
# ----------------------Menu---------------------- #

Playing = Game_menu.Menu_cycle()
if not Playing:
    exit()

# ----------------------Game---------------------- #
FT = pygame.transform.scale(load_image(
    'Main_menu\Fast_Tutorial.png'), (1800, 980))
running = True
while running:
    screen.blit(FT, (-30, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_SPACE]:
        running = False

    pygame.display.flip()

    clock.tick(st.FPS)


Game_play = MC.Main(screen, clock, size, Playing)


Game_play.MusicInit()
Game_play.Game_cycle()
