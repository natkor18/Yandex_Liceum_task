import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, w, y, speed, surf, danger, group):
        pygame.sprite.Sprite.__init__(self)
        self.w = w
        self.image = surf
        self.rect = self.image.get_rect(center=(self.w + 10, y))
        self.speed = speed
        self.danger = danger
        self.add(group)

    def update(self, *args):
        if self.rect.x > args[0]:
            self.rect.x -= self.speed
        else:
            self.kill()
