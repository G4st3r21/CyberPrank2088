import pygame


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, group, direct=0):
        super().__init__(group)
        self.frames = []
        self.frame_count = [3, 3, 3, 3, 3, 3, 3, 3]
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        if direct:
            self.frames = self.frames[::-1]

    def cut_sheet(self, sheet, columns, rows):
        num = 0
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                for _ in range(self.frame_count[num]):
                    self.frames.append(sheet.subsurface(pygame.Rect(
                            frame_location, self.rect.size)))
                num = (num + 1) % 8
        print(len(self.frames))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
