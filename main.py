import pygame
from moviepy.editor import VideoFileClip
from Hero_class import Players_Hero


Resolutions = {
    'FHD': (1920, 1080),
    'HD+': (1440, 1080),
    'HD': (1080, 720),
    'HQ': (800, 600)
}

# ------------------------GAME INITIALIZATION------------------------- #

pygame.init()
size = Resolutions['HD+']
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 60
player = Players_Hero('Синий', screen)

# -----------------------------GAME INTRO----------------------------- #

clip = VideoFileClip('static/video/Intro.mp4', target_resolution=size[::-1])
clip.set_fps(60)
clip.preview()


# sound = pygame.mixer.music.load("static/audio/Hyper - Spoiler.mp3")
# pygame.mixer.music.play()

# ----------------------------GAME WORKING---------------------------- #

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pressed_key = pygame.key.get_pressed()

    # ------------------------Moving-------------------------- #
    if pressed_key[pygame.K_w] and pressed_key[pygame.K_a]:
        player.Move_UL()
    elif pressed_key[pygame.K_w] and pressed_key[pygame.K_d]:
        player.Move_UR()
    elif pressed_key[pygame.K_s] and pressed_key[pygame.K_a]:
        player.Move_DL()
    elif pressed_key[pygame.K_s] and pressed_key[pygame.K_d]:
        player.Move_DR()
    elif pressed_key[pygame.K_w]:
        player.Move_Up()
    elif pressed_key[pygame.K_s]:
        player.Move_Down()
    elif pressed_key[pygame.K_a]:
        player.Move_Left()
    elif pressed_key[pygame.K_d]:
        player.Move_Right()
    elif not (pressed_key[pygame.K_w] or pressed_key[pygame.K_s] or
              pressed_key[pygame.K_a] or pressed_key[pygame.K_d]):
        player.Stand()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
