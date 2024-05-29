import pygame


class HUD:

    def __init__(self, cx, cy, sx, sy):

        # Controls
        self.con_x = cx
        self.con_y = cy
        self.controls = pygame.image.load("controls.png")
        self.controls_size = self.controls.get_size()
        self.controls_rect = pygame.Rect(90, 180, self.controls_size[0], self.controls_size[1])

        # Stats
        self.stats_x = sx
        self.stats_y = sy
        self.stats = pygame.image.load("stats.png")
        self.stats_size = self.stats.get_size()
        self.stats_rect = pygame.Rect(2, 2, self.stats_size[0], self.stats_size[1])


