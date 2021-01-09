import pygame
import os
import Fuctions
from random import choice
from moviepy.editor import VideoFileClip
import HUD
import Heroes_class as hc
import Guns_class as gc
import Settings as st
import Detail_class as dc


class Main():
    def __init__(self, screen, clock, size, Type):
        self.screen = screen
        self.clock = clock
        self.size = size

        self.mouse = gc.Mouse('Arrows/Arrow1.png',
                              'Arrows/Arrow1.1.png', self.screen)

        self.hud_sprites = pygame.sprite.Group()

        self.Type = Type
        self.spawnedAR = False
        self.spawnedSG = False
        self.kills = 0
        if self.Type == 'Debug':
            self.Debug_modeINIT()

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
        elif self.pressed_key[pygame.K_LSHIFT] and \
                self.pressed_key[pygame.K_p] and not self.DEV_MODE:
            self.DEV_MODE = 1
        for i in self.guns:
            if i.InHands:
                if self.DEV_MODE:
                    Fuctions.Dev_mode(self.screen, self.player,
                                      i, self.zombie1, st.FPS)

    def Player_moving(self):
        self.player.Cycle_moving(self.size)
        self.player.TakeDetail(dc.Coins, dc.Experience,
                               dc.Bullets_group, dc.Guns, self.guns)
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
            for i in self.guns:
                if i.InHands:
                    self.player.Change_gun('pistol', i)
            self.hud.Pistol_hud.kill()
            self.hud.Hud_Gun()
        elif self.pressed_key[pygame.K_2] and self.AR.Taken:
            for i in self.guns:
                if i.InHands:
                    self.player.Change_gun('AR', i)
            self.hud.Pistol_hud.kill()
            self.hud.Hud_Gun()
        elif self.pressed_key[pygame.K_3] and self.SG.Taken:
            for i in self.guns:
                if i.InHands:
                    self.player.Change_gun('shootgun', i)
            self.hud.Pistol_hud.kill()
            self.hud.Hud_Gun()

    def ZombieTest(self):
        self.player.Damage(self.zombie1)
        for i in self.guns:
            if i.InHands:
                self.zombie1.find_Hero(self.player, i)
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
        for i in self.guns:
            if i.InHands:
                self.hud.update(self.player.HeatPoints,
                                self.player.GunType, i.Ammo)
        self.hud.Coins_cnt(self.player)

    def Fire(self):
        if pygame.mouse.get_focused():
            if self.fire:
                for i in self.guns:
                    if i.InHands:
                        self.Firing = i.FireAnimOn(self.player)
                mSprite = self.mouse.mouse_spritesGet2()
                mSprite.draw(self.screen)
            else:
                for i in self.guns:
                    if i.InHands:
                        i.drawPistol(self.player)
                mSprite = self.mouse.mouse_spritesGet1()
                mSprite.draw(self.screen)

    def Debug_modeINIT(self):
        self.zombie1 = hc.Zombie(
            self.screen, (choice(range(300, 1700)), choice(range(300, 900))))

        self.pistol = gc.Gun(self.screen, self.mouse, 'pistol', -1)
        self.AR = gc.Gun(self.screen, self.mouse, 'AR', 50)
        self.SG = gc.Gun(self.screen, self.mouse, 'shootgun', 25)

        self.pistol.InHands = True

        self.guns = [self.pistol, self.AR, self.SG]

        self.player = hc.Players_Hero('Синий', self.screen, self.guns)

        self.hud = HUD.HUD(self.screen, self.hud_sprites,
                           100, self.player.GunType)

        self.pistol.Taken = True

    def Debug_mode(self):
        self.Guns()
        self.ZombieTest()
        if self.zombie1.HeatPoints <= 0:
            self.zombie1 = hc.Zombie(self.screen, (choice(
                range(300, 1700)), choice(range(300, 900))))
            self.kills += 1
        if self.kills >= 1 and not self.spawnedAR:
            dc.Floating_weapons('AR', choice(
                range(300, 1700)), choice(range(300, 900)))
            self.spawnedAR = True
        if self.kills >= 5 and not self.spawnedSG:
            dc.Floating_weapons('shootgun', choice(
                range(300, 1700)), choice(range(300, 900)))
            self.spawnedSG = True
        self.ColorTest()
        self.SettingTest()
        self.HUD()
        self.Dev_mode()

    def Game_cycle(self):
        self.pressed_key = pygame.key.get_pressed()
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
            dc.Experience.draw(self.screen)
            dc.Experience.update()
            dc.Coins.draw(self.screen)
            dc.Coins.update()
            dc.Bullets_group.draw(self.screen)
            dc.Bullets_group.update()
            dc.Guns.draw(self.screen)
            dc.Guns.update()

            self.Mouse()

            self.Player_moving()

            if self.Type == 'Debug':
                self.Debug_mode()

            self.Fire()

            Fuctions.mouse_regarding_Hero(self.mouse, self.player)
            pygame.display.flip()

            self.clock.tick(st.FPS)
