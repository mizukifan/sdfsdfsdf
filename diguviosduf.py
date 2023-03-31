from pygame import *

win = display.set_mode((700,500))
win.fill((106,174,233))
clock = time.Clock()
fps = 120

class GameSprite(sprite.Sprite):
    def __init__(self,player_name,speed,x,y):
        super().__init__()
        self.image = transform.scale(image.load(player_name),(50,50))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        win.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -=self.speed
        elif keys[K_DOWN] and self.rect.y < 80:
            self.rect.y += self.speed
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -=self.speed
        elif keys[K_s] and self.rect.y < 80:
            self.rect.y += self.speed


while True:
    win.fill((106,174,233))
    
    display.update()
    clock.tick(fps)