import pygame
import os
import Fuctions
from random import choice
from moviepy.editor import VideoFileClip
import HUD
import Heroes_class as hc
import Guns_class as gc
import Settings as st


class Main():
    def __init__(self, screen, clock, size):
        self.screen = screen
        self.clock = clock
        self.size = size

        self.player = hc.Players_Hero('Синий', self.screen, 1, 0, 0)

        self.zombie1 = hc.Zombie(
            self.screen, (choice(range(300, 900)), choice(range(300, 900))))

        self.mouse = gc.Mouse('Arrows/Arrow1.png',
                              'Arrows/Arrow1.1.png', self.screen)
        self.gun = gc.Gun(self.screen, self.player, self.mouse, 'AR')

        self.hud_sprites = pygame.sprite.Group()
        self.hud = HUD.HUD(self.screen, self.hud_sprites,
                           100, self.player.GunType)

    def IntroInit(self):
        clip = VideoFileClip('static/video/Intro.mp4',
                             target_resolution=self.size[::-1])
        clip.set_fps(st.FPS)
        clip.preview()

    def MusicInit(self):
        self.All_Gameplay_Music = [
            i for i in os.listdir('static/audio/fighting')]
        music = choice(self.All_Gameplay_Music)
        self.sound = pygame.mixer.music.load(
            '/'.join(['static/audio/fighting', music]))
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(st.Volume)

    def Mouse(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEMOTION:
                self.mouse.DrawArrow(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.fire = 1
                print('ЛКМ')
            elif event.type == pygame.MOUSEBUTTONUP:
                self.fire = 0
                self.Firing = 0

    def Dev_mode(self):
        if (
            self.pressed_key[pygame.K_LSHIFT] and
            self.pressed_key[pygame.K_p] and
            self.DEV_MODE
        ):
            self.DEV_MODE = 0
            print('DEV MODE OFF')
        elif self.pressed_key[pygame.K_LSHIFT] and \
                self.pressed_key[pygame.K_p] and not self.DEV_MODE:
            self.DEV_MODE = 1
            print('DEV MODE ON')

        if self.DEV_MODE:
            Fuctions.Dev_mode(self.screen, self.player,
                              self.gun, self.zombie1, st.FPS)

    def Player_moving(self):
        self.player.Cycle_moving(self.size)
        if self.pressed_key[pygame.K_w] and self.pressed_key[pygame.K_a]:
            self.player.Move_UL()
        elif self.pressed_key[pygame.K_w] and self.pressed_key[pygame.K_d]:
            self.player.Move_UR()
        elif self.pressed_key[pygame.K_s] and self.pressed_key[pygame.K_a]:
            self.player.Move_DL()
        elif self.pressed_key[pygame.K_s] and self.pressed_key[pygame.K_d]:
            self.player.Move_DR()
        elif self.pressed_key[pygame.K_w]:
            self.player.Move_Up()
        elif self.pressed_key[pygame.K_s]:
            self.player.Move_Down()
        elif self.pressed_key[pygame.K_a]:
            self.player.Move_Left()
        elif self.pressed_key[pygame.K_d]:
            self.player.Move_Right()
        elif not (self.pressed_key[pygame.K_w] or
                  self.pressed_key[pygame.K_s] or
                  self.pressed_key[pygame.K_a] or
                  self.pressed_key[pygame.K_d]
                  ):
            self.player.Stand()

    def Guns(self):
        if self.pressed_key[pygame.K_1]:
            self.player.Change_gun('pistol', self.gun)
            self.hud.Pistol_hud.kill()
            self.hud.Hud_Gun()
        elif self.pressed_key[pygame.K_2]:
            self.player.Change_gun('AR', self.gun)
            self.hud.Pistol_hud.kill()
            self.hud.Hud_Gun()
        elif self.pressed_key[pygame.K_3]:
            self.player.Change_gun('shootgun', self.gun)
            self.hud.Pistol_hud.kill()
            self.hud.Hud_Gun()

    def ZombieTest(self):
        self.player.Damage(self.zombie1)
        self.zombie1.find_Hero(self.player, self.gun)
        self.hud.Zombies_HeatPoints(self.zombie1)

    def ColorTest(self):
        if self.pressed_key[pygame.K_4]:
            self.Color = 'Black'
        elif self.pressed_key[pygame.K_5]:
            self.Color = 'White'
        elif self.pressed_key[pygame.K_6]:
            self.Color = 'Blue'
        elif self.pressed_key[pygame.K_7]:
            self.Color = 'Red'
        elif self.pressed_key[pygame.K_8]:
            self.Color = 'Green'

    def SettingTest(self):
        if self.pressed_key[pygame.K_z]:
            st.Change_Volume(0.3)
        elif self.pressed_key[pygame.K_x]:
            st.Change_Volume(0.7)
        elif self.pressed_key[pygame.K_c]:
            size = st.Change_Resolution('HD+')
            self.screen = pygame.display.set_mode(size)
        elif self.pressed_key[pygame.K_v]:
            size = st.Change_Resolution('HD')
            self.screen = pygame.display.set_mode(size)
        elif self.pressed_key[pygame.K_b]:  # BACK TO DEFAULT SETTINGS
            st.Change_Volume()
            size = st.Change_Resolution()
            self.screen = pygame.display.set_mode(size)

    def HUD(self):
        self.hud_sprites.draw(self.screen)
        self.hud.Hud_HeatPoints()
        self.hud.Gun_Ammo()
        self.hud.update(self.player.HeatPoints,
                        self.player.GunType, self.gun.Ammo)

    def Fire(self):
        if pygame.mouse.get_focused():
            if self.fire:
                self.Firing = self.gun.FireAnimOn()
                mSprite = self.mouse.mouse_spritesGet2()
                mSprite.draw(self.screen)
            else:
                self.gun.drawPistol()
                mSprite = self.mouse.mouse_spritesGet1()
                mSprite.draw(self.screen)

    def Game_cycle(self):
        self.running = True
        self.fire = 0
        self.Firing = 0
        self.DEV_MODE = 1
        self.Color = 'White'
        while self.running:

            self.screen.fill(pygame.Color(self.Color))
            self.pressed_key = pygame.key.get_pressed()

            gc.bullets.draw(self.screen)
            gc.bullets.update()

            self.Mouse()

            self.Player_moving()

            self.Guns()

            self.ZombieTest()

            self.ColorTest()

            self.SettingTest()

            self.HUD()

            self.Fire()

            Fuctions.mouse_regarding_Hero(self.mouse, self.player)
            pygame.display.flip()

            self.clock.tick(st.FPS)
