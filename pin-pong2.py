from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y  =player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 5
        if key_pressed[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y  += 5
    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 5
        if key_pressed[K_s] and self.rect.y < win_height - 150:
            self.rect.y  += 5

back = (200, 255, 255)
win_height = 500
win_widh = 600
window = display.set_mode((win_widh, win_height))
window.fill(back)

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('Player 1 Lose', True, (180,0,0))
lose2 = font1.render('Player 2 Lose', True, (180,0,0))

speed_x = 3
speed_y = 3

run = True
finish = False
clock = time.Clock()
FPS = 60


racket1 = Player('racket.png',10,200,50,150,4)
racket2 = Player('racket.png',540,200,50,150,4)
ball = GameSprite('tenis_ball.png',200,200,50,50,4)

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


        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y*= -1
        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(200,200))


        if ball.rect.x > win_widh - 50:
            finish = True
            window.blit(lose2,(200,200))


        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)