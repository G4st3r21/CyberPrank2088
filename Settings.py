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
Volume = 0
Language = 'Russian'


def Change_Volume(volume=0.5):
    global Volume
    Volume = volume
    pygame.mixer.music.set_volume(volume)
    return None


def Change_Resolution(resolution='FHD'):
    global Resolution
    Resolution = resolution
    return Resolutions[resolution]
