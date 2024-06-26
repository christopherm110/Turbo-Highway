import pygame


class Background:

    def __init__(self):
        self.x = 280
        self.y = -360
        self.image = pygame.image.load("Assets/long_road.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 2

    def down_scroll(self):
        self.y = self.y + self.delta

        if self.y > 0:
            self.y = -360
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def restart(self):
        self.x = 280
        self.y = -360
        self.image = pygame.image.load("Assets/long_road.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 2
