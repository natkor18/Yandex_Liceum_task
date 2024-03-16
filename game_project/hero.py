import pygame

FPS = 17

class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, group):
        pygame.sprite.Sprite.__init__(self)

        self.index = 0 #индекс для смены изображений - эффект анимации героя
        self.x = x  # первая координата героя
        self.y = y
        self.speed = 15 #скорость передвижения героя
        self.is_jump = False
        self.count_jump = 7

        #Спрайты героя
        images_girls = [f'hero{str(i)}_right.png' for i in range(1, 7)]
        hero_surf_images = [pygame.image.load("images/hero/" + path).convert_alpha() for path in images_girls]
        self.hero_surf = [pygame.transform.scale(i, (40, 70)) for i in hero_surf_images]

        # Спрайты героя  - вправо/влево
        self.hero_surf_right = [i for i in self.hero_surf]
        self.hero_surf_left = [pygame.transform.flip(i, 180, 0) for i in self.hero_surf]

        self.image = self.hero_surf_right[self.index]
        self.rect = self.image.get_rect(center=(self.x,  self.y))
        self.add(group)

#Смена спрайтов - анимация героя
    def update(self):
        clock = pygame.time.Clock()
        self.index = (self.index + 1) % 6
        self.image = self.hero_surf[self.index]
        clock.tick(FPS)


#Перемещение героя вправо-влево по нажатию клавиш "стрелка" (влево/вправо)
    def move(self, w, right=True):
        if right:
            self.image = self.hero_surf_right[self.index]
            self.rect.x += self.speed
            if self.rect.x > w - self.rect.width:
                self.rect.x = w - self.rect.width
        if not right:
            self.image = self.hero_surf_left[self.index]
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.rect.x = 0

    def jump(self, h, is_jump):
        if is_jump:
            if self.count_jump >= -7:
                if self.count_jump > 0:
                    self.rect.y -= (self.count_jump ** 2)
                else:
                    self.rect.y += (self.count_jump ** 2)
                self.count_jump -= 1
            else:
                self.is_jump = False
                self.count_jump = 7





