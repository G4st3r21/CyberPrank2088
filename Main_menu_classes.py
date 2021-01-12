import pygame
import os
import Settings as st
from random import choice
from Fuctions import load_image
from Guns_class import Mouse


class Main_menu():
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.mouse = Mouse('Arrows/Arrow1.png', 'Arrows/Arrow1.1.png', screen)
        spaces = [i for i in os.listdir('sprites/Main_menu/spaces')]
        space = '/'.join(['Main_menu/spaces', choice(spaces)])
        self.BG = pygame.transform.scale(load_image(space), st.ResolutionInt)
        self.all_sprites = pygame.sprite.Group()

        self.HerosInit()
        self.LogoInit()
        self.MusicInit()

    def HerosInit(self):
        self.Heroes = pygame.sprite.Group()
        for i in range(20):
            Hero = FloatingHeroes(self.Heroes)
            self.Heroes.add(Hero)

    def ButtonsInit(self, dokill=False):
        if dokill:
            self.button.kill()
            self.button1.kill()
            self.button2.kill()
        else:
            self.Buttons = pygame.sprite.Group()
            self.button = Button(self.screen, 'Play',
                                 self.Buttons, 350, 500)
            self.button1 = Button(self.screen, 'Settings',
                                  self.Buttons, 350, 600)
            self.button2 = Button(self.screen, 'Quit',
                                  self.Buttons, 350, 700)

    def LogoInit(self):
        Logo = pygame.sprite.Sprite()

        Logo.image = pygame.transform.scale(
            load_image('Logo/logo_for_menu.png'), (850, 450))
        Logo.rect = Logo.image.get_rect()
        Logo.rect.x = 300
        Logo.rect.y = 100

        self.all_sprites.add(Logo)

    def MusicInit(self):
        All_menu_music = [i for i in os.listdir('static/audio/main menu')]
        music = choice(All_menu_music)
        pygame.mixer.music.load(
            '/'.join(['static/audio/main menu', music]))
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(st.Volume)

    def Settings(self):
        self.Settingcirlce = pygame.sprite.Group()
        self.Setting_button = Button(self.screen, 'Settings', self.Buttons,
                                     275, 200, (1400, 700), True)
        self.Settingsliders = pygame.sprite.Group()
        self.volume = Slider(self.screen, 650, 350, self.Settingsliders)
        self.difficulty = Slider(self.screen, 650, 500, self.Settingsliders)

    def Play_Game(self):
        self.Game_type = Button(self.screen, 'Выбор режима', self.Buttons,
                                275, 200, (1400, 700), True)
        self.Play_buttons = pygame.sprite.Group()
        self.game_1 = Button(self.screen, 'НЕДОСТУПНО',
                             self.Play_buttons, 500, 500, (320, 64))
        self.game_2 = Button(self.screen, 'ОБЫЧНЫЙ',
                             self.Play_buttons, 1100, 500, (320, 64))

    def Menu_cycle(self):
        running = True
        fire = 0
        Setting = False
        self.Setting = False
        PlayGame = False
        self.PlayGame = False
        Logo = True
        self.ButtonsInit()
        while running:

            self.screen.blit(self.BG, (0, 0))
            self.Heroes.draw(self.screen)
            self.Heroes.update()
            self.Buttons.draw(self.screen)
            self.Buttons.update()
            if Logo:
                self.all_sprites.draw(self.screen)
                self.all_sprites.update()

            self.pressed_key = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEMOTION:
                    self.mouse.DrawArrow(event.pos)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    fire = 1

                    PlayGame = self.button.update(True)
                    if PlayGame:
                        Logo = False
                        self.ButtonsInit(True)
                        self.Play_Game()
                        self.PlayGame = True

                    Setting = self.button1.update(True)
                    if Setting:
                        if Setting:
                            Logo = False
                            self.ButtonsInit(True)
                            self.Settings()
                            self.Setting = True

                    Exit = self.button2.update(True)
                    if Exit:
                        return False

                    if self.PlayGame:
                        main_game = self.game_1.update(True)
                        if main_game:
                            continue
                        train_game = self.game_2.update(True)
                        if train_game:
                            return 'Debug'

                    if self.Setting:
                        self.Settingsliders.update(True)
                        st.Change_Volume((self.volume.percent/100))
                        st.Change_Difficulty(self.difficulty.percent)

                if event.type == pygame.MOUSEBUTTONUP:
                    fire = 0

            if self.pressed_key[pygame.K_ESCAPE]:
                PlayGame = False
                self.PlayGame = False
                Setting = False
                self.Setting = False
                Logo = True
                self.ButtonsInit()

            if self.Setting:
                font = pygame.font.Font('static/fonts/19888.ttf', 50)
                volume = font.render('Volume', True, (255, 255, 255))
                difficulty = font.render('Dufficulty', True, (255, 255, 255))

                self.screen.blit(volume, (350, 350))
                self.screen.blit(difficulty, (350, 500))
                self.Settingsliders.draw(self.screen)
                self.Settingsliders.update()

            if self.PlayGame:
                self.Play_buttons.draw(self.screen)
                self.Play_buttons.update()

            if pygame.mouse.get_focused():
                if fire:
                    mSprite = self.mouse.mouse_spritesGet2()
                    mSprite.draw(self.screen)
                else:
                    mSprite = self.mouse.mouse_spritesGet1()
                    mSprite.draw(self.screen)

            pygame.display.flip()

            self.clock.tick(75)


class FloatingHeroes(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        self.Group = group

        types = ['Hero_b', 'Hero_s', 'Zombie']
        path = f'Main_menu/Floating_heroes/{choice(types)}.png'

        self.original_image = load_image(path)
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.pos = (choice(range(200, 1720)), choice(
            range(200, 880)))
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.speedx = choice([-1, 1])
        self.speedy = choice([-1, 1])
        self.position = pygame.math.Vector2(*self.pos)
        self.i = 0
        self.rotateleft = choice([True, False])

    def update(self):
        if self.position.x < 0 - 128:
            self.position.x = st.ResolutionInt[0]
        if self.position.x > st.ResolutionInt[0] + 128:
            self.position.x = 0
        if self.position.y < 0 - 128:
            self.position.y = st.ResolutionInt[1]
        if self.position.y > st.ResolutionInt[1] + 128:
            self.position.y = 0

        self.image = pygame.transform.rotate(self.original_image, self.i)

        self.rect = self.image.get_rect()

        self.position.x += self.speedx
        self.position.y += self.speedy
        self.rect.center = self.position.x, self.position.y
        if self.rotateleft:
            self.i += 1
        else:
            self.i -= 1


class Button(pygame.sprite.Sprite):
    def __init__(self, screen, text, Group, x, y,
                 size=(256, 64), setting=False):
        super().__init__(Group)
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.Setting_button = setting
        self.screen = screen
        self.text = text
        self.size = size
        self.x = x + 10
        self.y = y + 10

        self.image = pygame.Surface(self.size)
        self.Button1 = pygame.transform.scale(load_image(
            'Main_menu/Buttons/Button1.png'), self.size)
        self.Button2 = pygame.transform.scale(load_image(
            'Main_menu/Buttons/Button1.1.png'), self.size)
        self.Button3 = pygame.transform.scale(load_image(
            'Main_menu/Buttons/Button1.2.png'), self.size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.font = pygame.font.Font('static/fonts/19888.ttf', 40)
        self.text = self.font.render(f'{text}', True, (255, 255, 255))
        self.screen.blit(self.text, (self.x, self.y))

    def update(self, clickedOn=False):
        mouse_pos = pygame.mouse.get_pos()
        if self.Setting_button:
            self.image = self.Button1
            self.screen.blit(self.text, (850, self.y))
            return None

        if (
            mouse_pos[0] >= self.rect.x and
            mouse_pos[1] >= self.rect.y and
            mouse_pos[0] <= self.rect.x + self.size[0] and
            mouse_pos[1] <= self.rect.y + self.size[1]
        ):
            self.image = self.Button2
            if clickedOn:
                return True
        else:
            self.image = self.Button1
        self.screen.blit(self.text, (self.x, self.y))

    def kill(self):
        self.text = self.font.render('', True, (255, 255, 255))
        self.update()
        self.rect.x, self.rect.y = -1000, -1000


class Slider(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, Group):
        super().__init__(Group)
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen
        self.image = pygame.transform.scale(load_image(
            'Main_menu/Circle.png'), (40, 40))
        self.rect = self.image.get_rect()
        self.rectangle_pos = (x, y)
        self.rect.x = x
        self.rect.y = y + 7
        self.percent = 50

    def update(self, clickedOn=False):
        pygame.draw.rect(self.screen, pygame.Color(
            'Gray'), (self.rectangle_pos[0],
                      self.rectangle_pos[1] + 25, 200, 5))
        if not clickedOn:
            return None

        mouse_pos = pygame.mouse.get_pos()

        if (
            mouse_pos[0] >= self.rectangle_pos[0] and
            mouse_pos[1] >= self.rectangle_pos[1] and
            mouse_pos[0] <= self.rectangle_pos[0] + 200 and
            mouse_pos[1] <= self.rectangle_pos[1] + 50
        ):
            self.rect.centerx = mouse_pos[0]
            self.percent = int((self.rect.centerx - self.rectangle_pos[0]) / 2)
