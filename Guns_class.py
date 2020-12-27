import pygame
import math
from AnimatedSprite_class import AnimatedSprite
from Fuctions import load_image
import Settings as st


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
    def __init__(self, screen):
        self.left_sprites = pygame.sprite.Group()
        self.right_sprites = pygame.sprite.Group()

        self.screen = screen
        self.pos = (248, 244)
        self.pos2 = (248, 244)

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

    def setPos(self, player):
        self.LastPose = player.LastPose
        self.pos = (player.Man_Go_R.rect.x, player.Man_Go_R.rect.y)
        self.Pistol_R.rect.x = self.pos[0] + 48
        self.Pistol_R.rect.y = self.pos[1] + 44
        self.Pistol_L.rect.x = self.pos[0] + 17
        self.Pistol_L.rect.y = self.pos[1] + 44

    def drawPistol(self, player):
        self.setPos(player)
        self.Pistol_R.cur_frame = 0
        self.Pistol_L.cur_frame = -1
        if self.LastPose == 'R':
            self.right_sprites.draw(self.screen)
        else:
            self.left_sprites.draw(self.screen)

    def Fire(self, player, lastcoords):
        self.setPos(player)
        if self.LastPose == 'R':
            self.right_sprites.draw(self.screen)
            self.right_sprites.update()
            if self.Pistol_R.cur_frame == 23:
                return 1
            else:
                return 0
        else:
            self.left_sprites.draw(self.screen)
            self.left_sprites.update()


class Bullet(Pistol):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.Bullets_R = pygame.sprite.Group()

        self.Bullet_R = AnimatedSprite(pygame.transform.scale(load_image(
            'For Fire/Red_bullet.png'), (16, 16)), 1, 1,
            x, y, self.Bullets_R)

        self.def_pos = (x, y)
        self.screen = screen
        self.speed = 15

    def Count_Angel(self, pistol, coords):
        self.def_pos = (pistol.Pistol_R.rect.centerx,
                        pistol.Pistol_R.rect.centery)
        self.Bullet_R.rect.centerx = pistol.Pistol_R.rect.centerx
        self.Bullet_R.rect.centery = pistol.Pistol_R.rect.centery
        s1 = coords[0] - self.Bullet_R.rect.centerx
        s2 = coords[1] - self.Bullet_R.rect.centery
        if s1 == 0 or s2 == 0:
            return 0
        angel = math.atan(s2/s1)

        self.gox1 = math.cos(angel)
        self.goy1 = math.sin(angel)
        self.gox = self.gox1
        self.goy = self.goy1
        return 1

    def DrawBullet(self):
        if int(self.goy1) > 1 or int(self.goy1) < -1:
            self.Bullet_R.rect.centery += self.goy1 * self.speed
            self.goy1 -= int(self.goy1)
        else:
            self.goy1 += self.goy
        if int(self.gox1) >= 1 or int(self.gox1) <= -1:
            self.Bullet_R.rect.centerx += self.gox1 * self.speed
            self.gox1 -= int(self.gox1)
        else:
            self.gox1 += self.gox
        self.Bullets_R.draw(self.screen)
        self.Bullets_R.update()
        if self.Bullet_R.rect.centerx < 0 or \
                self.Bullet_R.rect.centerx > st.ResolutionInt[0] or \
                self.Bullet_R.rect.centery < 0 or \
                self.Bullet_R.rect.centery > st.ResolutionInt[1]:
            self.Bullet_R.rect.centerx = self.def_pos[0]
            self.Bullet_R.rect.centery = self.def_pos[1]
