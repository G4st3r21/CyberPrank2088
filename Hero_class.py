import pygame
from animated_sprite import AnimatedSprite
from Fuctions import load_image


class Players_Hero():
    def __init__(self, PlayersColor, screen):
        self.left_sprites = pygame.sprite.Group()
        self.right_sprites = pygame.sprite.Group()
        self.stand_sprites_R = pygame.sprite.Group()
        self.stand_sprites_L = pygame.sprite.Group()

        self.screen = screen

        Man_start_pos = (200, 200)
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
        self.All_sprites = [self.Man_stand_R,
                            self.Man_stand_L, self.Man_Go_R, self.Man_Go_L]

        self.LastPose = 'R'

    def Stand(self):
        if self.LastPose == "L":
            self.stand_sprites_L.draw(self.screen)
            self.stand_sprites_L.update()
        else:
            self.stand_sprites_R.draw(self.screen)
            self.stand_sprites_R.update()

    def Move_Right(self):
        for i in self.All_sprites:
            i.rect.x += 4
        self.right_sprites.draw(self.screen)
        self.right_sprites.update()
        self.LastPose = 'R'

    def Move_Left(self):
        for i in self.All_sprites:
            i.rect.x -= 4
        self.left_sprites.draw(self.screen)
        self.left_sprites.update()
        self.LastPose = 'L'

    def Move_Up(self):
        for i in self.All_sprites:
            i.rect.y -= 5
        if self.LastPose == "L":
            self.left_sprites.draw(self.screen)
            self.left_sprites.update()
        else:
            self.right_sprites.draw(self.screen)
            self.right_sprites.update()

    def Move_Down(self):
        for i in self.All_sprites:
            i.rect.y += 5
        if self.LastPose == "L":
            self.left_sprites.draw(self.screen)
            self.left_sprites.update()
        else:
            self.right_sprites.draw(self.screen)
            self.right_sprites.update()

    def Move_UL(self):
        for i in self.All_sprites:
            i.rect.y -= 3
            i.rect.x -= 3
        self.left_sprites.draw(self.screen)
        self.left_sprites.update()

    def Move_UR(self):
        for i in self.All_sprites:
            i.rect.y -= 3
            i.rect.x += 3
        self.right_sprites.draw(self.screen)
        self.right_sprites.update()

    def Move_DL(self):
        for i in self.All_sprites:
            i.rect.y += 3
            i.rect.x -= 3
        self.left_sprites.draw(self.screen)
        self.left_sprites.update()

    def Move_DR(self):
        for i in self.All_sprites:
            i.rect.y += 3
            i.rect.x += 3
        self.right_sprites.draw(self.screen)
        self.right_sprites.update()
