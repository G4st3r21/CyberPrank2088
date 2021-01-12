import pygame
import Fuctions


class HUD():
    def __init__(self, screen, hudSpriteGroup, HeatPoints,
                 GunType='pistol', Ammo=0):
        self.screen = screen
        self.Group = hudSpriteGroup
        self.HP = HeatPoints
        self.GunType = GunType
        self.Ammo = Ammo
        self.Hud_Head()
        self.Coins()
        self.Hud_Gun()

    def update(self, HeatPoints, GunType, Ammo=0):
        self.HP = HeatPoints
        if self.HP <= 0:
            self.HP = 0
        self.GunType = GunType
        self.Ammo = Ammo

    def Hud_Head(self):
        self.Head = pygame.sprite.Sprite()
        self.Head.image = pygame.transform.scale(
            Fuctions.load_image("Hud/Hero's Head.png"), (128, 128))

        self.Head.rect = self.Head.image.get_rect()
        self.Head.rect.x = 210
        self.Head.rect.y = 125
        self.Group.add(self.Head)

    def Coins(self):
        self.coin = pygame.sprite.Sprite()
        self.coin.image = pygame.transform.scale(
            Fuctions.load_image('details/coin.png'), (38, 42))
        self.coin.rect = self.coin.image.get_rect()
        self.coin.rect.x = 345
        self.coin.rect.y = 185
        self.Group.add(self.coin)

    def Coins_cnt(self, player):
        font = pygame.font.Font('static/fonts/19888.ttf', 20)
        cnt = font.render(str(player.Coins), True, (0, 0, 0))
        self.screen.blit(cnt, (380, 227))

    def Hud_HeatPoints(self):
        pygame.draw.rect(self.screen, pygame.Color(
            'Red'), (340, 125, self.HP * 4, 50))
        pygame.draw.rect(self.screen, pygame.Color(
            'Black'), (340, 125, 400, 50), 3)
        font = pygame.font.Font('static/fonts/19888.ttf', 40)
        HP = font.render(f'{self.HP}/100', True, (0, 0, 0))
        self.screen.blit(HP, (460, 133))

    def Hud_Gun(self):
        if self.GunType == 'pistol':
            self.Pistol_hud = pygame.sprite.Sprite()
            self.Pistol_hud.image = pygame.transform.scale(
                Fuctions.load_image("Hud/Pistol.png"), (64, 64))
        elif self.GunType == 'AR':
            self.Pistol_hud = pygame.sprite.Sprite()
            self.Pistol_hud.image = pygame.transform.scale(
                Fuctions.load_image("Hud/AR.png"), (64, 64))
        elif self.GunType == 'shootgun':
            self.Pistol_hud = pygame.sprite.Sprite()
            self.Pistol_hud.image = pygame.transform.scale(
                Fuctions.load_image("Hud/Shootgun.png"), (64, 64))

        self.Pistol_hud.rect = self.Pistol_hud.image.get_rect()
        self.Pistol_hud.rect.x = 210
        self.Pistol_hud.rect.y = 260

        self.Ammo_hud = pygame.sprite.Sprite()
        self.Ammo_hud.image = pygame.transform.scale(
            Fuctions.load_image("Hud/Circle_1px.png"), (32, 32))

        self.Ammo_hud.rect = self.Ammo_hud.image.get_rect()
        self.Ammo_hud.rect.x = 250
        self.Ammo_hud.rect.y = 305

        self.Group.add(self.Pistol_hud)
        self.Group.add(self.Ammo_hud)

    def Gun_Ammo(self):
        font = pygame.font.Font('static/fonts/19888.ttf', 20)
        if self.Ammo < 0:
            Ammo = pygame.transform.rotate(
                font.render(str(8), True, (0, 0, 0)), 90)
        else:
            Ammo = font.render(str(self.Ammo), True, (0, 0, 0))
        self.screen.blit(Ammo, (255, 312))

    def Zombies_HeatPoints(self, zombie):
        font = pygame.font.Font('static/fonts/19888.ttf', 15)
        zHP = zombie.HeatPoints
        if zombie.Strench <= 60:
            color = (255, 0, 0)
        elif zombie.Strench > 60 and zombie.Strench < 80:
            color = (0, 0, 255)
        elif zombie.Strench <= 100:
            color = (139, 0, 255)
        pos = (zombie.Man_stand_R.rect.x, zombie.Man_stand_R.rect.y)
        pygame.draw.rect(self.screen, color,
                         (pos[0] + 23, pos[1] - 15, zHP * zombie.zS, 8))
        pygame.draw.rect(self.screen, pygame.Color(
            'Black'), (pos[0] + 23, pos[1] - 15, 80, 8), 2)
        HP = font.render(f'{zombie.Strench} lvl.', True, (0, 0, 0))
        self.screen.blit(HP, (pos[0] + 38, pos[1] - 30))
