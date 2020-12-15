import os
import sys
import pygame


pygame.init()
size = width, height = 1440, 720
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Герой двигается')


def load_image(name, colorkey=None):
    fullname = os.path.join('sprites\Космонавт', name)

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


left_sprites = pygame.sprite.Group()
rigth_sprites = pygame.sprite.Group()
def_sprite = pygame.sprite.Group()
right = []
left = []
for i in range(1, 8):
    right_sprite = pygame.sprite.Sprite()
    image = load_image(f"Космонавт_run_R{i}.png")
    right_sprite.image = pygame.transform.scale(image, (128, 128))
    right_sprite.rect = right_sprite.image.get_rect()
    right_sprite.rect.x = i * 10
    right_sprite.rect.y = 0
    right.append(right_sprite)
    rigth_sprites.add(right_sprite)
for i in range(1, 8):
    left_sprite = pygame.sprite.Sprite()
    image = load_image(f"Космонавт_run_L{i}.png")
    left_sprite.image = pygame.transform.scale(image, (128, 128))
    left_sprite.rect = left_sprite.image.get_rect()
    left_sprite.rect.x = i * -10
    left_sprite.rect.y = 0
    left.append(left_sprite)
    left_sprites.add(left_sprite)


d_sprite = pygame.sprite.Sprite()
image = load_image("Космонавт_stand_R1.png")
d_sprite.image = pygame.transform.scale(image, (128, 128))
d_sprite.rect = d_sprite.image.get_rect()
d_sprite.rect.x = 0
d_sprite.rect.y = 0
def_sprite.add(d_sprite)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill((255, 255, 255))

        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP]:
            for i in right:
                i.rect.y -= 10
            for i in left:
                i.rect.y -= 10
            d_sprite.rect.y -= 10
            def_sprite.draw(screen)
        elif pressed_key[pygame.K_DOWN]:
            for i in right:
                i.rect.y += 10
            for i in left:
                i.rect.y += 10
            d_sprite.rect.y += 10
            def_sprite.draw(screen)
        elif pressed_key[pygame.K_LEFT]:
            left_sprites.draw(screen)
            left_sprites.update()
            pygame.time.delay(30)
            for i in right:
                i.rect.x -= 60
            for i in left:
                i.rect.x -= 60
            d_sprite.rect.x -= 60
        elif pressed_key[pygame.K_RIGHT]:
            rigth_sprites.draw(screen)
            rigth_sprites.update()
            pygame.time.delay(30)
            for i in right:
                i.rect.x += 60
            for i in left:
                i.rect.x += 60
            d_sprite.rect.x += 60
        else:
            def_sprite.draw(screen)

        print(d_sprite.rect.x, d_sprite.rect.y)

        pygame.display.flip()

pygame.quit()
