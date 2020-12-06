import os
import sys
import pygame


pygame.init()
size = width, height = 300, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Герой двигается')


def load_image(name, colorkey=None):
    fullname = os.path.join('sprites\Police_run', name)

    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
    if colorkey == -1:
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


all_sprites = pygame.sprite.Group()
for i in range(1, 6):
    sprite = pygame.sprite.Sprite()
    image = load_image(f"Police_run_right{i}.png")
    sprite.image = pygame.transform.scale(image, (128, 128))
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 0
    sprite.rect.y = 0
    all_sprites.add(sprite)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP]:
            sprite.rect.y = -10
        if pressed_key[pygame.K_DOWN]:
            sprite.rect.y = +10
        if pressed_key[pygame.K_LEFT]:
            sprite.rect.x = -10
        if pressed_key[pygame.K_RIGHT]:
            sprite.rect.x = +10

        all_sprites.update()
        screen.fill((255, 255, 255))
        all_sprites.draw(screen)

        pygame.display.flip()

pygame.quit()
