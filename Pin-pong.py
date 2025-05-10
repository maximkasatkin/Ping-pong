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
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and player.rect.y > 5:
            player.rect.y -= 12
        if key_pressed[K_DOWN] and player.rect.y < 430:
            player.rect.y  += 12
        if key_pressed[K_LEFT] and player.rect.x > 5:
            player.rect.x -= 12
        if key_pressed[K_RIGHT] and player.rect.x < 620:
            player.rect.x  += 12