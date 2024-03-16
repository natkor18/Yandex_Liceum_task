import pygame
import os
import sys
pygame.mixer.pre_init(44100, -16, 1, 512)

RED = (139, 0, 0)
def terminate():
    pygame.quit()
    sys.exit()

def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    if not os.path.isfile(fullname):
        print("Файл не найден", fullname)
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    image = pygame.transform.scale(image, (500, 400))
    return image

def finish_screen(score_game, score_life):
    WINDOWS_SIZE = WIDTH, HEIGHT = 500, 400
    FPS = 10
    pygame.init()

    screen = pygame.display.set_mode(WINDOWS_SIZE)
    pygame.display.set_caption("Маша собирает монтеки")
    clock = pygame.time.Clock()

    music_name = "data/winnner.mp3"
    text_win = ["Win!"]
    text_lost = ["Lost!"]
    if score_game >= 100 and score_life > 0:
        remarka = text_win
        name ='win.png'
    else:
        remarka = text_lost
        name = 'finish_screen.png'
        music_name = "data/shejmm.mp3"
    music_play = pygame.mixer.Sound(music_name)
    music_play.play()

    fon = pygame.transform.scale(load_image(name), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 80)
    text_coord = 150

    for line in remarka:
        string_rendered = font.render(line, 1, RED)
        intro_rect = string_rendered.get_rect()
        text_coord += 50
        intro_rect.top = text_coord
        intro_rect.x = WIDTH // 2 - 60
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)