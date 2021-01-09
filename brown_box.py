import os
import random

import pygame

pygame.init()
fps = 60
gravity = 0.8

clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 300))


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


WIDTH = 400
HEIGHT = 300

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# для отслеживания улетевших частиц
# удобно использовать пересечение прямоугольников
screen_rect = (0, 0, WIDTH, HEIGHT)


class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера
    chips = [pygame.transform.scale(load_image('доска.png', -1), (20, 20))]
    for scale in (5, 10, 20):
        chips.append(pygame.transform.scale(chips[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.image = random.choice(self.chips)
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость - это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой
        self.gravity = gravity

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(screen_rect):
            self.kill()


def create_particles(position):
    # количество создаваемых частиц
    particle_count = 7
    # возможные скорости
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))


# class Brown_box(pygame.sprite.Sprite):
#     image = pygame.transform.scale(load_image('sprite_bbox.png'), (32, 32))
#
#     def __init__(self):
#         super().__init__(all_sprites)
#         self.image = Brown_box.image
#         self.rect = self.image.get_rect()
#         # вычисляем маску для эффективного сравнения
#         self.mask = pygame.mask.from_surface(self.image)


all_sprites = pygame.sprite.Group()
# b_box = Brown_box()

# pygame.mouse.set_visible(1)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # создаем частицы по щелчку мыши
            create_particles(pygame.mouse.get_pos())

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
