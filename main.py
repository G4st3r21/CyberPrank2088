import pygame
from moviepy.editor import VideoFileClip


pygame.init()
size = 1920, 1080
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 60

clip = VideoFileClip('Intro.mp4', target_resolution=size[::-1])
clip.set_fps(60)
clip.preview()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
