import pygame
import Settings as st
import Main_menu_classes as MMC
import main_class as MC


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

Game_play = MC.Main(screen, clock, size, Playing)


Game_play.MusicInit()
Game_play.Game_cycle()
