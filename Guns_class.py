import pygame
import math
from AnimatedSprite_class import AnimatedSprite
from Fuctions import load_image
import Settings as st


bullets = pygame.sprite.Group()


class Mouse(pygame.sprite.Sprite):
    def __init__(self, ArrowType, ArrowType2, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.mouse_sprite1 = pygame.sprite.Group()
        self.mouse_sprite2 = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite()
        self.sprite2 = pygame.sprite.Sprite()
        self.sprite2.image = load_image(ArrowType2)
        self.sprite.image = load_image(ArrowType)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite2.rect = self.sprite2.image.get_rect()
        self.mouse_sprite1.add(self.sprite)
        self.mouse_sprite2.add(self.sprite2)
        pygame.mouse.set_visible(False)
        self.sprite.rect.x = screen.get_size()[0] // 2
        self.sprite.rect.y = screen.get_size()[1] // 2
        self.sprite2.rect.x = screen.get_size()[0] // 2
        self.sprite2.rect.y = screen.get_size()[1] // 2

    def DrawArrow(self, event):
        pos = event
        if pos[0] <= st.ResolutionInt[0] - 64 and \
                pos[1] <= st.ResolutionInt[1] - 64:
            self.sprite.rect.x = pos[0]
            self.sprite.rect.y = pos[1]
            self.sprite2.rect.x = pos[0]
            self.sprite2.rect.y = pos[1]

    def mouse_spritesGet1(self):
        return self.mouse_sprite1

    def mouse_spritesGet2(self):
        return self.mouse_sprite2


class Pistol(Mouse):
    def __init__(self, screen, player, mouse):
        self.player = player
        self.mouse = mouse

        self.left_sprites = pygame.sprite.Group()
        self.right_sprites = pygame.sprite.Group()

        self.screen = screen
        self.pos = (248, 244)

        self.left_sprites = pygame.sprite.Group()
        self.right_sprites = pygame.sprite.Group()

        self.Pistol_R = AnimatedSprite(pygame.transform.scale(load_image(
            'guns/pistol/Default_pistol_R.png'), (512, 64)), 8, 1,
            *self.pos, self.right_sprites)
        self.Pistol_L = AnimatedSprite(pygame.transform.scale(load_image(
            'guns/pistol/Default_pistol_L.png'), (512, 64)), 8, 1,
            *self.pos, self.left_sprites, 1)

        self.Ammo = -1  # '-1' means Infinity ammo

        self.Damage = 5

    def setPos(self):
        self.LastPose = self.player.LastPose
        self.pos = (self.player.Man_Go_R.rect.x, self.player.Man_Go_R.rect.y)
        self.Pistol_R.rect.x = self.pos[0] + 48
        self.Pistol_R.rect.y = self.pos[1] + 44
        self.Pistol_L.rect.x = self.pos[0] + 17
        self.Pistol_L.rect.y = self.pos[1] + 44
        self.Pistol_rect = (self.Pistol_L.rect.centerx,
                            self.Pistol_L.rect.centery)

    def drawPistol(self):
        self.setPos()
        self.Pistol_R.cur_frame = 0
        self.Pistol_L.cur_frame = -1
        if self.LastPose == 'R':
            self.right_sprites.draw(self.screen)
        else:
            self.left_sprites.draw(self.screen)

    def FireAnimOn(self):
        self.setPos()
        if self.LastPose == 'R':
            self.right_sprites.draw(self.screen)
            self.right_sprites.update()
            if self.Pistol_R.cur_frame == 23:
                goal = (self.mouse.sprite.rect.x, self.mouse.sprite.rect.y)
                bullet = Bullet(self.Pistol_rect, goal, 'R', bullets)
                bullets.add(bullet)
        else:
            self.left_sprites.draw(self.screen)
            self.left_sprites.update()
            if self.Pistol_L.cur_frame == 23:
                goal = (self.mouse.sprite.rect.x, self.mouse.sprite.rect.y)
                bullet = Bullet(self.Pistol_rect, goal, 'L', bullets)
                bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, goal, LastPose, group):
        super().__init__(group)
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(
            load_image('For Fire/Red_bullet.png'), (32, 32))

        self.rect = self.image.get_rect()

        self.LastPose = LastPose
        if self.LastPose == 'R':
            self.rect.centerx = pos[0] + 50
            self.rect.centery = pos[1] - 50
        else:
            self.rect.centerx = pos[0] - 50
            self.rect.centery = pos[1] - 50

        self.pistol_pos = pos
        self.goal = goal

        self.speed = 15
        if self.LastPose == 'L' and self.speed > 0 or \
                self.LastPose == 'R' and self.speed < 0:
            self.speed = -1 * self.speed
        self.Count_Angle()
        if not self.angle or self.angle > 1 or self.angle < -1:
            self.kill()
            self.rect.centerx, self.rect.centery = 0, 0

    def Count_Angle(self):
        s1 = self.goal[0] - self.rect.centerx
        s2 = self.goal[1] - self.rect.centery
        if s1 == 0 or s2 == 0:
            self.angle = 0
        else:
            self.angle = math.atan(s2/s1)

            self.gox1 = math.cos(self.angle)
            self.goy1 = math.sin(self.angle)
            self.gox = self.gox1
            self.goy = self.goy1

    def update(self):
        if self.rect.centerx == 0 and self.rect.centery == 0:
            return None
        if int(self.goy1) > 1 or int(self.goy1) < -1:
            self.rect.centery += self.goy1 * self.speed
            self.goy1 -= int(self.goy1)
        else:
            self.goy1 += self.goy
        if int(self.gox1) >= 1 or int(self.gox1) <= -1:
            self.rect.centerx += self.gox1 * self.speed
            self.gox1 -= int(self.gox1)
        else:
            self.gox1 += self.gox
        if self.rect.centerx < 0 or \
                self.rect.centerx > st.ResolutionInt[0] or \
                self.rect.centery < 0 or \
                self.rect.centery > st.ResolutionInt[1]:
            self.kill()
