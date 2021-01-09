import pygame


Resolutions = {
    'FHD': (1920, 1080),
    'HD+': (1440, 1080),
    'HD': (1080, 720),
    'HQ': (800, 600)
}

Resolution = 'FHD'
ResolutionInt = Resolutions[Resolution]
FPS = 60
Volume = .3
Language = 'Russian'
Difficulty = 1


def Change_Volume(volume=0.5):
    global Volume
    Volume = volume
    pygame.mixer.music.set_volume(volume)
    return None


def Change_Resolution(resolution='FHD'):
    global Resolution
    Resolution = resolution
    return Resolutions[resolution]


def Change_Difficulty(difficulty=50):
    global Difficulty
    if difficulty in range(40, 61):
        Difficulty = 1
    elif difficulty in range(61, 81):
        Difficulty = 2
    elif difficulty in range(81, 101):
        Difficulty = 3
    return None
