#Создай собственный Шутер!
from random import *
from pygame import *

mixer.init()
#создай окно игры
window = display.set_mode((1600, 900))

display.set_caption('ШУТЕР')
win_width = 1600
win_height = 900
#задай фон сцены
background = transform.scale(image.load('back.png'), (1600,900))
mixer.music.load('Wii - Shop Theme.mp3')
mixer.music.play()
mixer.music.set_volume(0.1)
game = True
speed = 5
lost = 0
score = 0
max_lost = 10
goal = 30
health = 2
display.toggle_fullscreen() 
sp_x = 6
sp_y = 6
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (90, 90))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed 

class Player2(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed 
    
run = True
finish = False
clock = time.Clock()
FPS = 144
font.init()
font = font.SysFont('Arial', 70)
player1 = Player2('photo_2022-04-10_13-02-38.jpg', 250, win_height - 200, 8)
player2 = Player1('photo_2022-04-10_13-02-38.jpg', 1250, win_height - 200, 8)
ball = GameSprite('pngegg.png', 800, 450, 2)
cock = mixer.Sound('cock.ogg')
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False    
    lose = font.render('YOU LOSE', 1, (255, 0, 0))
    win = font.render('YOU WIN!', 1, (0, 0, 255))
    if finish != True:
        window.blit(background,(0, 0))
        ball.rect.x += sp_x
        ball.rect.y += sp_y
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            sp_x *= -1
            sp_y *= 1
            cock.play()
        if ball.rect.y > win_height-120 or ball.rect.y < 0:
            sp_y *= -1
            cock.play()
        if ball.rect.x < 0 or ball.rect.x > 1500:
            mixer.music.stop()
            mixer.music.load('lose.ogg')
            mixer.music.play()
            window.blit(lose, (600,400))
            finish = True
        player1.update()
        player1.reset()
        player2.update()
        player2.reset()
        ball.update()
        ball.reset()
        display.update()
        clock.tick(FPS)