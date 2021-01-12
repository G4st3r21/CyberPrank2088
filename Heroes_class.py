import pygame
from AnimatedSprite_class import AnimatedSprite
from Fuctions import load_image
from Guns_class import bullets
from random import choice
import Detail_class as dc
import Settings as st


class Players_Hero():
    def __init__(self, PlayersColor, screen, guns):
        self.screen = screen
        self.HeatPoints = 100
        self.Coins = 0

        self.LastPose = 'R'
        self.RoomIn = 0

        self.guns = guns
        if self.guns[1].InHands:
            self.cur_sprites = 0
            self.GunType = 'AR'
        elif self.guns[0].InHands:
            self.cur_sprites = 1
            self.GunType = 'pistol'
        elif self.guns[2].InHands:
            self.cur_sprites = 0
            self.GunType = 'shootgun'
        self.SpritesINIT(PlayersColor)

        self.IsAlive = True

    def SpritesINIT(self, PlayersColor):
        Man_start_pos = (500, 500)

        # ----------------ASSAULT RIFLE------------------ #
        self.left_sprites = pygame.sprite.Group()
        self.right_sprites = pygame.sprite.Group()
        self.left_back_sprites = pygame.sprite.Group()
        self.right_back_sprites = pygame.sprite.Group()
        self.stand_sprites_R = pygame.sprite.Group()
        self.stand_sprites_L = pygame.sprite.Group()

        self.Man_stand_R = AnimatedSprite(load_image(
            f'Космонавт/{PlayersColor}/Космонавт_stand_R_ALL.png'), 8, 1,
            *Man_start_pos, self.stand_sprites_R)
        self.Man_stand_L = AnimatedSprite(load_image(
            f'Космонавт/{PlayersColor}/Космонавт_stand_L_ALL.png'), 8, 1,
            *Man_start_pos, self.stand_sprites_L, 1)
        self.Man_Go_R = AnimatedSprite(load_image(
            f'Космонавт/{PlayersColor}/Космонавт_run_R_ALL.png'), 8, 1,
            *Man_start_pos, self.right_sprites)
        self.Man_Go_L = AnimatedSprite(load_image(
            f'Космонавт/{PlayersColor}/Космонавт_run_L_ALL.png'), 8, 1,
            *Man_start_pos, self.left_sprites, 1)
        self.Man_Go_L_Back = AnimatedSprite(load_image(
            f'Космонавт/{PlayersColor}/Космонавт_run_L_ALL.png'), 8, 1,
            *Man_start_pos, self.left_back_sprites)
        self.Man_Go_R_Back = AnimatedSprite(load_image(
            f'Космонавт/{PlayersColor}/Космонавт_run_R_ALL.png'), 8, 1,
            *Man_start_pos, self.right_back_sprites, 1)

        self.default_sprites_DRAW = [
            self.stand_sprites_R, self.stand_sprites_L,
            self.right_sprites, self.left_sprites,
            self.right_back_sprites, self.left_back_sprites
        ]

        # ----------------С ПИСТОЛЕТОМ------------------ #

        self.left_sprites_P = pygame.sprite.Group()
        self.right_sprites_P = pygame.sprite.Group()
        self.left_back_sprites_P = pygame.sprite.Group()
        self.right_back_sprites_P = pygame.sprite.Group()
        self.stand_sprites_R_P = pygame.sprite.Group()
        self.stand_sprites_L_P = pygame.sprite.Group()

        path = f'Космонавт/{PlayersColor}/С_пистолетом/'
        self.Man_stand_R_P = AnimatedSprite(load_image(
            path + 'Космонавт_stand_R_ALL_P.png'), 8, 1,
            *Man_start_pos, self.stand_sprites_R_P)
        self.Man_stand_L_P = AnimatedSprite(load_image(
            path + 'Космонавт_stand_L_ALL_P.png'), 8, 1,
            *Man_start_pos, self.stand_sprites_L_P, 1)
        self.Man_Go_R_P = AnimatedSprite(load_image(
            path + 'Космонавт_run_R_ALL_P.png'), 8, 1,
            *Man_start_pos, self.right_sprites_P)
        self.Man_Go_L_P = AnimatedSprite(load_image(
            path + 'Космонавт_run_L_ALL_P.png'), 8, 1,
            *Man_start_pos, self.left_sprites_P, 1)
        self.Man_Go_L_Back_P = AnimatedSprite(load_image(
            path + 'Космонавт_run_L_ALL_P.png'), 8, 1,
            *Man_start_pos, self.left_back_sprites_P)
        self.Man_Go_R_Back_P = AnimatedSprite(load_image(
            path + 'Космонавт_run_R_ALL_P.png'), 8, 1,
            *Man_start_pos, self.right_back_sprites_P, 1)

        self.pistol_sprites_DRAW = [
            self.stand_sprites_R_P, self.stand_sprites_L_P,
            self.right_sprites_P, self.left_sprites_P,
            self.right_back_sprites_P, self.left_back_sprites_P
        ]

        # ------------------ВСЕ СПРАЙТЫ В СПИСКАХ---------------- #

        self.ALL_sprites_RECT = [
            self.Man_stand_R_P, self.Man_stand_L_P,
            self.Man_Go_R_P, self.Man_Go_L_P,
            self.Man_Go_L_Back_P, self.Man_Go_R_Back_P,
            self.Man_stand_R, self.Man_stand_L,
            self.Man_Go_R, self.Man_Go_L,
            self.Man_Go_L_Back, self.Man_Go_R_Back
        ]

        self.ALL_sprites_DRAW = [
            self.default_sprites_DRAW,
            self.pistol_sprites_DRAW
        ]

    def Change_gun(self, GunType, gun):
        if GunType == 'pistol':
            self.guns[0].InHands = True
            self.guns[1].InHands = False
            self.guns[2].InHands = False
            gun.Change_gun('pistol')
        elif GunType == 'AR':
            self.guns[0].InHands = False
            self.guns[1].InHands = True
            self.guns[2].InHands = False
            gun.Change_gun('AR')
        elif GunType == 'shootgun':
            self.guns[0].InHands = False
            self.guns[1].InHands = False
            self.guns[2].InHands = True
            gun.Change_gun('shootgun')

        if self.guns[1].InHands:
            self.cur_sprites = 0
            self.GunType = 'AR'
        elif self.guns[0].InHands:
            self.cur_sprites = 1
            self.GunType = 'pistol'
        elif self.guns[2].InHands:
            self.cur_sprites = 0
            self.GunType = 'shootgun'

    def Stand(self):
        if not self.IsAlive:
            return 0
        if self.LastPose == "L":
            self.ALL_sprites_DRAW[self.cur_sprites][1].draw(self.screen)
            self.ALL_sprites_DRAW[self.cur_sprites][1].update()
        else:
            self.ALL_sprites_DRAW[self.cur_sprites][0].draw(self.screen)
            self.ALL_sprites_DRAW[self.cur_sprites][0].update()

    def Move_Right(self):
        if not self.IsAlive:
            return 0
        for i in self.ALL_sprites_RECT:
            i.rect.x += 4
        if self.LastPose == 'R':
            self.ALL_sprites_DRAW[self.cur_sprites][2].draw(self.screen)
            self.ALL_sprites_DRAW[self.cur_sprites][2].update()
        else:
            self.ALL_sprites_DRAW[self.cur_sprites][5].draw(self.screen)
            self.ALL_sprites_DRAW[self.cur_sprites][5].update()

    def Move_Left(self):
        if not self.IsAlive:
            return 0
        for i in self.ALL_sprites_RECT:
            i.rect.x -= 4
        if self.LastPose == 'L':
            self.ALL_sprites_DRAW[self.cur_sprites][3].draw(self.screen)
            self.ALL_sprites_DRAW[self.cur_sprites][3].update()
        else:
            self.ALL_sprites_DRAW[self.cur_sprites][4].draw(self.screen)
            self.ALL_sprites_DRAW[self.cur_sprites][4].update()

    def Move_Up(self):
        if not self.IsAlive:
            return 0
        for i in self.ALL_sprites_RECT:
            i.rect.y -= 4
        if self.LastPose == 'L':
            self.ALL_sprites_DRAW[self.cur_sprites][3].draw(self.screen)
            self.ALL_sprites_DRAW[self.cur_sprites][3].update()
        else:
            self.ALL_sprites_DRAW[self.cur_sprites][2].draw(self.screen)
            self.ALL_sprites_DRAW[self.cur_sprites][2].update()

    def Move_Down(self):
        if not self.IsAlive:
            return 0
        for i in self.ALL_sprites_RECT:
            i.rect.y += 4
        if self.LastPose == 'L':
            self.ALL_sprites_DRAW[self.cur_sprites][3].draw(self.screen)
            self.ALL_sprites_DRAW[self.cur_sprites][3].update()
        else:
            self.ALL_sprites_DRAW[self.cur_sprites][2].draw(self.screen)
            self.ALL_sprites_DRAW[self.cur_sprites][2].update()

    def Move_UL(self):
        if not self.IsAlive:
            return 0
        for i in self.ALL_sprites_RECT:
            i.rect.y -= 3
            i.rect.x -= 3
        if self.LastPose == 'L':
            self.ALL_sprites_DRAW[self.cur_sprites][3].draw(self.screen)
            self.ALL_sprites_DRAW[self.cur_sprites][3].update()
        else:
            self.ALL_sprites_DRAW[self.cur_sprites][4].draw(self.screen)
            self.ALL_sprites_DRAW[self.cur_sprites][4].update()

    def Move_UR(self):
        if not self.IsAlive:
            return 0
        for i in self.ALL_sprites_RECT:
            i.rect.y -= 3
            i.rect.x += 3
        if self.LastPose == 'R':
            self.ALL_sprites_DRAW[self.cur_sprites][2].draw(self.screen)
            self.ALL_sprites_DRAW[self.cur_sprites][2].update()
        else:
            self.ALL_sprites_DRAW[self.cur_sprites][5].draw(self.screen)
            self.ALL_sprites_DRAW[self.cur_sprites][5].update()

    def Move_DL(self):
        if not self.IsAlive:
            return 0
        for i in self.ALL_sprites_RECT:
            i.rect.y += 3
            i.rect.x -= 3
        if self.LastPose == 'L':
            self.ALL_sprites_DRAW[self.cur_sprites][3].draw(self.screen)
            self.ALL_sprites_DRAW[self.cur_sprites][3].update()
        else:
            self.ALL_sprites_DRAW[self.cur_sprites][4].draw(self.screen)
            self.ALL_sprites_DRAW[self.cur_sprites][4].update()

    def Move_DR(self):
        if not self.IsAlive:
            return 0
        for i in self.ALL_sprites_RECT:
            i.rect.y += 3
            i.rect.x += 3
        if self.LastPose == 'R':
            self.ALL_sprites_DRAW[self.cur_sprites][2].draw(self.screen)
            self.ALL_sprites_DRAW[self.cur_sprites][2].update()
        else:
            self.ALL_sprites_DRAW[self.cur_sprites][5].draw(self.screen)
            self.ALL_sprites_DRAW[self.cur_sprites][5].update()

    def Cycle_moving(self, size):
        if not self.IsAlive:
            return 0
        if self.Man_Go_L.rect.x < 0 + 200 + 358 - 128:
            for i in self.ALL_sprites_RECT:
                i.rect.x = size[0] - 200 - 358
            return [1, 0, 0, 0]
        if self.Man_Go_R.rect.x > size[0] - 358 + 128:
            for i in self.ALL_sprites_RECT:
                i.rect.x = 0 + 200 + 358
            return [0, 1, 0, 0]
        if self.Man_Go_R.rect.y < 0 - 128:
            for i in self.ALL_sprites_RECT:
                i.rect.y = size[1]
            return [0, 0, 1, 0]
        if self.Man_Go_R.rect.y > size[1] + 128:
            for i in self.ALL_sprites_RECT:
                i.rect.y = 0
            return [0, 0, 0, 1]
        return -1

    def Damage(self, zombie):
        if zombie.Man_stand_R.rect.right > self.Man_stand_R.rect.left and \
                zombie.Man_stand_R.rect.left < self.Man_stand_R.rect.right and \
                zombie.Man_stand_R.rect.bottom > self.Man_stand_R.rect.top and \
                zombie.Man_stand_R.rect.top < self.Man_stand_R.rect.bottom:
            hit = True
        else:
            hit = False
        if hit:

            if zombie.Man_stand_R.rect.right > self.Man_stand_R.rect.left and \
                    zombie.Man_stand_R.rect.left < self.Man_stand_R.rect.left:
                self.HeatPoints -= 15
                for i in self.ALL_sprites_RECT:
                    i.rect.x += 100
            elif zombie.Man_stand_R.rect.left < self.Man_stand_R.rect.right and \
                    zombie.Man_stand_R.rect.right > self.Man_stand_R.rect.right:
                self.HeatPoints -= 15
                for i in self.ALL_sprites_RECT:
                    i.rect.x -= 100
            elif zombie.Man_stand_R.rect.bottom > self.Man_stand_R.rect.top and \
                    zombie.Man_stand_R.rect.top < self.Man_stand_R.rect.top:
                self.HeatPoints -= 15
                for i in self.ALL_sprites_RECT:
                    i.rect.y += 100
            elif zombie.Man_stand_R.rect.top < self.Man_stand_R.rect.bottom and \
                    zombie.Man_stand_R.rect.bottom > self.Man_stand_R.rect.bottom:
                self.HeatPoints -= 15
                for i in self.ALL_sprites_RECT:
                    i.rect.y -= 100
            if self.HeatPoints <= 0:
                self.IsAlive = False
                for i in self.ALL_sprites_RECT:
                    i.rect.y = -1000
                    i.rect.x = -1000

    def TakeDetail(self, group, group2, group3, group4, guns):
        takingCoin = pygame.sprite.spritecollide(
            self.Man_stand_R, group, True)
        takingXP = pygame.sprite.spritecollide(
            self.Man_stand_R, group2, True)
        takingBullets = pygame.sprite.spritecollide(
            self.Man_stand_R, group3, True)
        takingGuns = pygame.sprite.spritecollide(
            self.Man_stand_R, group4, True)
        if takingCoin:
            for i in takingCoin:
                self.Coins += 1
        elif takingXP:
            for i in takingXP:
                self.HeatPoints += i.xp
                if self.HeatPoints >= 100:
                    self.HeatPoints = 100
        elif takingBullets:
            for i in takingBullets:
                if guns[0].InHands:
                    if guns[1].Ammo < guns[2].Ammo:
                        guns[1].Ammo += 5
                    else:
                        guns[2].Ammo += 5
                elif guns[1].InHands:
                    guns[1].Ammo += 5
                elif guns[2].InHands:
                    guns[2].Ammo += 5
        elif takingGuns:
            for i in takingGuns:
                for j in guns:
                    if j.type == i.GunType:
                        j.Taken = True


class Zombie():
    def __init__(self, screen, start_pos=(500, 600)):
        self.left_sprites = pygame.sprite.Group()
        self.right_sprites = pygame.sprite.Group()
        self.stand_sprites_R = pygame.sprite.Group()
        self.stand_sprites_L = pygame.sprite.Group()

        self.screen = screen

        # Speed from 2 --> 5, HP from 20 --> 50, Visibility from 250 --> 500
        self.Difficulty = st.Difficulty
        if self.Difficulty == 1:
            self.Strench = choice(range(40, 60))
        elif self.Difficulty == 2:
            self.Strench = choice(range(60, 80))
        elif self.Difficulty == 3:
            self.Strench = choice(range(80, 101))

        self.Speed = int(0.05 * self.Strench)
        self.HeatPoints = int(0.5 * self.Strench)
        self.zS = 80 / self.HeatPoints
        self.Visibility = (6.25 * self.Strench)

        Man_start_pos = start_pos
        self.Man_stand_R = AnimatedSprite(load_image(
            'Зомби/Зомби_stand_R_ALL.png'), 8, 1,
            *Man_start_pos, self.stand_sprites_R)
        self.Man_stand_L = AnimatedSprite(load_image(
            'Зомби/Зомби_stand_L_ALL.png'), 8, 1,
            *Man_start_pos, self.stand_sprites_L, 1)
        self.Man_Go_R = AnimatedSprite(load_image(
            'Зомби/Зомби_run_R_ALL.png'), 8, 1,
            *Man_start_pos, self.right_sprites)
        self.Man_Go_L = AnimatedSprite(load_image(
            'Зомби/Зомби_run_L_ALL.png'), 8, 1,
            *Man_start_pos, self.left_sprites, 1)
        self.All_sprites = [
            self.Man_stand_R, self.Man_stand_L,
            self.Man_Go_R, self.Man_Go_L
        ]

        self.LastPose = 'R'
        self.IsAlive = True

    def Stand(self):
        if self.LastPose == "L":
            self.stand_sprites_L.draw(self.screen)
            self.stand_sprites_L.update()
        else:
            self.stand_sprites_R.draw(self.screen)
            self.stand_sprites_R.update()

    def Move_Right(self):
        for i in self.All_sprites:
            i.rect.x += self.Speed
        self.right_sprites.draw(self.screen)
        self.right_sprites.update()
        self.LastPose = 'R'

    def Move_Left(self):
        for i in self.All_sprites:
            i.rect.x -= self.Speed
        self.left_sprites.draw(self.screen)
        self.left_sprites.update()
        self.LastPose = 'L'

    def Move_Up(self):
        for i in self.All_sprites:
            i.rect.y -= self.Speed
        if self.LastPose == 'R':
            self.right_sprites.draw(self.screen)
            self.right_sprites.update()
        else:
            self.left_sprites.draw(self.screen)
            self.left_sprites.update()

    def Move_Down(self):
        for i in self.All_sprites:
            i.rect.y += self.Speed
        if self.LastPose == 'R':
            self.right_sprites.draw(self.screen)
            self.right_sprites.update()
        else:
            self.left_sprites.draw(self.screen)
            self.left_sprites.update()

    def Move_UL(self):
        for i in self.All_sprites:
            i.rect.y -= self.Speed
            i.rect.x -= self.Speed
        self.left_sprites.draw(self.screen)
        self.left_sprites.update()
        self.LastPose = 'L'

    def Move_UR(self):
        for i in self.All_sprites:
            i.rect.y -= self.Speed
            i.rect.x += self.Speed
        self.right_sprites.draw(self.screen)
        self.right_sprites.update()
        self.LastPose = 'R'

    def Move_DL(self):
        for i in self.All_sprites:
            i.rect.y += self.Speed
            i.rect.x -= self.Speed
        self.left_sprites.draw(self.screen)
        self.left_sprites.update()
        self.LastPose = 'L'

    def Move_DR(self):
        for i in self.All_sprites:
            i.rect.y += self.Speed
            i.rect.x += self.Speed
        self.right_sprites.draw(self.screen)
        self.right_sprites.update()
        self.LastPose = 'R'

    def find_Hero(self, player, gun):
        if not self.IsAlive:
            return 0

        rect_x = player.Man_stand_R.rect.x
        rect_y = player.Man_stand_R.rect.y
        if rect_x < (self.Man_stand_R.rect.x - self.Visibility) or \
                rect_x > (self.Man_stand_R.rect.x + self.Visibility) or \
                rect_y < (self.Man_stand_R.rect.y - self.Visibility) or \
                rect_y > (self.Man_stand_R.rect.y + self.Visibility):
            self.Stand()
        else:
            Zombie_rect = (self.Man_stand_R.rect.x,
                           self.Man_stand_R.rect.y)
            S = (rect_x - Zombie_rect[0], rect_y - Zombie_rect[1])
            if S[0] > 0 and S[1] > 0:
                self.Move_DR()
            elif S[0] < 0 and S[1] < 0:
                self.Move_UL()
            elif S[0] > 0 and S[1] < 0:
                self.Move_UR()
            elif S[0] < 0 and S[1] > 0:
                self.Move_DL()
            elif S == (0, 0):
                self.Stand()
            elif S[0] == 0 and S[1] > 0:
                self.Move_Down()
            elif S[0] == 0 and S[1] < 0:
                self.Move_Up()
            elif S[0] < 0 and S[1] == 0:
                self.Move_Left()
            elif S[0] > 0 and S[1] == 0:
                self.Move_Right()
        self.Damage(gun)

    def Damage(self, gun):
        Hits = pygame.sprite.spritecollide(self.Man_stand_R, bullets, True)
        if Hits:
            self.HeatPoints -= gun.Damage
        if self.HeatPoints <= 0:
            self.IsAlive = False
            counts = [choice(range(4)), choice(range(4)), choice(range(4))]

            for i in range(counts[0]):
                dc.Coin(self.Man_stand_R.rect.centerx,
                        self.Man_stand_R.rect.centery)
            for i in range(counts[1]):
                dc.XP(self.Man_stand_R.rect.centerx,
                      self.Man_stand_R.rect.centery)
            for i in range(counts[2]):
                dc.Bullets(self.Man_stand_R.rect.centerx,
                           self.Man_stand_R.rect.centery)

            for i in self.All_sprites:
                i.rect.y = -1000
                i.rect.x = -1000
