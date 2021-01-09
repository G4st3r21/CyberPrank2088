import pygame
from random import choice
from Fuctions import load_image


Experience = pygame.sprite.Group()
Coins = pygame.sprite.Group()
Bullets_group = pygame.sprite.Group()
Guns = pygame.sprite.Group()


class XP(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(Experience)
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        self.pos = (x, y)

        self.image = load_image('details/XP.png')
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = self.pos[0], self.pos[1]

        self.xp = choice(range(10, 30))
        self.i = 0
        self.speedx, self.speedy = choice([-4, 4]), choice([-4, 4])
        Experience.add(self)

    def update(self):
        if self.i in range(10):
            self.rect.centerx += self.speedx
            self.rect.centery += self.speedy
        elif self.i == 11:
            self.rect.centerx = choice(
                range(self.pos[0] - 50, self.pos[0] + 50))
            self.rect.centery = choice(
                range(self.pos[1] - 50, self.pos[1] + 50))
        self.i += 1

    def kill(self):
        self.rect.centerx, self.rect.centery = 0, 0


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(Coins)
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        self.pos = (x, y)

        self.image = load_image('details/coin.png')
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = self.pos[0], self.pos[1]

        self.i = 0
        self.speedx, self.speedy = choice([-4, 4]), choice([-4, 4])
        Coins.add(self)

    def update(self):
        if self.i in range(10):
            self.rect.centerx += self.speedx
            self.rect.centery += self.speedy
        elif self.i == 11:
            self.rect.centerx = choice(
                range(self.pos[0] - 50, self.pos[0] + 50))
            self.rect.centery = choice(
                range(self.pos[1] - 50, self.pos[1] + 50))
        self.i += 1

    def kill(self):
        self.rect.centerx, self.rect.centery = -1000, -1000


class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(Bullets_group)
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        self.pos = (x, y)

        self.image = load_image('details/bullets.png')
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = self.pos[0], self.pos[1]

        self.i = 0
        self.speedx, self.speedy = choice([-4, 4]), choice([-4, 4])
        Bullets_group.add(self)

    def update(self):
        if self.i in range(10):
            self.rect.centerx += self.speedx
            self.rect.centery += self.speedy
        elif self.i == 11:
            self.rect.centerx = choice(
                range(self.pos[0] - 50, self.pos[0] + 50))
            self.rect.centery = choice(
                range(self.pos[1] - 50, self.pos[1] + 50))
        self.i += 1

    def kill(self):
        self.rect.centerx, self.rect.centery = -1000, -1000


class Floating_weapons(pygame.sprite.Sprite):
    def __init__(self, GunType, x, y):
        super().__init__(Guns)
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        self.GunType = GunType

        if self.GunType == 'AR':
            self.image = load_image('details/AR.png')
        elif self.GunType == 'shootgun':
            self.image = load_image('details/Shootgun.png')

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        Guns.add(self)

    def kill(self):
        self.rect.centerx, self.rect.centery = -1000, -1000
