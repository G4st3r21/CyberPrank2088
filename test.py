import pygame
pygame.init()

BACKGROUND_COLOR = (0, 0, 0)


class Player(pygame.sprite.Sprite):

    def __init__(self, position=(0, 0)):
        super(Player, self).__init__()
        self.original_image = pygame.Surface((32, 32))
        pygame.draw.lines(self.original_image, (255, 255, 255),
                          True, [(16, 0), (0, 31), (31, 31)])
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.position = pygame.math.Vector2(*position)

    def update(self):
        """Updates the players orientation."""
        mouse_pos = pygame.math.Vector2(*pygame.mouse.get_pos())

        rel_mouse_pos = mouse_pos - self.position

        y_axis = pygame.math.Vector2(0, -1)
        angle = -y_axis.angle_to(rel_mouse_pos)

        self.image = pygame.transform.rotate(
            self.original_image, angle).convert()

        self.rect = self.image.get_rect()

        self.rect.center = self.position.x, self.position.y


screen = pygame.display.set_mode((720, 480))
player = Player(position=(300, 250))

while True:
    screen.fill(BACKGROUND_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    player.update()
    screen.blit(player.image, player.rect)
    pygame.display.update()
