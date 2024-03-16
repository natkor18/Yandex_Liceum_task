import pygame

class Heart(pygame.sprite.Sprite):

    def __init__(self, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(130, 35))
        self.add(group)

