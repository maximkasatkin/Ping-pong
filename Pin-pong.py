from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y  =player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and player.rect.y > 5:
            player.rect.y -= 5
        if key_pressed[K_DOWN] and player.rect.y < win_height - 150:
            player.rect.y  += 5
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and player.rect.y > 5:
            player.rect.y -= 5
        if key_pressed[K_s] and player.rect.y < win_height - 150:
            player.rect.y  += 5

back = (200, 255, 255)
win_height = 500
win_widh = 600
window = display.set_mode((win_widh, win_height))
window.fill(back)

run = True
finish = False
clock = time.Clock()
FPS = 60

racket2 = Player('racket.png', 10, 200, 50, 150, 4)
racket1 = Player('racket.png', 540, 200, 50, 150, 4)

speed_x = 3
speed_y = 3

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        window.fill(back)
        racket2.update_l()
        racket1.update_r()

        racket1.reset()
        racket2.reset()
    
    display.update()
    clock.tick(FPS)